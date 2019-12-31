from tkinter import *

window=Tk()

def kmConverter():
    print(e1_value.get())
    converted_value = float(e1_value.get())*1.6
    t1.insert(END, converted_value)

b1 = Button(window, text="Calculate", command= kmConverter)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1= Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window)
t1.grid(row=0, column=2)

window.mainloop()