'''
Created on 18 Aug 2017

@author: smathireddy
'''
from Tkinter import*


def show_entry_fields():
    print("abc")
    print("Host Name: %s\nHost ID: %s\nUser ID: %s\nKafka Port: %s\nCassandra Port: %s" % (e1.get(),e2.get(),e3.get(),e4.get(),e5.get()))

def host_Config():
    root = Tk()
    root.geometry("500x500")
 

    Label(root, text="Host Name").grid(row=0)
    Label(root, text="Host ID").grid(row=1)
    Label(root, text="User ID").grid(row=2)
    Label(root, text="Kafka Port").grid(row=3)
    Label(root, text="Cassandra Port").grid(row=4)

    global e1 
    e1 = Entry(root)
    global e2 
    e2 = Entry(root)
    global e3 
    e3 = Entry(root)
    global e4
    e4= Entry(root)
    global e5 
    e5 = Entry(root)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    
    Button(root, text='Quit', command=root.quit).grid(row=5, column=0, sticky=W, pady=4)
    Button(root, text='Show', command=show_entry_fields).grid(row=5, column=1, sticky=W, pady=4)
    root.mainloop()
host_Config()