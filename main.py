from tkinter import *
from mettler_toledo_device import MettlerToledoDevice
from tkinter import ttk

class Application(Frame):
        def __init__(self, master):
                Frame.__init__(self, master)
                self.screen_widgets()
                global ent1

        def getValue(self, buttonValue):
            
            if (buttonValue == 1):
                ent1.delete(0, END)
                getA1 = dev.get_weight()
                ent1.insert(0, getA1[0])

        def screen_widgets(self):

                global dev
                dev = MettlerToledoDevice(port='COM7') # Windows specific port

                rndlbl=Label(root, text='Mettler Toledo Scale Value', font=("Arial",15))
                rndlbl.place(x=50,y=5,width=300,height=25)

                ent1=ttk.Entry(root)
                ent1.place(x=20,y=50,width=150,height=25)

                getbtn1=ttk.Button(root, text='Get Value', command=lambda: self.getValue(1))
                getbtn1.place(x=200,y=50,width=70,height=25)



root = Tk()
root.title("mass")
root.geometry("350x200")
width=760
height=500
App = Application(root)
root.mainloop()
