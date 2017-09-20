'''
Created on 17 Jul 2017

@author: smathireddy
'''

from Tkinter import *

root = Tk()
root.geometry("500x500")
mainframe = Frame(root)
mainframe.grid(column=0,row=11, sticky=(N,W,E,S) )
# mainframe.columnconfigure(0, weight = 1)
# mainframe.rowconfigure(0, weight = 1)
# mainframe.pack(pady = 100, padx = 100)
def show_entry_fields():
    print("Monitor Name: %s\nJob Name: %s\nSource directory: %s\nSource Trigger Pattern: %s\nSource File pattern: %s\nDestination directory: %s\nDestination Trigger Pattern: %s\nDestination File pattern: %s\nMonitor XML File Path: %s" % (e1.get(), e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get()))
def popupMenu1():
    print("")

Label(root, text="Monitor Name").grid(row=0)
Label(root, text="Job Name").grid(row=1)

l = Label(root, text="SOURCE DETAILS").grid(row=2)
Label(root, text="Source directory").grid(row=3)
Label(root, text="Source Trigger Pattern").grid(row=4)
Label(root, text="Source File pattern").grid(row=5)

l = Label(root, text="DESTINATION DETAILS").grid(row=6)
Label(root, text="Destination directory").grid(row=7)
Label(root, text="Destination Trigger Pattern").grid(row=8)
Label(root, text="Destination File pattern").grid(row=9)

l = Label(root, text="POLL DETAILS").grid(row=10)
 
tkvar = StringVar(root)
tkvar1 = StringVar(root) 
# Dictionary with options
choices = { 'Minutes','Seconds','Days','Weeks','Years'}
tkvar.set('Select') # set the default option
 
popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Poll Units").grid(row = 11, column = 1)
popupMenu.grid(row = 12, column =1)
 
 
 # Dictionary with options
Minutes = { '1', '2', '3','4','5','6','7','8','9','10','11','12', '13','14','15','16','17','18','19','20','21','22', '23','24','25','26','27','28','29','30'}
tkvar1.set('Select1') # set the default option

# if tkvar.get() == Minutes :
popupMenu1 = OptionMenu(mainframe, tkvar1, *Minutes)
Label(mainframe, text="Poll Interval").grid(row = 13, column = 1)
popupMenu1.grid(row = 14, column =1)
 
 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
#     print( tkvar1.get() )
# link function to change dropdown
tkvar.trace('w', change_dropdown)
def change_dropdown1(*args):
    print( tkvar1.get() )
tkvar1.trace('w', change_dropdown1  )


Label(root, text="Monitor XML File Path").grid(row=16)
 

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)
e8 = Entry(root)
e9=Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=7, column=1)
e7.grid(row=8, column=1)
e8.grid(row=9, column=1)
e9.grid(row=16,column=1)

Button(root, text='Quit', command=root.quit).grid(row=17, column=0, sticky=W, pady=4)
Button(root, text='Show', command=show_entry_fields).grid(row=17, column=1, sticky=W, pady=4)
root.mainloop()