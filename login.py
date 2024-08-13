from tkinter import *   
from PIL import ImageTk, Image  #python image library  #imagetk class will help us in adding jpg image on our window
from tkinter import messagebox
import pymysql  #this is the python connector for mysql helps for establishing connection fot mysql database

#functionality part
def signUp_page():
    login_window.destroy()
    import signup

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required..')
    else:
        try:
            conn = pymysql.connect(host='localhost',user='root',password='tejas21')
            myCursor = conn.cursor()
        except:
            messagebox.showerror('Error','Connection is not established ! Try Again..')
            return   #if exception accurs code below this in the function will not execute
        
        query = 'use FileTransferApp'
        myCursor.execute(query)
        query = 'select * from userdata where username = %s and password = %s'
        myCursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row = myCursor.fetchone()
        
        if row == None:
            messagebox.showerror('Error','Invalid Username or Password')
        else:
            messagebox.showinfo('Welcome','Login is Successful..')
            login_window.destroy()
            import homePage
        
def forgot():
    login_window.destroy()
    import forgotPassword


def hide():
    #open_eye_img.config(file="eye_button_close.png")
    # Replace 'eye_button_close.png' with the path to your closed eye image
    img = Image.open('Image/eye_button_close.png')
    resized_img = img.resize((27, 27))
    closed_eye_img = ImageTk.PhotoImage(resized_img)
    eyeButton.config(image=closed_eye_img)
    eyeButton.image = closed_eye_img

    #for doing password in ***
    passwordEntry.config(show='*')

    eyeButton.config(command=show)

def show():
    img = Image.open('Image/eye_button_open.png')
    resized_img = img.resize((27, 27))
    opened_eye_img = ImageTk.PhotoImage(resized_img)
    eyeButton.config(image=opened_eye_img)
    eyeButton.image = opened_eye_img

    passwordEntry.config(show='')

    eyeButton.config(command=hide)
 

def on_user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def on_password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


#gui part

login_window =Tk()

login_window.geometry('1100x820+200+10')  #this is needed for place method
login_window.resizable(0,0)
login_window.title('Login Page')

bgimg = Image.open('Image/demo.jpg')
resized_bgimg = bgimg.resize((1100,820))
bgImage = ImageTk.PhotoImage(resized_bgimg)
bgLabel = Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)
#bgLabel.grid(row=0,column=0)
#bgLabel.pack()   #use this#when u want to place at particular position then u use place instead of grid and pack its better to use place

#final1 = 
#final1.rectangle((100,200,200,100), fill="white")
usernameLabel = Label(login_window,text='/Username',fg='#939393',bg='white',font=('Microsoft Yhei UI Light',12))
usernameLabel.place(x=232,y=216)

usernameEntry = Entry(login_window,font=('Microsoft Yhei UI Light',14),bd=0,fg='#095376')
usernameEntry.place(x=165,y=251,width=300,height=50)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',on_user_enter)

Frame(login_window,width=270,height=1,bg='#095376').place(x=165,y=290)

passwordEntry = Entry(login_window,font=('Microsoft Yhei UI Light',14),bd=0,fg='#095376')
passwordEntry.place(x=165,y=367,width=300,height=50)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',on_password_enter)

Frame(login_window,width=270,height=1,bg='#095376').place(x=165,y=406)
#00E9C4

# Read the Image
image_eye = Image.open("Image/eye_button_open.png")
resize_image = image_eye.resize((27, 27))
open_eye_img = ImageTk.PhotoImage(resize_image)
eyeButton = Button(login_window,image=open_eye_img,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=440,y=374)

forgetButton = Button(login_window,text='Forgot Passward ?',bd=0,fg='#095376',bg='#FBFBFB',activebackground='white',cursor='hand2',font=('Microsoft Yhei UI Light',13,'underline'),width=18,activeforeground='#095376',command=forgot)
forgetButton.place(x=322,y=440)

login_Button = Button(login_window,text='Login',font=('Open Sans',22),fg='white',bg='#2D2D2D',activeforeground='#095376',activebackground='#2D2D2D',cursor='hand2',bd=0,width=20,command=login_user)
login_Button.place(x=129,y=500)
#2D2D2D

logo_img = Image.open('Image/fly_files.jpg')
resize_logo_img = logo_img.resize((230,120))
logo_on_img = ImageTk.PhotoImage(resize_logo_img)
logo_on_label =  Label(login_window,image=logo_on_img)
logo_on_label.place(x=180,y=600)


#signUp_Button = Button(login_Button,text='Sign Up',bg='#ffffff',width=100,bd=0)
#signUp_Button.place(x=250,y=700)

signUp_Button = Button(login_window,text='Sign Up',font=('Open Sans',13),fg='#095376',bg='#EDEDED',activeforeground='#095376',activebackground='#F9F9F9',cursor='hand2',width=10,bd=0,command=signUp_page)
signUp_Button.place(x=734,y=705)






login_window.mainloop()
