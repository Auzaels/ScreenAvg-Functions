from tkinter import *

def screen_avg(win, width, height):
    screenWidth = win.winfo_screenwidth()
    screenHeight = win.winfo_screenheight()
    x = (screenWidth - width)//2
    y = (screenHeight - height)//2
    return win.geometry(f"{width}x{height}+{x}+{y}")

win = Tk()
win.title("Screen Avg")
screen_avg(win,300,300)

win.mainloop()