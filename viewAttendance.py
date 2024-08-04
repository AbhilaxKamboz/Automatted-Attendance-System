# import csv
# from tkinter import *
#
# root = Tk()
# root.geometry()  # Optional: Set window size
#
# ent1 = Entry(root, font=('times new roman', 20), fg='white', bg='Skyblue',width=50)
# ent1.place(x=100, y=100)
# # ent1.place()
# with open("Attendance.csv", "r") as f:
#     reader = csv.DictReader(f)
#
#     for i in reader:
#         print(i)
#         ent1.delete(0, END)
#         ent1.insert(0, i)
#
# root.mainloop()


import csv
from tkinter import *
from tkinter import ttk

def populate_treeview(tree, data):
    for row in data:
        tree.insert("", "end", values=row)

def load_csv(file_path):
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)  # Read the first line as headers
        data = [row for row in reader]
    return headers, data

root = Tk()
root.geometry("1000x700")
root.title("CSV Table")

# Load CSV data
csv_file_path = "Attendance.csv"
headers, data = load_csv(csv_file_path)

# Create Treeview
tree = ttk.Treeview(root, columns=headers, show="headings")

# Define columns
for header in headers:
    tree.heading(header, text=header)
    tree.column(header, anchor=CENTER)

tree.pack(expand=True, fill=BOTH)

# Populate Treeview
populate_treeview(tree, data)

root.mainloop()
