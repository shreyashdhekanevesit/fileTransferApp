import tkinter as tk
from tkinter import PhotoImage
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import ImageTk, Image
from tkinter import filedialog
import zlib
import pymysql
from tkinter import END

about_us_frame = None
contact_us_frame = None
help_frame = None
feedback_frame = None
report_frame = None
send_frame = None
receive_frame = None


def show_send_page():
    global send_frame
    send_frame = tk.Frame(content_frame, width=900, height=820)
    send_frame.pack(side='right', fill='both', expand=True)
#d5e2f3
    upper_frame = tk.Frame(send_frame, bg='#FBFBFB')
    upper_frame.place(relx=0, rely=0, relwidth=1, relheight=0.3)

    lower_frame = tk.Frame(send_frame, bg='#095376')#f4fdfe#095376
    lower_frame.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)


    def send():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetype=(('File_Type','*.txt'),('All Files','*.*')))

        if filename:
            messagebox.showinfo("File Selected", f"Selected File: {filename}")
        
    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print("Waiting for any incoming connections....")
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully")
        file.close()
        s.close()
        messagebox.showinfo("File Sent", "File has been sent successfully!")


    select_file_button = tk.Button(lower_frame, text="+ Select File", width=10, height=1, font='arial 14 bold', bg='#059bad', fg='#000', bd=0, relief=tk.RAISED, highlightthickness=2, padx=10, pady=5,command=send)
    select_file_button.place(x=350, y=20)
    
    send_button = tk.Button(lower_frame, text="SEND", width=8, height=1, font='arial 14 bold', bg='#059bad', fg='#000', bd=0, relief=tk.RAISED, highlightthickness=2, padx=10, pady=5,command=sender)
    send_button.place(x=360, y=380)

    tk.Label(lower_frame,image=image3,bg='#095376').place(x=300,y=100)

    host=socket.gethostname()
    tk.Label(lower_frame,text=f'ID:{host}',bg='white',fg='black').place(x=350,y=130)

    profile = tk.Button(upper_frame, image=image, bg="#FBFBFB", bd=0,)
    profile.place(x=5, y=-20)

    tk.Label(upper_frame,image=image4,bd=0,bg='#FBFBFB').place(x=245,y=40)

    logout_button = tk.Button(send_frame, image=image6,bg="#FBFBFB", bd=0, command=logout_function)
    logout_button.place(x=1020, y=5)  


