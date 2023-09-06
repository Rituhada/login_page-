from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#def onclick():

def forget_password():
    def change_password():
        if user_entry.get() == '' or newpass_entry.get() == '' or confirmpass_entry.get() == '':
            messagebox.showerror('Error', 'All fields required',parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
                messagebox.showerror('Error', 'Password and confirm password not matching ', parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='Ritu@22*', database='userdata')
            mycursor = con.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row ==None:
                messagebox.showerror('Error', 'Incorrect username', parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, Please login with new password',parent=window)
                window.destroy()
    window=Toplevel()
    window.title('Change password')

    bgpic=ImageTk.PhotoImage(file='background.jpg')
    bglabel=Label(window,image=bgpic)
    bglabel.grid()

    heading_label=Label(window,text='RESET PASSWORD', font='arial 18 bold',
                        fg='firebrick',bg='white')
    heading_label.place(x=470,y=60)

    userLabel=Label(window,text='Username',font='arial 12 bold',bg='white',fg='firebrick')
    userLabel.place(x=470,y=130)
    user_entry=Entry(window,width=25,fg='firebrick' , font='arial 12 bold', bd=0)
    user_entry.place(x=470,y=160)
    Frame(window,width=250,height=2,bg='firebrick').place(x=470,y=180)

    newpasswordLabel = Label(window, text='New password', font='arial 12 bold', bg='white', fg='firebrick')
    newpasswordLabel.place(x=470, y=200)
    newpass_entry = Entry(window, width=25, fg='firebrick', font='arial 12 bold', bd=0)
    newpass_entry.place(x=470, y=230)
    Frame(window, width=250, height=2, bg='firebrick').place(x=470, y=260)

    confirmpassLabel = Label(window, text='Confirm password', font='arial 12 bold', bg='white', fg='firebrick')
    confirmpassLabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=25, fg='firebrick', font='arial 12 bold', bd=0)
    confirmpass_entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='firebrick').place(x=470, y=340)

    submitButton = Button(window, text='Submit', font='arial 16 bold',
                          fg='white', bg='firebrick1', activebackground='firebrick1',
                          activeforeground='white', cursor='hand2', bd=0, width=19, command=change_password)
    submitButton.place(x=470,y=390)
    window.mainloop()
def login_user():
    if usernameEntry.get()== '' or passwordEntry.get()=='':
        messagebox.showerror( 'Error','All fields required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Ritu@22*')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection not established ')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('error','Invalid username or password')
        else:
            messagebox.showinfo('success','Login successful')
def signup_page():
    login_window.destroy()
    import signup
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
     openeye.config(file='closeye.png')
     passwordEntry.config(show='*')
     eyeButton.config(command=show)
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

#gui
login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.title("Login")
login_window.resizable(False,False)

bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font="arial 23 bold",
              bg='white',fg='firebrick1')
heading.place(x=605,y=120)
usernameEntry=Entry(login_window,width=25,
                    font="arial 11 bold",bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)


passwordEntry=Entry(login_window,width=25,
                    font="arial 11 bold",bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',
                 activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=250)

forgetButton=Button(login_window,text='Forget Password?',bd=0,bg='white',
                  font='arial 11 bold',fg='firebrick1',cursor='hand2',command=forget_password)
forgetButton.place(x=700,y=290)

loginButton=Button(login_window,text='Login',font='arial 16 bold',
                   fg='white',bg='firebrick1',activebackground='firebrick1',
                   activeforeground='white',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=570,y=350)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
gLabel=Label(login_window,image=google_logo,bg='white')
gLabel.place(x=700,y=440)

twitter_logo=PhotoImage(file='twitter.png')
tLabel=Label(login_window,image=twitter_logo)
tLabel.place(x=760,y=440)

signupLabel=Label(login_window,text='Create new account?', font='arial 9 bold',
                  fg='firebrick1',bg='white')
signupLabel.place(x=590,y=500)

newAccountButton=Button(login_window,text='Create new one',font='arial 9 bold underline',
                   fg='blue',bg='white',activebackground='white',
                   activeforeground='blue',cursor='hand2',bd=0,command=signup_page)
newAccountButton.place(x=727,y=500)

login_window.mainloop()
