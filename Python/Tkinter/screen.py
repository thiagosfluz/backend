try:

    import tkinter
except ImportError: #Python2
    import TKinter as tkinter


import os
mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')

mainWindow['padx'] = 8

label = tkinter.Label (mainWindow, text='Tkinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)


mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)

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
rbvalue.set(1)

#Radio Buttons

radio1 = tkinter.Radiobutton(optionframe, text='Filename', value=1, variable = rbvalue)
radio2 = tkinter.Radiobutton(optionframe, text='Path', value=2, variable = rbvalue)
radio3 = tkinter.Radiobutton(optionframe, text='Timestamp', value=3, variable = rbvalue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')


# widget to display the result
resultlabel = tkinter.Label(mainWindow, text = 'Result')
resultlabel.grid(row=2, column=2, sticky= 'nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

#FRame for the time spinners
timeframe = tkinter.LabelFrame(mainWindow, text='time')
timeframe.grid(row = 3, column =0, sticky='new')

#Time spinners
hourspinner = tkinter.Spinbox(timeframe, width=2, values=tuple(range(0, 24)))
minutespinner = tkinter.Spinbox(timeframe, width=2, from_=0, to=59)
secondspinner = tkinter.Spinbox(timeframe, width=2, from_=0, to =59)

hourspinner.grid(row=0, column=0)
tkinter.Label(timeframe, text=':').grid(row=0, column=1)

minutespinner.grid(row=0, column=2)
tkinter.Label(timeframe, text=':').grid(row=0, column=3)
secondspinner.grid(row=0, column=4)
timeframe['padx'] = 36


#Frame for the date spinners
dateframe = tkinter.Frame(mainWindow)
dateframe.grid(row=4, column=0, sticky='new')

#date labels
daylabel = tkinter.Label(dateframe, text= 'Day')
monthlabel = tkinter.Label(dateframe, text= 'Month')
yearlabel = tkinter.Label(dateframe, text= 'Year')
daylabel.grid(row=0, column=0, sticky= 'w')
monthlabel.grid(row=0, column=1, sticky= 'w')
yearlabel.grid(row=0, column=2, sticky= 'w')


#Date Spinners
dayspin = tkinter.Spinbox(dateframe, width=5, from_=1, to =31)
monthspin = tkinter.Spinbox(dateframe, width=5, values = ("Jan", "Fev", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
yearspin = tkinter.Spinbox(dateframe, width=5, from_=2000, to =2099)


dayspin.grid(row=1, column=0)
monthspin.grid(row=1, column=1)
yearspin.grid(row=1, column=2)




#Buttons
okbutton = tkinter.Button(mainWindow, text='OK')
cancelbutton = tkinter.Button(mainWindow, text = 'Cancel', command = mainWindow.destroy)

okbutton.grid(row=4, column =3, sticky = 'e')
cancelbutton.grid(row =4, column =4, sticky= 'w')



mainWindow.mainloop()

print(rbvalue.get())