def show_receive_page():
    global receive_frame
    receive_frame = tk.Frame(content_frame, width=850, height=800, bg='#FBFBFB')
    #receive_frame.place(x=200,y=100)
    receive_frame.pack(side='right', fill='both', expand=True)  

    def receiver():
        id=SenderID.get()
        filename1 = incoming_filename.get()

        s = socket.socket()
        port = 8080
        s.connect((id,port))
        file = open(filename1,'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        messagebox.showinfo("File Recieve","File has been received successfully....")


    inner_frame = tk.Frame(receive_frame,width=780,height=650,bg='#095376')
    inner_frame.place(x=30,y=20)

    #receive_label = tk.Label(receive_frame, text="Receive Page")
    #receive_label.pack()

    # img = Image.open('Image/receiver.png')
    # resized_img = img.resize((760,200))
    # Hbackground = ImageTk.PhotoImage(resized_img)
    bgimage = tk.Label(inner_frame,image=Hbackground)
    bgimage.place(x=8,y=5)
    
    tk.Label(inner_frame,text='Receive',font=('arial',10,'bold'),bg='#095376',fg='white').place(x=350,y=260)

    #logo = PhotoImage(file='Image/profile.png')
    logoLabel = tk.Label(inner_frame,image=profile_r,bg='#f4fdfe')
    logoLabel.place(x=335,y=280)

    tk.Label(inner_frame,text="Input Sender ID : ",font=('arial',10,'bold'),bg='#095376').place(x=250,y=380)
    SenderID = tk.Entry(inner_frame,width=25,fg='black',font=('arial',15))
    SenderID.place(x=250,y=410)
    SenderID.focus()

    tk.Label(inner_frame,text="Filename for the incoming file : ",font=('arial',10,'bold'),bg='#095376').place(x=250,y=460)
    incoming_filename = tk.Entry(inner_frame,width=25,fg='black',font=('arial',15))
    incoming_filename.place(x=250,y=490)

    # image_icon=tk.PhotoImage(file='Image/arrow.png')
    rr=tk.Button(inner_frame,text="Receive",compound=tk.LEFT,image=image_icon,width=100,bg='#39c790',font=('arial', 14 ,'bold'),command=receiver)
    rr.place(x=330,y=550)

    #compound=tk.LEFT
    
def about_us():
    global about_us_frame, contact_us_frame, help_frame, feedback_frame, report_frame
    if about_us_frame is not None:
        about_us_frame.destroy()
    if contact_us_frame is not None:
        contact_us_frame.pack_forget()
    if help_frame is not None:
        help_frame.pack_forget()
    if feedback_frame is not None:
        feedback_frame.pack_forget()
    if report_frame is not None:
        report_frame.pack_forget()

    about_us_frame = tk.Frame(content_frame, width=900, height=820, bg='#d5e2f3')
    about_us_frame.pack(side='right', fill='both', expand=True)
    #about_us_label = tk.Label(about_us_frame, text="About Us Page")
    #about_us_label.pack()

    description_text = """
    
                                                                 Welcome to Fly Files!
    
       We are a leading file management application providing comprehensive solutions for all your 
       file transfer, compression, and decompression needs. Our mission is to simplify the way you 
       manage your files, making it faster, easier, and more efficient.
    
       Key Features:
       - File Transfer: Seamlessly transfer files between devices with lightning-fast speed, whether it's 
       across the room or across the globe.
       - File Compression: Reduce file sizes without compromising on quality, saving valuable storage 
       space and bandwidth, while ensuring swift uploads and downloads.
       - File Decompression: Extract files effortlessly, allowing you to access and utilize archived 
       content with ease, whether it's a single file or an entire archive.
    
       With Fly Files, you can take control of your digital assets like never before. Our intuitive 
       user interface and robust functionality empower you to organize, share, and manage your files 
       effortlessly.
    
       Whether you're a professional seeking to streamline your workflow or an individual looking for a 
       hassle-free file management solution, Fly Files is your ultimate companion.
    
       Join the Fly Files community today and experience the future of file management!
    
       For any inquiries or feedback, please contact us at support@flyfiles.com.
    
       Thank you for choosing Fly Files!"""
    
    description_label = tk.Label(about_us_frame, text=description_text, font=("Helvetica", 14), justify='left', bg='#d5e2f3', wraplength=880)
    description_label.pack(pady=20, padx=20, fill='both')

# Footer
    footer_label = tk.Label(about_us_frame, text="© 2024 Fly Files. All Rights Reserved.", font=("Helvetica", 10), bg='#d5e2f3')
    footer_label.pack(side='bottom', pady=10, fill='x')

def contact_us():
    global contact_us_frame, about_us_frame, help_frame, feedback_frame, report_frame
    if contact_us_frame is not None:
        contact_us_frame.destroy()
    if about_us_frame is not None:
        about_us_frame.pack_forget()
    if help_frame is not None:
        help_frame.pack_forget()
    if feedback_frame is not None:
        feedback_frame.pack_forget()
    if report_frame is not None:
        report_frame.pack_forget()

    contact_us_frame = tk.Frame(content_frame, width=900, height=820, bg='#d5e2f3')
    contact_us_frame.pack(side='right', fill='both', expand=True)


    #tk.Label(contact_us_frame,image=image7).place(x=5,y=100)

    contact_info_text = """
    Contact Information:
    
    We would love to hear from you! Feel free to reach out to us for any queries, feedback, or 
    support.
    
    Email: support@flyfiles.com
    Phone: +1-800-123-4567
    Address: 23/200 Bandra(W)
    
    Our support team is available 24/7 to assist you with any issues or concerns you may have. 
    Your satisfaction is our top priority.
    """

    contact_info_label = tk.Label(contact_us_frame, text=contact_info_text, font=("Helvetica", 14), justify='left', bg='#d5e2f3', wraplength=880)
    contact_info_label.pack(pady=20, padx=20, fill='both')

    # Footer
    footer_label = tk.Label(contact_us_frame, text="© 2024 Fly Files. All Rights Reserved.", font=("Helvetica", 10), bg='#d5e2f3')
    footer_label.pack(side='bottom', pady=10, fill='x')

def Feedback():
    global feedback_frame, about_us_frame, contact_us_frame, help_frame, report_frame
    if feedback_frame is not None:
        feedback_frame.destroy()
    if about_us_frame is not None:
        about_us_frame.pack_forget()
    if contact_us_frame is not None:
        contact_us_frame.pack_forget()
    if help_frame is not None:
        help_frame.pack_forget()
    if report_frame is not None:
        report_frame.pack_forget()
    
    def clear():
        entry_name.delete(0,END)
        entry_email.delete(0,END)
        text_message.delete('1.0',END)
        var1.set(None)

    def submit_form():
        name = entry_name.get()
        email = entry_email.get()
        message = text_message.get("1.0", "end-1c")
        feedback = var1.get()

        if name.strip() == "" or email.strip() == "" or message.strip() == "" or feedback ==  "":
            messagebox.showwarning("Error", "Please fill in all fields.")
        else:
            try:
                conn = pymysql.connect(host='localhost',user='root',password='tejas21')  
                myCursor = conn.cursor()   
            except:
                messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
                return
                    
        try:
                query = 'create database FileTransferApp'   
                myCursor.execute(query)
                query= 'use FileTransferApp'
                myCursor.execute(query)
                query = 'create table feedback(id int auto_increment primary key not null , name varchar(100), email varchar(50), feedback varchar(20) , message varchar(500))'
                myCursor.execute(query)
        except:
                try:
                    myCursor.execute('use FileTransferApp')
                    query = 'create table feedback(id int auto_increment primary key not null , name varchar(100), email varchar(50), feedback varchar(20) , message varchar(500))'
                    myCursor.execute(query)
                    query = 'insert into feedback(name,email,feedback,message) values(%s,%s,%s,%s)'
                    myCursor.execute(query,(name,email,feedback,message))
                    conn.commit()
                    conn.close()
                except:
                    myCursor.execute('use FileTransferApp')
                    query = 'insert into feedback(name,email,feedback,message) values(%s,%s,%s,%s)'
                    myCursor.execute(query,(name,email,feedback,message))
                    conn.commit()
                    conn.close()
  
        messagebox.showinfo("Success", "Form submitted successfully!")
        clear()
             
    def show_selected():
        selected_option = var1.get()
        if selected_option == 1:
            print("Option 1 selected")
        elif selected_option == 2:
            print("Option 2 selected")
        elif selected_option == 3:
            print("Option 3 selected")
        elif selected_option == 4:
            print("Option 4 selected")
        elif selected_option == 5:
            print("Option 5 selected")

    feedback_frame = tk.Frame(content_frame, width=900, height=820, bg='#d5e2f3')
    feedback_frame.pack(side='right', fill='both', expand=True)
    # feedback_label = tk.Label(feedback_frame, text="Feedback Page")
    # feedback_label.pack()
    #bgimage = tk.Label(feedback_frame,image=formBg)
    #bgimage.place(x=8,y=8)

    feedback_label = tk.Label(feedback_frame, text="Feedback Form", font=('arial', 30 ,'bold'),fg= "black",bg='#d5e2f3')
    feedback_label.place(x=270,y=70)

    var1 = tk.IntVar()

    label_question = tk.Label(feedback_frame, text="How do you Rate your overall experience ? ", bg='#d5e2f3', fg='#000',font=('arial', 10 ,'bold'))
    label_question.place(x=160, y=180)

    radio_option1 = tk.Radiobutton(feedback_frame, text="Excellent", variable=var1, value=1, command=show_selected,  fg='#000', bg='#d5e2f3',font=('arial', 10 ,'bold'))
    radio_option1.place(x=160, y=210)

    radio_option2 = tk.Radiobutton(feedback_frame, text="Good", variable=var1, value=2, command=show_selected,  fg='#000', bg='#d5e2f3',font=('arial', 10 ,'bold'))
    radio_option2.place(x=260, y=210)

    radio_option3 = tk.Radiobutton(feedback_frame, text="Average", variable=var1, value=3, command=show_selected,  fg='#000', bg='#d5e2f3',font=('arial', 10 ,'bold'))
    radio_option3.place(x=340, y=210)

    radio_option3 = tk.Radiobutton(feedback_frame, text="Poor", variable=var1, value=4, command=show_selected,  fg='#000', bg='#d5e2f3',font=('arial', 10 ,'bold'))
    radio_option3.place(x=430, y=210)

    radio_option3 = tk.Radiobutton(feedback_frame, text="Very Poor", variable=var1, value=5, command=show_selected,  fg='#000', bg='#d5e2f3',font=('arial', 10 ,'bold'))
    radio_option3.place(x=510, y=210)

    label_name = tk.Label(feedback_frame, text="Name : ", bg='#d5e2f3', fg='#000',font=('arial', 10 ,'bold'))
    label_name.place(x=160, y=260)
    entry_name = tk.Entry(feedback_frame,width=25 ,font=('arial', 14 ))
    entry_name.place(x=160, y=290)

    # Email field
    label_email = tk.Label(feedback_frame, text="Email : ", bg='#d5e2f3', fg='#000',font=('arial', 10 ,'bold'))
    label_email.place(x=160, y=340)
    entry_email = tk.Entry(feedback_frame,width=25 ,font=('arial', 14 ))
    entry_email.place(x=160, y=370)

    # Message field
    label_message = tk.Label(feedback_frame, text="Feedback : ", bg='#d5e2f3', fg='#000' ,font=('arial', 10 ,'bold'))
    label_message.place(x=160, y=420)
    text_message = tk.Text(feedback_frame, height=5, width=50,font=('arial', 10 ))
    text_message.place(x=160, y=450)

    # Submit button
    #submit_button = tk.Button(feedback_frame, text="Submit")
    #submit_button.place(x=160, y=560)

    send_button = tk.Button(feedback_frame, text="Submit", width=8, height=1, font='arial 14 bold', bg='#059bad', fg='#000', bd=0, relief=tk.RAISED, highlightthickness=2, padx=10, pady=5, command=submit_form)
    send_button.place(x=340, y=570)

def help():
    global help_frame, about_us_frame, contact_us_frame, feedback_frame, report_frame
    if help_frame is not None:
        help_frame.destroy()
    if about_us_frame is not None:
        about_us_frame.pack_forget()
    if contact_us_frame is not None:
        contact_us_frame.pack_forget()
    if feedback_frame is not None:
        feedback_frame.pack_forget()
    if report_frame is not None:
        report_frame.pack_forget()

    help_frame = tk.Frame(content_frame, width=900, height=820, bg='#d5e2f3')
    help_frame.pack(side='right', fill='both', expand=True)

    head_text = """
    FREQUENTLY ASKED QUESTIONS
    """
    head_label = tk.Label(help_frame, text=head_text, font=("Helvetica", 18), justify='center', bg='#d5e2f3')
    head_label.pack(pady=5, padx=5, fill='both')

    faq_text = """
    1. File Transfer:

    To transfer files between devices, follow these steps:
    - Click on the "Select File" button to choose the file you want to transfer.
    - Click on the "Send File" button to start the transfer.

    2. File Compression:

    To compress a file, follow these steps:
    - Click on the "Select File" button to choose the file you want to compress.
    - Enter the name for the compressed file.
    - Click on the "Compress File" button to start the compression process.

    3. File Decompression:

    To decompress a file, follow these steps:
    - Click on the "Select File" button to choose the file you want to decompress.
    - Enter the name for the decompressed file.
    - Click on the "Decompress File" button to start the decompression process.

    4. How secure are file transfers in Fly File?

    Fly File ensures secure file transfers through robust encryption protocols. Your files are encrypted during transit to 
    ensure they remain private and secure.

    5. Forgot Password:
    
    If you forgot your password while logging in, follow these steps:
    - Click on the "Forgot Password" option on the login screen.
    - Enter your email address or username associated with your account.
    """
    faq_label = tk.Label(help_frame, text=faq_text, font=("Helvetica", 12), justify='left', bg='#d5e2f3', wraplength=800)
    faq_label.pack(pady=20, padx=20, fill='both', side='left')

entry_name = None
entry_email = None
text_message = None
var1= None

def submit_report():
    global entry_name, entry_email, text_message,var1
    # Get values from the form
    name = entry_name.get()
    email = entry_email.get()
    message = text_message.get("1.0", "end-1c")
    issue_type = var1.get()  # Get the selected issue type

    if name.strip() == "" or email.strip() == "" or message.strip() == "":
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        try:
            conn = pymysql.connect(host='localhost', user='root', password='tejas21', database='FileTransferApp')
            myCursor = conn.cursor()

            # Insert the form data into the database
            query = 'INSERT INTO reports (name, email, issue_type, message) VALUES (%s, %s, %s, %s)'
            myCursor.execute(query, (name, email, issue_type, message))
            conn.commit()

            conn.close()
            clear()  
            messagebox.showinfo("Success", "Report submitted successfully!")

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Database Error: {e}")


def clear():
    entry_name.delete(0, "end")
    entry_email.delete(0, "end")
    text_message.delete("1.0", "end")

def Report():
    global report_frame, about_us_frame, contact_us_frame, help_frame, feedback_frame
    global entry_name, entry_email, text_message,var1
    if report_frame is not None:
        report_frame.destroy()
    if about_us_frame is not None:
        about_us_frame.pack_forget()
    if contact_us_frame is not None:
        contact_us_frame.pack_forget()
    if help_frame is not None:
        help_frame.pack_forget()
    if feedback_frame is not None:
        feedback_frame.pack_forget()

    report_frame = tk.Frame(content_frame, width=900, height=820, bg='#d5e2f3')
    report_frame.pack(side='right', fill='both', expand=True)

    title_label = tk.Label(report_frame, text="Report Us", font=("Helvetica", 18), bg='#d5e2f3')
    title_label.pack(pady=80)

    var1 = tk.IntVar()

    label_question = tk.Label(report_frame, text="Select the type of issue:", bg='#d5e2f3', fg='#000', font=('Arial', 10, 'bold'))
    label_question.place(x=160, y=150)

    radio_option1 = tk.Radiobutton(report_frame, text="Bug", variable=var1, value=1, fg='#000', bg='#d5e2f3', font=('Arial', 10, 'bold'))
    radio_option1.place(x=160, y=180)

    radio_option2 = tk.Radiobutton(report_frame, text="Feature Request", variable=var1, value=2, fg='#000', bg='#d5e2f3', font=('Arial', 10, 'bold'))
    radio_option2.place(x=250, y=180)

    radio_option3 = tk.Radiobutton(report_frame, text="Other", variable=var1, value=3, fg='#000', bg='#d5e2f3', font=('Arial', 10, 'bold'))
    radio_option3.place(x=430, y=180)

    label_name = tk.Label(report_frame, text="Name:", bg='#d5e2f3', fg='#000', font=('Arial', 10, 'bold'))
    label_name.place(x=160, y=220)
    entry_name = tk.Entry(report_frame, width=25, font=('Arial', 12))
    entry_name.place(x=160, y=250)

    label_email = tk.Label(report_frame, text="Email:", bg='#d5e2f3', fg='#000', font=('Arial', 10, 'bold'))
    label_email.place(x=160, y=290)
    entry_email = tk.Entry(report_frame, width=25, font=('Arial', 12))
    entry_email.place(x=160, y=320)

    label_message = tk.Label(report_frame, text="Description:", bg='#d5e2f3', fg='#000', font=('Arial', 10, 'bold'))
    label_message.place(x=160, y=360)
    text_message = tk.Text(report_frame, height=5, width=50, font=('Arial', 10))
    text_message.place(x=160, y=390)

    submit_button = tk.Button(report_frame, text="Submit", width=10, height=1, font=('Arial', 12, 'bold'), bg='#059bad', fg='#000', bd=0,command=submit_report)
    submit_button.place(x=360, y=500)

    
    



def show_compression_page():
    for widget in content_frame.winfo_children():
        widget.destroy()
    global compression_frame
    compression_frame = tk.Frame(content_frame, width=900, height=820,bg='#d5e2f3')
    compression_frame.pack(side='right', fill='both', expand=True)

#d5e2f3
     
    def send():
        global filepath
        filepath=filedialog.askopenfilename()
        if filepath:
            text_box.delete(0, tk.END)  # Clear previous content
            text_box.insert(tk.END, filepath)
        
    def compress_file():
        #filepath = filedialog.askopenfilename()
        global filepath,status_label,compressed_filepath
        if filepath:
            try:
                with open(filepath, 'rb') as f:
                    original_data = f.read()
                    compressed_data = zlib.compress(original_data)

                compressed_filepath = filepath + '.compressed'
                with open(compressed_filepath, 'wb') as f:
                    f.write(compressed_data)

                #status_label.config(text=f"File compressed successfully: {compressed_filepath}")
                messagebox.showinfo("Compression Successful", f"File compressed successfully: {compressed_filepath}")
            except Exception as e:
                #status_label.config(text=f"Error: {str(e)}")
                messagebox.showerror("Compression Error", f"Error: {str(e)}")

    profile = tk.Button(content_frame, image=image, bg="#d5e2f3", bd=0,)
    profile.place(x=300, y=100)

    text_box = tk.Entry(content_frame, font='arial 22', fg='white', bg='#059bad', bd=0, width=35)
    text_box.place(x=130, y=420)

    select_file = tk.Button(content_frame, image=image5, bg="#059bad",bd=0,relief=tk.RAISED, highlightthickness=2, padx=10, pady=5,command=send)
    select_file.place(x=640, y=420)

    select_button = tk.Button(content_frame, text="Compress", width=10, height=1, font='arial 14 bold', bg='#059bad', fg='#000', bd=0, relief=tk.RAISED, highlightthickness=2, padx=10, pady=5,command=compress_file)
    select_button.place(x=350, y=500)

    

def show_decompression_page():
    for widget in content_frame.winfo_children():
        widget.destroy()
    global decompression_frame
    decompression_frame = tk.Frame(content_frame, width=900, height=820, bg='#d5e2f3')
    decompression_frame.pack(side='right', fill='both', expand=True)
    
    
    global filepath
    
    def select_file_decompress():
        global filepath
        filepath = filedialog.askopenfilename()
        if filepath:
            text_box.delete(0, tk.END)  # Clear previous content
            text_box.insert(tk.END, filepath)
    
    def decompress_file():
        global filepath
        if filepath:
            try:
                with open(filepath, 'rb') as f:
                    compressed_data = f.read()
                    decompressed_data = zlib.decompress(compressed_data)

                decompressed_filepath = filepath[:-len('.compressed')]
                with open(decompressed_filepath, 'wb') as f:
                    f.write(decompressed_data)

                messagebox.showinfo("Decompression Successful", f"File decompressed successfully: {decompressed_filepath}")
            except Exception as e:
                messagebox.showerror("Decompression Error", f"Error: {str(e)}")

    profile = tk.Button(decompression_frame, image=image, bg="#d5e2f3", bd=0,)
    profile.place(x=300, y=100)

    text_box = tk.Entry(decompression_frame, font='arial 22', fg='white', bg='#059bad', bd=0, width=35)
    text_box.place(x=130, y=420)

    select_file = tk.Button(decompression_frame, image=image5, bg="#059bad", bd=0, relief=tk.RAISED, highlightthickness=2, padx=10, pady=5, command=select_file_decompress)
    select_file.place(x=640, y=420)

    decompress_button = tk.Button(decompression_frame, text="Decompress File", width=15, height=1, font='arial 14 bold', bg='#059bad', fg='#000', bd=0, relief=tk.RAISED, highlightthickness=2, padx=10, pady=5, command=decompress_file)
    decompress_button.place(x=330, y=500)
    
'''def hide_other_frames():
    global about_us_frame, contact_us_frame, help_frame, feedback_frame, report_frame, send_frame, receive_frame
    frames = [about_us_frame, contact_us_frame, help_frame, feedback_frame, report_frame, send_frame, receive_frame]
    for frame in frames:
        if frame is not None:
            frame.pack_forget()'''
def show_main_dashboard():
    for widget in content_frame.winfo_children():
        widget.destroy()
    profile = tk.Button(content_frame, image=image, bg="#d5e2f3", bd=0)
    profile.place(x=300, y=80)
    send = tk.Button(content_frame, image=image1, bg='#d5e2f3', bd=0, command=show_send_page, cursor="hand2")
    send.place(x=200, y=390)
    receive = tk.Button(content_frame, image=image2, bg='#d5e2f3', bd=0, command=show_receive_page, cursor="hand2")
    receive.place(x=520, y=390)
    send_label = tk.Label(content_frame, text="Send", bg='#d5e2f3', fg="#04094e", font=("Agrandin", 20))
    send_label.place(x=230, y=540)
    receive_label = tk.Label(content_frame, text="Receive", fg="#04094e", bg='#d5e2f3', font=("Agrandin", 20))
    receive_label.place(x=535, y=540)
    bottom_frame = tk.Frame(root, width=900, height=100, bg='#7884a4')
    bottom_frame.place(x=252, y=692)
    About_us = tk.Button(bottom_frame, text="About US", bg="#7884a4", bd=0, fg="#04094e", command=about_us, cursor="hand2", font=("Agrandin", 16))
    About_us.pack(side="left", padx=10, pady=10)
    Contat_us = tk.Button(bottom_frame, text="Contact Us", command=contact_us, bg="#7884a4", fg="#04094e", bd=0, cursor="hand2", font=("Agrandin", 16))
    Contat_us.pack(side="left", padx=75, pady=10)
    Help = tk.Button(bottom_frame, text="Help", bg="#7884a4", command=help, bd=0, fg="#04094e", cursor="hand2", font=("Agrandin", 16))
    Help.pack(side="left", padx=20, pady=10)
    Report_btn = tk.Button(bottom_frame, text="Report", bg="#7884a4", bd=0, fg="#04094e", cursor="hand2", font=("Agrandin", 16), command=Report)
    Report_btn.pack(side="left", padx=60, pady=10)
    feedback = tk.Button(bottom_frame, text="Feedback", bg="#7884a4", bd=0, fg="#04094e", command=Feedback, cursor="hand2", font=("Agrandin", 16))
    feedback.pack(side="left", padx=30, pady=10)
    logout_button = tk.Button(root, image=image6,bg="#d5e2f3", bd=0, cursor="hand2", command=logout_function)
    logout_button.place(x=1020, y=5)  

def logout_function():
    root.destroy()
    import login

root = tk.Tk()
root.title("Fly Files")
root.configure(bg="#d5e2f3")
root.geometry("1100x750+200+10")

image_path = "Image/p1.png"
image1_path = "Image/sendf.png"
image2_path = "Image/receivef.png"
image3_path="Image/id.png"
image4_path="Image/text.png"
image5_path="Image/file.png"
image6_path="Image/logout1.png"
image7_path="Image/email.png"

profile_r = PhotoImage(file='Image/profile.png')
img = Image.open('Image/receiver.png')
resized_img = img.resize((760,250))
Hbackground = ImageTk.PhotoImage(resized_img)
image_icon=tk.PhotoImage(file='Image/arrow.png')

image = PhotoImage(file=image_path)
image1 = PhotoImage(file=image1_path)
image2 = PhotoImage(file=image2_path)
image3= PhotoImage(file=image3_path)
image4=PhotoImage(file=image4_path)
image5= PhotoImage(file=image5_path)
image6= PhotoImage(file=image6_path)
image7=PhotoImage(file=image7_path)

menu_frame = tk.Frame(root, width=200, height=820, bg="#059bad")
menu_frame.pack(side='left', fill='y', padx=0, pady=0)

left_menu_top_image_path = "Image/output-onlinepngtools (26).png"
left_menu_top_image = PhotoImage(file=left_menu_top_image_path)

left_menu_top_label = tk.Label(menu_frame, image=left_menu_top_image, bg="#059bad")
left_menu_top_label.pack(pady=10)

File_Transfer = tk.Button(menu_frame, text="File Transfer", width=20, bg="#059bad", bd=0, relief=tk.FLAT, highlightthickness=0,
                          font=("Agrandin", 16), cursor="hand2", fg="#04094e", command=show_main_dashboard)  # Increase font size here
File_Transfer.pack(pady=10)

File_Compression = tk.Button(menu_frame, text="File Compression", width=20, bg="#059bad", bd=0, relief=tk.FLAT, highlightthickness=0,
                          font=("Agrandin", 16), command=show_compression_page, cursor="hand2", fg="#04094e")  #  font size here
File_Compression.pack(pady=10)

File_DeCompression = tk.Button(menu_frame, text="File Decompression", width=20, bg="#059bad", bd=0, relief=tk.FLAT, highlightthickness=0,
                          font=("Agrandin", 16), command=show_decompression_page, cursor="hand2", fg="#04094e")  # Increase font size here
File_DeCompression.pack(pady=10)

content_frame = tk.Frame(root, width=900, height=820, bg='#d5e2f3')
content_frame.pack(side='right', fill='both', expand=True)

show_main_dashboard()


root.mainloop()
