from tkinter import *
from PIL import ImageTk, Image
app = Tk()


# Getting Screen Dimensions
width, height = app.winfo_screenwidth(), app.winfo_screenheight()

# Title of the window
app.title("Time Table Scheduler")

# Disabled the ability to resize the window
app.wm_minsize(width, height)
app.resizable(height=False, width=False)

# To initialize the window in full screen mode
app.attributes("-fullscreen", True)

mainloop()