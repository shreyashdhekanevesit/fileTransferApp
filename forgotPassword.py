from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox
import pymysql

def login_page():
    forgotPassword_window.destroy()
    import login

def change_password():
    if usernameEntry.get()=='' or val.get()=='Select' or answerEntry.get()=='' or newpasswordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required..')

    else:
        try:
            conn = pymysql.connect(host='localhost',user='root',password='MY@06#2024sql')
            myCursor = conn.cursor()
        except:
            messagebox.showerror('Error','Connection is not established ! Try Again..')
            return
        
        query = 'use FileTransferApp'
        myCursor.execute(query)
        query = 'select * from userdata where username = %s and securityQuestion = %s and securityAnswer=%s'
        myCursor.execute(query,(usernameEntry.get(),val.get(),answerEntry.get()))
        row = myCursor.fetchone()

        if row == None:
            messagebox.showerror('Error','No Data Found')
        else:
            query = 'UPDATE userdata SET password = %s WHERE username = %s'
            myCursor.execute(query,(newpasswordEntry.get(),usernameEntry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Login with New Password')
            forgotPassword_window.destroy()
            import login


forgotPassword_window =Tk()

forgotPassword_window.geometry('1100x800+50+10')  #this is needed for place method
forgotPassword_window.resizable(0,0)
forgotPassword_window.title('Forgot Password Page')

bgimg = Image.open('Image/demo.jpg')
resized_bgimg = bgimg.resize((1100,820))
bgImage = ImageTk.PhotoImage(resized_bgimg)
bgLabel = Label(forgotPassword_window,image=bgImage)
bgLabel.grid()

forgotPassword_label = Label(forgotPassword_window,text='FORGOT PASSWORD',bg='#F3F3F3',font=('Microsoft Yhei UI Light',12))
forgotPassword_label.place(x=220,y=104)

frame = Frame(forgotPassword_window,bg='white')
frame.place(x=100,y=200)

usernamelabel = Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#939393')
usernamelabel.grid(row=1,column=0,padx=10,sticky='w',pady=(10,0))

usernameEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',14,'bold'),fg='white',bg='#095376')
usernameEntry.grid(row=2,column=0,padx=10,sticky='w')

securityQuestionlabel = Label(frame,text='Security Question',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#939393')
securityQuestionlabel.grid(row=3,column=0,padx=10,sticky='w',pady=(10,0))

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
securityQuestion.grid(row=4,column=0,padx=10,sticky='w')

answerlabel = Label(frame,text='Answer',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#939393')
answerlabel.grid(row=5,column=0,padx=10,sticky='w',pady=(10,0))

answerEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',14,'bold'),fg='white',bg='#0B5C83')
answerEntry.grid(row=6,column=0,padx=10,sticky='w')

newpasswordlabel = Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#939393')
newpasswordlabel.grid(row=7,column=0,padx=10,sticky='w',pady=(10,0))

newpasswordEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',14,'bold'),fg='white',bg='#095376')
newpasswordEntry.grid(row=8,column=0,padx=10,sticky='w')

changepassword_Button = Button(frame,text='Change Password',font=('Open Sans',18),fg='white',bg='#2D2D2D',activeforeground='#095376',activebackground='#F9F9F9',cursor='hand2',bd=0,width=18,command=change_password)
changepassword_Button.grid(row=13,column=0,pady=(55,0),)

logo_img = Image.open('Image/fly_files.jpg')
resize_logo_img = logo_img.resize((230,120))
logo_on_img = ImageTk.PhotoImage(resize_logo_img)
logo_on_label =  Label(frame,image=logo_on_img)
logo_on_label.grid(row=14,column=0,pady=30)
#btimg = Image.open('filetransferimg.png')
#sizeimg = btimg.resize()
#bottomimg = PhotoImage()

haveAcc = Label(forgotPassword_window,text='Already have an Account ?',font=('Microsoft Yhei UI Light',12),width=24,bg='#E6E6E6')
haveAcc.place(x=680,y=687)

signIn_label = Button(forgotPassword_window,text='Sign In',bd=0,font=('Microsoft Yhei UI Light',13),fg='#095376',bg='#E6E6E6',width=7,activebackground='#E6E6E6',command=login_page)
signIn_label.place(x=760,y=710)

forgotPassword_window.mainloop()