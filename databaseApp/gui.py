from tkinter import *
import books_db

#functions


def view_command():
    listbox1.delete(0,END)
    for row in books_db.view():
        listbox1.insert(END, row)

def search_command():
    listbox1.delete(0,END)
    for row in books_db.search(title = title_text.get(), author = author_text.get(), year = year_text.get(), isbn=ISBN_text.get()):
        listbox1.insert(END, row)

def add_command():
    books_db.insert(title = title_text.get(), author = author_text.get(), year = year_text.get(), isbn=ISBN_text.get())
    view_command()

def delete_command():
    books_db.delete(selected_row[0])
    view_command()

def get_selected_row(event):
    global selected_row
    index=listbox1.curselection()[0]
    selected_row = listbox1.get(index)
    
    e1.delete(0,END)
    e1.insert(END, selected_row[1])
    e2.delete(0,END)
    e2.insert(END, selected_row[2])
    e3.delete(0,END)
    e3.insert(END, selected_row[3])
    e4.delete(0,END)
    e4.insert(END, selected_row[4])


def update_command():
    books_db.update(selected_row[0], title = title_text.get(), author = author_text.get(), year = year_text.get(), isbn=ISBN_text.get())
    view_command()


#gui 

window = Tk()

#top lookup section
l1 = Label(window, text="title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN ID")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

ISBN_text = StringVar()
e4 = Entry(window, textvariable=ISBN_text)
e4.grid(row=1, column=3)


#Left listbox with scrollbar
listbox1 = Listbox(window, height=6, width=35)
listbox1.grid(row=2, column=0, rowspan =6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=1, column=2, rowspan=8)

listbox1.configure(yscrollcommand = sb1.set)
sb1.configure(command=listbox1.yview)

listbox1.bind("<<ListboxSelect>>", get_selected_row)

#right buttons
b1 = Button(window, text="View All", width = 10, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width = 10, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width = 10, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width = 10, command = update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width = 10, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width = 10, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()