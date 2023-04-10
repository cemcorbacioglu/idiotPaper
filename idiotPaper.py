import tkinter as tk
import os
from tkinter import filedialog
import random
import ctypes

def open_wallpaper():
    # Get the path to the current wallpaper
    wallpaper_path = os.path.join(
        os.environ["USERPROFILE"], "AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper"
    )

    # Open the wallpaper in the default browser
    os.startfile("file://" + wallpaper_path)

def set_random_wallpaper():
    # Get the path to the folder containing the wallpapers
    wallpapers_folder = filedialog.askdirectory()

    # Get a list of all the image files in the folder
    image_files = [f for f in os.listdir(wallpapers_folder) if f.endswith(".jpg") or f.endswith(".png")]

    # Select a random image file from the list
    random_image_file = random.choice(image_files)

    # Set the selected image as the wallpaper
    image_path = os.path.join(wallpapers_folder, random_image_file)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)
    os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")


def change_wallpaper():
    # Open a file dialog to select a new wallpaper file
    new_wallpaper_path = filedialog.askopenfilename()

    # Change the wallpaper using the selected file
    os.system('rundll32.exe user32.dll, UpdatePerUserSystemParameters 1, "{0}"'.format(new_wallpaper_path))

window = tk.Tk()
window.title("Idiot Paper")
window.geometry('300x150+400+300')
window.resizable(False, False)


label = tk.Label(window, text="Click 'View Wallpaper' to view your current wallpaper", bd=0, bg='light gray')
label.pack(pady=5)

view_button = tk.Button(window, text="View Wallpaper", command=open_wallpaper, bd=0, bg='dark gray')
view_button.pack(pady=5)

change_button = tk.Button(window, text="Change Wallpaper", command=change_wallpaper, bd=0, bg='dark gray')
change_button.pack(pady=5)

random_button = tk.Button(window, text="Randomize", command=set_random_wallpaper, bd=0, bg='dark gray')
random_button.pack(pady=5)

close_button = tk.Button(window, text="Close", command=window.quit, bd=0, bg='dark gray')
close_button.pack(pady=5)

window.configure(bg='light gray')

window.mainloop()
