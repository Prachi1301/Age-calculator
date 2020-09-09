import tkinter as tk
import datetime
from PIL import Image,ImageTk
window=tk.Tk()
window.geometry("800x900")
window.title("Age Calculator App")
window.configure(bg="pink")
name=tk.Label(text="Name",font=("arial",16,"bold"),relief='solid')
name.place(x=100,y=430)
month=tk.Label(text="Month",font=("arial",16,"bold"),relief='solid')
month.place(x=100,y=470)
year=tk.Label(text="Year",font=("arial",16,"bold"),relief='solid')
year.place(x=100,y=510)
date=tk.Label(text="Date",font=("arial",16,"bold"),relief='solid')
date.place(x=100,y=550)
nameEntry=tk.Entry()
nameEntry.place(x=180,y=430)
monthEntry=tk.Entry()
monthEntry.place(x=180,y=470)
yearEntry=tk.Entry()
yearEntry.place(x=180,y=510)
dateEntry=tk.Entry()
dateEntry.place(x=180,y=550)
def getInput():
    name=nameEntry.get()
    person=Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    textarea=tk.Text(master=window,height=10,width=40,bg='light blue',fg='blue',font=("arial",15,"bold"))
    textarea.place(x=120,y=640)
    answer="Heyy {person}!!! You are {age} years old!!!".format(person=name, age=person.age())
    textarea.insert(tk.END,answer)
button=tk.Button(window,text="Calculate Age",command=getInput,bg='brown',activebackground="yellow",fg='white')
button.place(x=150,y=600)
Image=Image.open('age1.jpg')
photo=ImageTk.PhotoImage(Image)
Label_image=tk.Label(image=photo)
Label_image.place(x=60,y=100)

class Person:
    def __init__(self,name,birthdate):
        self.name=name
        self.birthdate=birthdate
    def age(self):
        today=datetime.date.today()
        age=today.year-self.birthdate.year
        return age
window.mainloop()