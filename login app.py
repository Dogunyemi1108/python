#Import necessary libraries
from tkinter import *

#Create window
root=Tk()
root.title('Login app')
root.geometry('400x400')

#Create a frame to organise elememts better
frame= Frame(master=root,height=200,width=360,bg='#d0efff')

#Add widgets
#Add label
lbl1=Label(frame,text="Full Name",bg="#3895D3", fg='white',width=12)
lbl2=Label(frame,text="Email Id",bg="#3895D3", fg='white',width=12)
lbl1=Label(frame,text="Email password",bg="#3895D3", fg='white',width=12)

#Use entry widget to create a text box for user to enter details
name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show="*")

#Function to display message
def display():
    name=name_entry.get()
    greet="Hey"+name
    message="\nCongratulations for your new account"
    Textbox.insert(END,greet)
    Textbox.insert(END,message)

#Textbox to display message
Textbox=Text(bg="#BEBEBE",fg="black")

#Add button, when pressed message will be displayed
btn=Button(text="Create Account",command=display,b3g="red")

#Arrange all widgets
frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
name_entry.place(x=150,y=20)
lbl2.place(x=20,y=20)
email_entry.place(x=150,y=80)
lbl2.place(x=20,y=20)
pass_entry.place(x=150,y=140)
btn.place(x=130, y=210)
Textbox.place(y=250)

#Start the GUI event loop
root.mainloop()