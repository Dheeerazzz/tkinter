# main.py

from tkinter import *
from tkcalendar import Calendar
import pandas as pd
from PIL import ImageTk, Image


data = [] 

def saveinfo():
    valor1 = e1.get()
    valor2 = e2.get()
    valor3 = e3.get()
    valor4 = e4.get()
    valor5 = e5.get()
    valor6 = e6.get()
    valor7 = e7.get()
    entry = {'Customer Name': valor1, 'Name of the Project': valor2, 'Email': valor3, 'Phone No.': valor4,
             'College Name': valor5, 'Project Description': valor6, 'Cost': valor7}

    data.append(entry)
    print(data)

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    
    
def export():
    df = pd.DataFrame(data)

    try:
        existing_df = pd.read_csv('output.csv')
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        updated_df.to_csv('output.csv', index=False)
        print("Data exported successfully!")
    except FileNotFoundError:
        df.to_csv('output.csv', index=False)
        print("Data exported successfully!")






top = Tk()

top.geometry("500x700")
top.title("Enquiry Form")

head = Label(top, text="Robocoupler Enquiry Form",font="bold")
head.place(x=120, y=100)
img=Image.open("robocouplerlogo.png")
resized=img.resize((500,100),Image.LANCZOS )
img = ImageTk.PhotoImage(resized)
label = Label(top, image = img,width=500,height=100)
label.pack()


cname = Label(top, text="Customer Name")
cname.place(x=10, y=140)
e1 = Entry(top)
e1.place(x=150, y=140)

pname = Label(top, text="Name of the Project ")
pname.place(x=10, y=170)
e2 = Entry(top)
e2.place(x=150, y=170)

email = Label(top, text="Email")
email.place(x=10, y=200)
e3 = Entry(top)
e3.place(x=150, y=200)

phno = Label(top, text="Phone No.")
phno.place(x=10, y=230)
e4 = Entry(top)
e4.place(x=150, y=230)

clg = Label(top, text="College Name")
clg.place(x=10, y=260)
e5 = Entry(top)
e5.place(x=150, y=260)

desc = Label(top, text="Project Description")
desc.place(x=10, y=290)
e6 = Entry(top)
e6.place(x=150, y=290)

cost = Label(top, text="Cost")
cost.place(x=10, y=320)
e7 = Entry(top)
e7.place(x=150, y=320)

submit = Button(top, text="Submit", command=saveinfo)
submit.place(x=170, y=350)

export = Button(top, text="Export", command=export)
export.place(x=170, y=380)

top.mainloop()
