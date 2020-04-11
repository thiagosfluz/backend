try:

    import tkinter
except ImportError: #Python2
    import TKinter as tkinter


import os
mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')

label = tkinter.Label (mainWindow, text='Tkinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)


mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

filelist = tkinter.Listbox(mainWindow)
filelist.grid(row=1, column=0, sticky = 'nsew', rowspan = 2)
filelist.config(border=2, relief='sunken')

for zone in os.listdir('/usr/bin'):
    filelist.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=filelist.yview)
listScroll.grid(row=1, column=1, sticky = 'nsw', rowspan=2)

filelist['yscrollcommand'] = listScroll.set

#frame for the radio buttons
optionframe = tkinter.LabelFrame(mainWindow, text='File Details')
optionframe.grid(row=1, column=2, sticky='ne')

rbvalue = tkinter.IntVar()
rbvalue.set(3)

#Radio Buttons

radio1 = tkinter.Radiobutton(optionframe, text='Filename', value=1, variable = rbvalue)
radio2 = tkinter.Radiobutton(optionframe, text='Path', value=2, variable = rbvalue)
radio3 = tkinter.Radiobutton(optionframe, text='Timestamp', value=3, variable = rbvalue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')




mainWindow.mainloop()

print(rbvalue.get())