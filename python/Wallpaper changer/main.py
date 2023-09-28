print("Importing modules...")
import os, random
import ctypes

print("Creating wallpaper function...")

def set_wallpaper(path:str):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

Input_folder = "C:/Users/Aavaa/Pictures/Wallpapers/"
print("Getting wallpaper list...")
List_of_wallpapers = os.listdir(Input_folder)
print("Checking wallpaper names...")
for count, Filename in enumerate(List_of_wallpapers):
    if not Filename[0].isdigit() or int(Filename[0]) != count:
        os.rename(Input_folder + Filename, Input_folder + str(count) + Filename[-4 :])

print("Setting wallpaper...")
set_wallpaper(Input_folder + List_of_wallpapers[random.randint(0, len(List_of_wallpapers) - 1)])

print("Done.")
input()