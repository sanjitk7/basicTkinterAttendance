# import tkinter as tk

# def doNothing():
#     print("hi")

# root = tk.Tk()

# menu = tk.Menu(root)
# root.config(menu=menu)

# subMenu = tk.Menu(menu)
# menu.add_cascade(label="File", menu=subMenu)
# subMenu.add_command(label="New", command=doNothing)


# root.mainloop()

import tkinter

def page1():
    page2text.pack_forget()
    page1text.pack()

def page2():
    page1text.pack_forget()
    page2text.pack()

window = tkinter.Tk()

page1btn = tkinter.Button(window, text="Page 1", command=page1)
page2btn = tkinter.Button(window, text="Page 2", command=page2)

page1text = tkinter.Label(window, text="This is page 1")
page2text = tkinter.Label(window, text="This is page 2")

page1btn.pack()
page2btn.pack()
page1text.pack()

window.mainloop()