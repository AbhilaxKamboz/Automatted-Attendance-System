from tkinter import *
from tkinter import ttk

root =Tk()
root.configure(background="skyblue")

tree = ttk.Treeview(root)

tree["columns"]=("Id","Name","Age")

tree.column("#0",width=0,stretch=NO)
tree.column("Id",anchor=CENTER,width=80)
tree.column("Name",anchor=W,width=120)
tree.column("Age",anchor=CENTER,width=80)

tree.heading("#0",text="",anchor=CENTER)
tree.heading("Id",text="ID",anchor=CENTER)
tree.heading("Name",text="Name",anchor=CENTER)
tree.heading("Age",text="Age",anchor=CENTER)

data= [
    (1,"Abc",20),
    (2,"Def",15),
    (3,"Ghi",30),
]
for i in data:
    tree.insert("",END,values=i)


tree.pack(pady=20)

root.mainloop()