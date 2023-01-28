from tkinter import *
from PIL import ImageTk, Image


def main():
   app = Tk()

   label = Label(app, text="Generate Time Table",background="#fff", pady=20, font=('Arial', 30, "bold"))
   label.pack()
   
   btn = Button(app, text="Generate TimeTable", )
   btn.pack()

   app.configure(background="white")

   # Getting Screen Dimensions
   width, height = app.winfo_screenwidth(), app.winfo_screenheight()

   # Title of the window
   app.title("Time Table Scheduler")

   # Adding AppIcon
   img = PhotoImage(file="favicon.png")
   app.iconphoto(False, img)

   # Disabled the ability to resize the window
   app.wm_minsize(width, height)
   app.resizable(height=False, width=False)

   # To initialize the window in full screen mode
   app.attributes("-fullscreen", True)

   mainloop()

if __name__ == "__main__":
   main()