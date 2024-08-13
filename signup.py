from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk, Image
import pymysql

def login_page():
    signUp_window.destroy()
    import login

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmPasswordEntry.delete(0,END)
    val.set('Select')
    answerEntry.delete(0,END)
    check.set(0)


def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmPasswordEntry.get()=='' or      val=='Select' or answerEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    
    elif passwordEntry.get() != confirmPasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    
    elif check.get() == 0:
        messagebox.showerror('Error','Plesae accept Terms and Conditions')
    
    else:
        try:
            conn = pymysql.connect(host='localhost',user='root',password='tejas21')  #conn use for connection and commiting the changes
            myCursor = conn.cursor()    #this will help us in executing our commands
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return

    try:
        query = 'create database FileTransferApp'    #if the database is not already created then only this code will execute
        myCursor.execute(query)
        query= 'use FileTransferApp'
        myCursor.execute(query)
        query = 'create table userdata(id int auto_increment primary key not null , email varchar(50), username varchar(100),password varchar(20), securityQuestion varchar(100), securityAnswer varchar(100))'
        myCursor.execute(query)
    except: 
        #when the database is already created this code will execute
        myCursor.execute('use FileTransferApp')

    query='select * from userdata where username=%s' #%S will get replace with that field value in execute function
    myCursor.execute(query,(usernameEntry.get()))  
    
    row = myCursor.fetchone()
    if row != None:
        messagebox.showerror('Error','Username already exist..')
    else:
        #if no same username in database then this will execute
        query = 'insert into userdata(email,username,password,securityQuestion,securityAnswer) values(%s,%s,%s,%s,%s)'
        myCursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get(),val.get(),answerEntry.get())) 
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Registration is Successful')
        clear()   #for clearing all the inputs in the entry field
        signUp_window.destroy()
        import login

    #print('connected')

signUp_window =Tk()

signUp_window.geometry('1100x800+200+10')  #this is needed for place method
signUp_window.resizable(0,0)
signUp_window.title('Sign Up Page')

bgimg = Image.open('Image/demo.jpg')
resized_bgimg = bgimg.resize((1100,820))
bgImage = ImageTk.PhotoImage(resized_bgimg)
bgLabel = Label(signUp_window,image=bgImage)
bgLabel.grid()

signUp_label = Label(signUp_window,text='SIGN UP',bg='#F3F3F3',font=('Microsoft Yhei UI Light',18))
signUp_label.place(x=254,y=100)

whitelabel = Label(signUp_window,text='',bg='white',width=60,height=35)
whitelabel.place(x=110,y=200)

frame = Frame(signUp_window,bg='white')
frame.place(x=100,y=200)

emaillabel = Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#939393')
emaillabel.grid(row=0,column=0,padx=10,sticky='w',pady=(10,0))

emailEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',14,'bold'),fg='white',bg='#095376')
emailEntry.grid(row=1,column=0,padx=10,sticky='w')

usernamelabel = Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#939393')
usernamelabel.grid(row=2,column=0,padx=10,sticky='w',pady=(10,0))

usernameEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',14,'bold'),fg='white',bg='#095376')
usernameEntry.grid(row=3,column=0,padx=10,sticky='w')

passwordlabel = Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#939393')
passwordlabel.grid(row=4,column=0,padx=10,sticky='w',pady=(10,0))

passwordEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',14,'bold'),fg='white',bg='#095376')
passwordEntry.grid(row=5,column=0,padx=10,sticky='w')

confirmPasswordlabel = Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#939393')
confirmPasswordlabel.grid(row=6,column=0,padx=10,sticky='w',pady=(10,0))

confirmPasswordEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',14,'bold'),fg='white',bg='#0B5C83')
confirmPasswordEntry.grid(row=7,column=0,padx=10,sticky='w')

securityQuestionlabel = Label(frame,text='Security Question',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#939393')
securityQuestionlabel.grid(row=8,column=0,padx=10,sticky='w',pady=(10,0))

options = [
"Select",
"What is your pet name ?",
"Your grandfather Name",
"Your birthplace",
"your favourite movie"
]
val = StringVar()
val.set(options[0])
securityQuestion = OptionMenu(frame,val,*options)
securityQuestion.config(width=32,bg='#0B5C83',fg='white',font=('Microsoft Yahei UI Light',12,'bold'),bd=0)
securityQuestion.grid(row=9,column=0,padx=10,sticky='w')

answerlabel = Label(frame,text='Answer',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#939393')
answerlabel.grid(row=10,column=0,padx=10,sticky='w',pady=(10,0))

answerEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',14,'bold'),fg='white',bg='#0B5C83')
answerEntry.grid(row=11,column=0,padx=10,sticky='w')

check = IntVar()


termsandConditions = Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',10,'bold','underline'),fg='#0B5C83',bg='white',activebackground='white',activeforeground='#0B5C83',cursor='hand2',variable=check)
termsandConditions.grid(row=12,column=0,padx=10,sticky='w',pady=(8,0))

signUp_Button = Button(frame,text='Sign Up',font=('Open Sans',18),fg='white',bg='#2D2D2D',activeforeground='#095376',activebackground='#F9F9F9',cursor='hand2',bd=0,width=18,command=connect_database)
signUp_Button.grid(row=13,column=0,pady=(25,0))

haveAcc = Label(signUp_window,text='Already have an Account ?',font=('Microsoft Yhei UI Light',12),width=24,bg='#E6E6E6')
haveAcc.place(x=680,y=687)

signIn_label = Button(signUp_window,text='Sign In',bd=0,font=('Microsoft Yhei UI Light',13),fg='#095376',bg='#E6E6E6',width=7,activebackground='#E6E6E6',command=login_page)
signIn_label.place(x=760,y=710)

signUp_window.mainloop()