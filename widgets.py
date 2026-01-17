#Import necessary libraries
from tkinter import *
from datetime import date

#Create window
root=Tk()
#Set the window Title and Geometry
root.title('Getting started with widgets')
root.geometry('400x300')

#Add widgets
#Add Label
lbl=Label(text="Hey there!", fg="white", bg="#072F5F",height=1, width=300)

#Add label for getting name as input from user
#Use Entry Widget to create a text ox for user to enter details
name_lbl=Label(text="Full name", bg="#3895D3")
name_entry=Entry()

#Function to display a Message
def display():
    #Read input given by user
    name =name.entry.get()
    #Declaring a global variable
    #to make it accesible anywhere in the program
    global message 
    message="welcome to the application!\nToday's date is:"
    great="hello"+name+"\n"
    #Display details in a text box
    #Specify where to add the details inside the text box
    text_box.inset(END,great)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
#Add text widget to display information/messages
text_box=Text(height=3)
