from tkinter import *

root = Tk()




# Getting Screen Dimensions
width, height = root.winfo_screenwidth(), root.winfo_screenheight()

# Title of the window
root.title("Time Table Scheduler")

# Icon of the window
root.wm_iconbitmap(bitmap="./favicon.ico")

# Disabled the ability to resize the window
root.resizable(False)

# To initialize the window in full screen mode
root.attributes("-fullscreen", True)

mainloop()