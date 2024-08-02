import os
import shutil
from tkinter import Tk, filedialog
from datetime import datetime


# Function to choose a folder
def wybierz_folder():
    root = Tk()
    root.withdraw()  # Hide the main Tkinter window
    folder = filedialog.askdirectory()
    return folder


# List of supported image and video file extensions
obslugiwane_rozszerzenia = [
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.svg', '.ico',  # images
    '.mp4', '.mov', '.wmv', '.avi', '.mkv', '.flv', '.webm', '.vob', '.ogv', '.ogg', '.drc', '.mng', '.qt', '.mpg',
    '.mpeg', '.3gp'  # videos
]


# Function to search the folder
def przeszukaj_folder(wejsciowy_folder, docelowy_folder):
    for root, dirs, files in os.walk(wejsciowy_folder):
        for file in files:
            if any(file.lower().endswith(ext) for ext in obslugiwane_rozszerzenia):
                sciezka_pliku = os.path.join(root, file)

                # Get the file's modification date
                mtime = os.path.getmtime(sciezka_pliku)
                mod_date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d_%H-%M-%S')

                # Create the new file name with modification date
                new_file_name = f"{mod_date}{os.path.splitext(file)[1]}"
                docelowa_sciezka = os.path.join(docelowy_folder, new_file_name)

                # Copy the file
                shutil.copy2(sciezka_pliku, docelowa_sciezka)
                print(f'Skopiowano: {sciezka_pliku} do {docelowa_sciezka}')


# Choose the folder to search
wejsciowy_folder = wybierz_folder()
print(f'Wybrano folder do przeszukania: {wejsciowy_folder}')

# Choose the target folder
docelowy_folder = wybierz_folder()
print(f'Wybrano folder docelowy: {docelowy_folder}')

# Search the folder and copy the files
przeszukaj_folder(wejsciowy_folder, docelowy_folder)
print('Operacja zakończona.')
