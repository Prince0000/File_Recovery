import os
import threading
import time
import pyfiglet
from pathlib import Path

class Recovery:
    def __init__(self, filetype):
        self.filetype = filetype

    def data_recovery(self, fileName, fileStart, fileEnd, fileOffSet, drive_letter, recovered_location):
        drive = f"\\\\.\\{drive_letter}:"
        with open(drive, "rb") as fileD:
            size = 512
            byte = fileD.read(size)
            offs = 0
            drec = False
            rcvd = 0

            while byte:
                found = byte.find(fileStart)
                if found >= 0:
                    drec = True
                    print(f'==== Found {fileName} at location: {hex(found + (size * offs))} ====')
                    timestamp = int(time.time())
                    fileN_path = os.path.join(recovered_location, f'{rcvd}_{timestamp}.{fileName}')
                    with open(fileN_path, "wb") as fileN:
                        fileN.write(byte[found:])
                        while drec:
                            byte = fileD.read(size)
                            bfind = byte.find(fileEnd)
                            if bfind >= 0:
                                fileN.write(byte[:bfind + fileOffSet])
                                fileD.seek((offs + 1) * size)
                                print(f'==== Wrote {fileName} to location: {rcvd}_{timestamp}.{fileName} ====\n')
                                drec = False
                                rcvd += 1
                            else:
                                fileN.write(byte)
                byte = fileD.read(size)
                offs += 1

def progress_bar(total_iterations, current_iteration, bar_length, fill):
    percent = f"{100 * current_iteration / float(total_iterations):.1f}"
    fill_length = int(bar_length * current_iteration / total_iterations)
    bar = fill * fill_length + "-" * (bar_length - fill_length)
    print(f"\rLoading: |{bar}| {percent}%", end="")
    if current_iteration == total_iterations:
        print("\nRunning.........")

def show_menu(recovered_location, available_drives):
    print("=" * 100)
    print(pyfiglet.figlet_format("Data Recovery Tool", font='starwars', justify="center", width=100))
    print("=" * 100)
    print(f'Recovered data will be saved to {recovered_location}')
    print(f"Available Drives are: {available_drives}")
    print("Menu:")
    print("1. Start Data Recovery")
    print("2. Exit")

def main_menu():
    total_iteration = 50
    available_drives = [chr(x) + "" for x in range(65, 91) if os.path.exists(chr(x) + ":")]
    cwd = Path.cwd()
    recovered_location = cwd / 'RecoveredData'
    recovered_location.mkdir(exist_ok=True)

    pdf = Recovery('pdf')
    jpg = Recovery('jpg')
    zip_recovery = Recovery('zip')
    png = Recovery('png')

    while True:
        show_menu(recovered_location, available_drives)
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            start_data_recovery(pdf, jpg, zip_recovery, png, total_iteration, recovered_location, available_drives)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def start_data_recovery(pdf, jpg, zip_recovery, png, total_iteration, recovered_location, available_drives):
    drive_letter = input("Enter Removable Drive Letter: ").capitalize()

    if drive_letter in available_drives:
        for i in range(total_iteration + 1):
            progress_bar(total_iteration, i, 15, ">")
            time.sleep(0.1)

        pdf_thread = threading.Thread(target=pdf.data_recovery, args=('pdf', b'\x25\x50\x44\x46\x2D', b'\x0a\x25\x25\x45\x4f\x46', 6, drive_letter, recovered_location))
        jpg_thread = threading.Thread(target=jpg.data_recovery, args=('jpg', b'\xff\xd8\xff\xe0\x00\x10\x4a\x46', b'\xff\xd9', 2, drive_letter, recovered_location))
        zip_thread = threading.Thread(target=zip_recovery.data_recovery, args=('zip', b'\x50\x4b\x03\x04\x14', b'\x50\x4b\x05\x06', 4, drive_letter, recovered_location))
        png_thread = threading.Thread(target=png.data_recovery, args=('png', b'\x89\x50\x4e\x47', b'\x49\x45\x4e\x44\xae\x42\x60\x82', 8, drive_letter, recovered_location))

        start_time = time.time()
        pdf_thread.start()
        jpg_thread.start()
        zip_thread.start()
        png_thread.start()
        pdf_thread.join()
        jpg_thread.join()
        zip_thread.join()
        png_thread.join()
        end_time = time.time()
        print(f"Data recovery completed in {end_time - start_time} seconds.")
        
        another_recovery = input("Do you want to start another recovery? (1 - Yes, 2 - No): ")
        if another_recovery == '1':
            pass  # The loop will continue for another recovery
        elif another_recovery == '2':
            print("Exiting the program.")
        else:
            print("Invalid choice. Exiting the program.")
    else:
        print("Invalid drive letter. Please enter a valid drive letter.")

if __name__ == "__main__":
    main_menu()
