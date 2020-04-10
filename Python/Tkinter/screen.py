try:

    import tkinter
except ImportError: #Python2
    import TKinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+200')