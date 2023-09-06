from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)
def connect_database():
    if emailEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All fields required')
    # print("Table 'users' created successfully!")
    elif passwordEntry.get()!=confirmEntry.get():
        messagebox.showerror('Error', 'Password not matched')
    elif check.get()==0:
        messagebox.showerror('Error', 'Password not matched ')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Ritu@22*')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'No required')
            return
        try:
            query='Create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='CREATE TABLE  data (id int auto_increment primary key not null,email varchar (50),username varchar(255), password varchar(255))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query='select *  from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('error', 'name exits')
        query='insert into data(email,username,password) values(%s,%s,%s)'
        mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))

        con.commit()
        con.close()
        messagebox.showinfo('success','Registration Succesful')
        clear()
        signup_window.destroy()
        import signin

def login_page():
    signup_window.destroy()
    import signin
signup_window = Tk()
signup_window.title('signup page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='Create An Account ',font="arial 20",
               bg='white', fg='firebrick1')

heading.grid(row=0,column=0,padx=10,pady=10)
emailLabel=Label(frame,text='Email',font='arial 10 bold',bg='white',
                 fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry=Entry(frame, width=25,font='arial 10 bold')
emailEntry.grid(row=2, column=0,  sticky='w', padx=25)

usernameLabel=Label(frame,text='Username',font='arial 10 bold',bg='white',
                 fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=25,font='arial 10 bold')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font='arial 10 bold',bg='white',
                 fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=25,font='arial 10 bold')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm password',font='arial 10 bold',bg='white',
                 fg='firebrick1')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
confirmEntry=Entry(frame,width=25,font='arial 10 bold')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termscondition=Checkbutton(frame,text="I agree to terms & conditions", font="arial 10 bold",
                           fg='firebrick1',bg='white', activebackground='white',
                           activeforeground='firebrick1',cursor='hand2',variable=check)
termscondition.grid(row=9,column=0, pady=10,padx=15)

signupButton=Button(frame,text='signup',font='arial 16 bold',
                   fg='white',bg='firebrick1',activebackground='firebrick1',
                   activeforeground='white',cursor='hand2',bd=0,width=19, command=connect_database)
signupButton.grid(row=10,column=0,pady=10)
signup_window.mainloop()