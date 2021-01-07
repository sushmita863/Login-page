from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
from tkinter.font import Font

def done():

    uname=ename.get()
    u_email=email.get()
    u_roll=eroll.get()
    u_mobno=emob.get()
    password=epass.get()
    conpass=econpass.get()



    if(uname=="" or password=="" or conpass=="" or u_email=="" or u_roll=="" or u_mobno==""):
        messagebox.showinfo("Blank field not allowed")


    elif(password=="" and conpass==""):
        messagebox.showinfo("Specify password")

    elif(password=="-"):
        messagebox.showinfo('-',"is not allowed")
        messagebox.showinfo("Make a strong passwrd")

    elif (password == conpass):
        saved()
        print("Register Successfully")

    else:
        messagebox.showinfo('invalid username and password')




def registration():
    top=Toplevel()
    top.geometry('500x400')
    top.title("Registration")
    label = Label(top, text="Registration Page", font=('arial', 20, 'bold'), bg='black', fg='White')
    label.pack(side=TOP, fill=X)
    label = Label(top, text=" ", font=('arial', 10, 'bold'), bg='black', fg='White')
    label.pack(side=BOTTOM, fill=X)





    global ename
    global email
    global eroll
    global emob
    global epass
    global econpass

    Label(top, text='Full-name', font=('arial',10,'bold')).place(x=10, y=50)
    Label(top, text='Email', font=('arial',10,'bold')).place(x=10, y=90)
    Label(top, text='Roll-no', font=('arial',10,'bold')).place(x=10, y=130)
    Label(top, text='Mobile', font=('arial',10,'bold')).place(x=10, y=170)
    Label(top, text='password', font=('arial',10,'bold')).place(x=10, y=210)
    Label(top, text='confirm password', font=('arial',10,'bold')).place(x=10, y=250)

    ename = Entry(top)
    ename.place(x=130, y=50)

    email = Entry(top)
    email.place(x=130, y=90)

    eroll = Entry(top)
    eroll.place(x=130, y=130)


    emob = Entry(top)
    emob.place(x=130, y=170)

    epass = Entry(top)
    epass.place(x=130, y=210)
    epass.config(show='*')

    econpass = Entry(top)
    econpass.place(x=130, y=250)
    econpass.config(show='*')

    def create():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS users( id integer primary key autoincrement, ename TEXT, email Text, eroll integer , emob  integer, epass TEXT, econpass TEXT, sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
        conn.commit()
        conn.close()
    create()

    def savedata():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO users(ename, email, eroll, emob, epass, econpass) VALUES (?,?,?,?,?,?)',ename.get(), email.get(), eroll.get(), emob.get(), epass.get(), econpass.get())
        conn.commit()
        print('saved')

    Button(top, text='Register', fg='blue', bg='skyblue', command=done, height=2, width=10 ).place(x=10, y=280)

    bback=Button(top, text="back", command=top.destroy)
    bback.place(x=25, y=340)



    top.mainloop()


def OK():
    uname=e1.get()
    password=e2.get()

    if(uname == "" and password==""):
        messagebox.showinfo("Blank not allowed")

    elif(uname=="Admin" and password=="123"):
        print('login successful')
        root.destroy()

    else:
        messagebox.showinfo(" ","incorrect username or password")

root=Tk()
root.title('Login page')
root.geometry('500x400')


my_font=Font(family="Times New Roman", size=25, weight="bold", slant="italic", underline=1)
label=Label(root, text="JK College Ghansoli",fg="black", font=my_font)
label.place(x=120, y=60)


global e1
global e2

label=Label(root, text="Login page", font=('arial',20,'bold'), bg='black', fg='White')
label.pack(side=TOP, fill=X)
label=Label(root, text=" ", font=('arial',10,'bold'), bg='black', fg='White')
label.pack(side=BOTTOM, fill=X)

Label(root, text="username",font=('arial',15,'bold')).place(x=10, y=140)
Label(root, text="password",font=('arial',15,'bold')).place(x=10, y=180)

e1=ttk.Entry(root)
e1.place(x=140,y=140)

e2=ttk.Entry(root)
e2.place(x=140, y=180)
e2.config(show='*')


b1=Button(root, text="login", bg="skyblue", fg="blue", command=OK, height=2, width=13)
b1.place(x=10, y=220)

lreg=Label(root, text="If not having an account",)
lreg.place(x=10, y=330)
breg=Button(root, text="registar", bg="skyblue", command=registration, height=0, width=13)
breg.place(x=150, y=325)
root.mainloop()
