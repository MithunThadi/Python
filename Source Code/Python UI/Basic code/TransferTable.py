'''
Created on 18 Aug 2017

@author: smathireddy
'''
import Tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = SimpleTable(self,20,6)
        t.pack(side="bottom", fill="x")
        t.set(0,0,"Monitor_Name")
        t.set(0,1,"Job_Name")
        t.set(0,2,"Transfer_ID")
        t.set(0,3,"Source_File")
        t.set(0,4,"Target_File")
        t.set(0,5,"Transfer_Status")
        

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows, columns):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
#               label = tk.Label(self, text="%s/%s" % (row, column),  borderwidth=0, width=10)
                label = tk.Label(self, borderwidth=0, width=20)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()