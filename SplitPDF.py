import tkinter as tk
from tkinter import ttk
from pdf_split import pdf_split
import os, re

WIDTH = 800
HEIGHT = 1000

def get_input(filename,first,last,keep_pieces):
    try:
        pdf_split(filename,first,last,keep_pieces)
        l5["text"] = "Everything worked perfectly. Your file has been split!"
    except FileNotFoundError:
        l5["text"] = "File is not located in the directory"
    except ValueError:
        l5["text"] = "Wrong data type supplied. Please check your input"
    except IndexError:
        l5["text"] = "Supplied page number is not in range."
    except Exception:
        l5["text"] = "An unidentified error occured."

# Window
root = tk.Tk(className="SplitPDF") 

# Predefine Window width and height
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

# Background image
background_image = tk.PhotoImage(file=os.path.join("Assets","split.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

# Setup and place widgets
# User input arguments

# Frame 1
f1 = tk.Frame(root, bg = "#0731db",bd = 5)
f1.place(relx=0.5,rely= 0.05, relwidth = 0.8,relheight = 0.2,anchor = "n")

# filename -> widgets: label and entry?
l1 = tk.Label(f1, text = "Filename", bg = "#fcfcfc")
l1.place(relwidth = 0.45, relheight = 0.15)
files = [x for x in os.listdir() if re.search(".pdf",x)]
e1 = ttk.Combobox(f1, values=files)
e1.place(relx = 0.55, relwidth = 0.45, relheight = 0.15)

# first page -> label and entry
l2 = tk.Label(f1, text = "First page", bg = "#fcfcfc")
l2.place(rely = 0.175,relwidth = 0.45, relheight = 0.15)
e2 = tk.Entry(f1)
e2.place(relx = 0.55, rely = 0.175,relwidth = 0.45, relheight = 0.15)

# last page -> label and entry
l3 = tk.Label(f1, text = "Last Page", bg = "#fcfcfc")
l3.place(rely = 0.35,relwidth = 0.45, relheight = 0.15)
e3 = tk.Entry(f1)
e3.place(relx = 0.55, rely = 0.35,relwidth = 0.45, relheight = 0.15)

# keep all pieces -> label and entry
l4 = tk.Label(f1, text = "Keep all pieces", bg = "#fcfcfc")
l4.place(rely = 0.525,relwidth = 0.45, relheight = 0.15)
var = tk.IntVar()
r1 = tk.Radiobutton(f1, text = "Yes", variable=var, value = True)
r1.place(relx = 0.55, rely = 0.525,relwidth = 0.45/2, relheight = 0.15)
r2 = tk.Radiobutton(f1, text = "No", variable=var, value = False)
r2.place(relx = 0.55+0.45/2, rely = 0.525,relwidth = 0.45/2, relheight = 0.15)
#e4 = tk.Entry(f1)
#e4.place(relx = 0.55, rely = 0.525,relwidth = 0.45, relheight = 0.15)

# Submit button
b1 = tk.Button(f1, text = "Split!", font = 30, bg = "black", fg = "white", command= lambda: get_input(e1.get(),\
    int(e2.get()),int(e3.get()),var.get()))
b1.place(relx = 0.5, rely = 0.775,relwidth = 0.45, relheight = 0.2, anchor = "n")

# Frame 2
# Message field that tells the user what's happening and errors that occured
f2 = tk.Frame(root, bg = "#0731db",bd = 5)
f2.place(relx=0.5,rely= 0.7, relwidth = 0.8,relheight = 0.2,anchor = "n")

l5 = tk.Label(f2, text = "Hello! I am Mooses and I will split your PDF document in up to three pieces.\n" \
    "Just Save your file in the same directory as the exe file and specify the required information.\n" \
        "Then I shall split your file!")
l5.place(relwidth=1,relheight=1)

root.mainloop()