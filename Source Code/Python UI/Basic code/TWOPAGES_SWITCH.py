'''
Created on 25 Aug 2017

@author: smathireddy
'''
# import tkinter as tk                # python 3
# from tkinter import font  as tkfont # python 3
import Tkinter as tk1     # python 2
import tkFont as tkfont  # python 2

class SampleApp(tk1.Tk):

    def __init__(self, *args, **kwargs):
        tk1.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='TimesNewRoman', size=18, weight="bold", slant="roman")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk1.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, CreateMonitors, MonitorLogs,TransferLogs,HostConfiguration):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(tk1.Frame):

    def __init__(self, parent, controller):
        tk1.Frame.__init__(self, parent)
        self.controller = controller
        label = tk1.Label(self, text="OPEN FILE TRANSFER EDITION", width=25, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label.config(bg='black', fg='yellow',bd=10)   
           
        button1 = tk1.Button(self, text=" CREATE MONITORS", width=25,
                            command=lambda: controller.show_frame("CreateMonitors"))
        button1.config(bg='navy', fg='white', bd=5)
         
        button2 = tk1.Button(self, text="MONITOR LOGS",width=25,
                            command=lambda: controller.show_frame("MonitorLogs"))
        button2.config(bg='navy', fg='white', bd=5)
         
        button3 = tk1.Button(self, text=" TRANSFER LOGS",width=25,
                            command=lambda: controller.show_frame("TransferLogs"))
        button3.config(bg='navy', fg='white', bd=5) 
        
        button4 = tk1.Button(self, text="ONE TIME TRANSFER",width=25,
                            command=lambda: controller.show_frame("OneTimeTransfer"))
        button4.config(bg='navy', fg='white', bd=5)
         
        button5= tk1.Button(self, text=" SCHEDULED TRANSFER",width=25,
                            command=lambda: controller.show_frame("ScheduledTransfer"))
        button5.config(bg='navy', fg='white', bd=5) 
        
        button6 = tk1.Button(self, text="HOST CONFIGURATION",width=25,
                            command=lambda: controller.show_frame("HostConfiguration"))
        button6.config(bg='navy', fg='white', bd=5) 
        
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()

class CreateMonitors(tk1.Frame):

    def __init__(self, parent, controller):
        tk1.Frame.__init__(self, parent)
        self.controller = controller
        label = tk1.Label(self, text="Welcome to Create Monitors Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label.config(bg='black', fg='yellow',bd=10) 
        
        button = tk1.Button(self, text="Go to the Home page",width=25,
                           command=lambda: controller.show_frame("HomePage"))
        button.config(bg='navy', fg='white', bd=5)  
        button.pack()


class MonitorLogs(tk1.Frame):

    def __init__(self, parent, controller):
        tk1.Frame.__init__(self, parent)
        self.controller = controller
        label = tk1.Label(self, text="Welcome to Monitor Logs Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label.config(bg='black', fg='yellow',bd=10) 
         
        button = tk1.Button(self, text="Go to the Home page",
                           command=lambda: controller.show_frame("HomePage"))
        button.config(bg='navy', fg='white', bd=5) 
        button.pack()

    
class TransferLogs(tk1.Frame):

    def __init__(self, parent, controller):
        tk1.Frame.__init__(self, parent)
        self.controller = controller
        label = tk1.Label(self, text="Welcome to Transfers Logs Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label.config(bg='black', fg='yellow',bd=10) 
         
        button = tk1.Button(self, text="Go to the Home page",
                           command=lambda: controller.show_frame("HomePage"))
        button.config(bg='navy', fg='white', bd=5) 
        button.pack()
        
class HostConfiguration(tk1.Frame):

    def __init__(self, parent, controller):
        tk1.Frame.__init__(self, parent)
        self.controller = controller
        label = tk1.Label(self, text="Welcome to HostConfiguration Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label.config(bg='black', fg='yellow',bd=10) 
         
        button = tk1.Button(self, text="HostConfig",
                           command=lambda: controller.show_frame("HostConfig"))
        button.config(bg='navy', fg='white', bd=5) 
        button.pack()
    
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    
    
    
    
    
    
    
    
#     # import tkinter as tk                # python 3
# # from tkinter import font  as tkfont # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
# 
# class SampleApp(tk.Tk):
# 
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
# 
#         self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
# 
#         # the container is where we'll stack a bunch of frames
#         # on top of each other, then the one we want visible
#         # will be raised above the others
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
# 
#         self.frames = {}
#         for F in (StartPage, PageOne, PageTwo):
#             page_name = F.__name__
#             frame = F(parent=container, controller=self)
#             self.frames[page_name] = frame
# 
#             # put all of the pages in the same location;
#             # the one on the top of the stacking order
#             # will be the one that is visible.
#             frame.grid(row=0, column=0, sticky="nsew")
# 
#         self.show_frame("StartPage")
# 
#     def show_frame(self, page_name):
#         '''Show a frame for the given page name'''
#         frame = self.frames[page_name]
#         frame.tkraise()
# 
# 
# class StartPage(tk.Frame):
# 
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is the start page", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
# 
#         button1 = tk.Button(self, text="Go to Page One",
#                             command=lambda: controller.show_frame("PageOne"))
#         button2 = tk.Button(self, text="Go to Page Two",
#                             command=lambda: controller.show_frame("PageTwo"))
#         button1.pack()
#         button2.pack()
# 
# 
# class PageOne(tk.Frame):
# 
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 1", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()
# 
# 
# class PageTwo(tk.Frame):
# 
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 2", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()
# 
# 
# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()