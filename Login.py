from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector


def saveData():
    if (usernameEntry.get() == '' or emailEntry.grt() == '' or passwordEntry.get() == ''):
        messagebox.showerror("All fields are mandotary")
    else:
        try:
             conn = mysql.connector.connect(
             host="localhost",
             user="root",
             password="Neeru705",
             database="customerdata"
             )
             mycursor = conn.cursor()
             sql = 'insert into studentreg(username,email,password)values(%s,%s,%s)'
             mycursor.execute(sql, (usernameEntry.get(), emailEntry.get(), passwordEntry.get()))
             mycursor.execute(query, data)
             conn.commit()
             messagebox.showinfo("Success", "Data saved successfully!")

        except:
            messagebox.showinfo('Error',"Data saved successfully")

window = Tk()
background = ImageTk.PhotoImage(file='apjkalam.jpg')
blabel = Label(window, image=background)
blabel.grid()
frame = Frame(window)
frame.place(x=900, y=100)

usernameLabel = Label(frame, text="username", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
usernameLabel.grid(row=0, column=0)

usernameEntry = Entry(frame, width=30)
usernameEntry.grid(row=0, column=1)

emailLabel = Label(frame, text="email", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
emailLabel.grid(row=1, column=0)
emailEntry = Entry(frame, width=30)
emailEntry.grid(row=1, column=1)

passwordLabel = Label(frame, text="password", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
passwordLabel.grid(row=2, column=0, padx=10, pady=5)
passwordEntry = Entry(frame, width=30)
passwordEntry.grid(row=2, column=1)
submit_button = Button(window, text="Save", command=saveData)
submit_button.grid(row=4,column=1)



window.mainloop()