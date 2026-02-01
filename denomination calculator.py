from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#---------------------------------------------------
#Setting up main window

root = Tk
root.title("Denomintation counter")
root.configure(bg="light blue")
root.geometry("650x400")


#Adding Image and labels in main window

upload=Image.open("app_img.jpg")
upload=upload.resize((300,300)) 
image=ImageTk.PhotoImage(upload)

label=Label(root, image=image, bg="light blue")
label.place(x=180,y=20)

label1=Label(
    root,
    text="Hey Use! Welcome to denomination counter application",
    bg="light blue"
)
label1.place(relx=0.5,y=340,anchor=CENTER)


#Function to open messagebox

def msg():
    MsgBox=message.box.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"
    )
    if MsgBox== "ok":
        topwin()


#Adding button in main window

button1=Button(
    root,
    text="Let's get started!",
    command=msg,
    bg="brown",
    fg="white"
)
button1.place(x=260,y=360)


#Function for opening new/top window

def topwin():
    top=Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label=Label(top,text="Enter total amount", bg="light grey")
    entry=Entry(top)

    lb1=Label(
        top,
        text="Here are number of notes for each denomination",
        bg="light grey"
    )
    
    l1=Label(top,text="2000")