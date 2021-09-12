from email import message
import email
import smtplib
from tkinter import *
import tkinter as tk
import os, cv2
import shutil
import csv
import numpy as np
from tkinter import font
from tkinter.font import BOLD
from PIL import ImageTk, Image
import pandas as pd
pd.options.mode.chained_assignment = None
import datetime
import time
import tkinter.font as font
import pyttsx3
from tkinter import messagebox
import random
import array
import pyrebase
from pyrebase.pyrebase import Auth
import os

import show_attendance
import takeImage
import trainImage
import automaticAttedance

firebaseConfig = {
    'apiKey': "AIzaSyBEapbPNQFoJJPHqkbYytXKc10EKnW4ZSk",
    'authDomain': "attendance-management-sy-59713.firebaseapp.com",
    'databaseURL': "https://attendance-management-sy-59713-default-rtdb.firebaseio.com",
    'projectId': "attendance-management-sy-59713",
    'storageBucket': "attendance-management-sy-59713.appspot.com",
    'messagingSenderId': "536903474701",
    'appId': "1:536903474701:web:9c48127a90a84b57113f44",
    'measurementId': "G-WEGC8M0TRN"
  }


firebase1=pyrebase.initialize_app(firebaseConfig)

auth=firebase1.auth()

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

class login:
    def __init__(self,root):
        self.root = root
        self.root.title("Attandance Management System")
        self.root.geometry("900x600+100+50")
        self.root.resizable(False,False)
        self.bg = ImageTk.PhotoImage(file = "Images/background.jpg")
        self.bg_Image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #login frame
        frame_login = Frame(self.root, bg="white",border=5, borderwidth=10)
        frame_login.place(x=220, y=80,width=450, height=400)

        title1 = Label(frame_login, text="Login Here", font=("Impact", 35,"bold", "underline"),bg="white").place(x=105, y=1)
        desc = Label(frame_login, text="Welcome to Attendance Management System", font=("Cooper Black", 12),fg="#353332",bg="white").place(x=30, y=65)


        lbl_user = Label(frame_login, text="E-Mail", font=("Goudy old style", 15, "bold"),fg="#353332",bg="white").place(x=65, y=95)
        self.text_user= Entry(frame_login, font=("times new roman", 12 ),bg="lightgrey")
        self.text_user.place(x=65, y=125,width=300, height=35)

        
        

        lbl_pass1 = Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"),fg="#353332",bg="white").place(x=65, y=170)
        self.text_pass1= Entry(frame_login, show="*",font=("times new roman", 12),bg="lightgrey")
        self.text_pass1.place(x=65, y= 210,width=300, height=35)

        

        otp = StringVar()
        def send_message():
            sender_email = "minorprojectsem2@gmail.com"
            receiver_email = self.text_user.get()
            MAX_LEN = 8

            # declare arrays of the character that we need in out password
            # Represented as chars to enable easy string concatenation
            DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                'z']

            UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                                'Z']

            SYMBOLS = ['@', '#',]

            # combines all the character arrays above to form one array
            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

            # randomly select at least one character from each character set above
            rand_digit = random.choice(DIGITS)
            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)

            # combine the character randomly selected above
            # at this stage, the password contains only 4 characters but
            # we want a 12-character password
            temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


            # now that we are sure we have at least one character from each
            # set of characters, we fill the rest of
            # the password length by selecting randomly from the combined
            # list of character above.
            for x in range(MAX_LEN - 4):
                temp_pass = temp_pass + random.choice(COMBINED_LIST)

                # convert temporary password into array and shuffle to
                # prevent it from having a consistent pattern
                # where the beginning of the password is predictable
                temp_pass_list = array.array('u', temp_pass)
                random.shuffle(temp_pass_list)

            # traverse the temporary password array and append the chars
            # to form the password
            password = ""
            for x in temp_pass_list:
                password = password + x

            otp.set(password) 
                            
            print(password)
            sender_password = "Minor@1234"
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(sender_email,sender_password)
            print("loggined")
            server.sendmail(sender_email,receiver_email,password)
            print("Message Send..!!")
            messagebox.showinfo("Alert", f"OTP sent to {receiver_email}")


        get_otp = Button(frame_login,command=send_message ,text="Get OTP", bg="lightgrey", font=("Georgia", 8, "bold")).place(x=65, y=332)

        lbl_pass = Label(frame_login, text="Enter OTP", font=("Goudy old style", 15, "bold"),fg="#353332",bg="white").place(x=65, y=265)
        self.text_pass= Entry(frame_login, font=("times new roman", 12 ),bg="lightgrey")
        self.text_pass.place(x=65, y=295,width=300, height=35)

        def login_function():
            emails=self.text_user.get()
            password=self.text_pass1.get()
            
            try:
                auth.sign_in_with_email_and_password(emails, password)
                if self.text_pass.get() == otp.get():
                    messagebox.showinfo("Welcome", "You are logined")

                # filename = "attendance.py"
                # os.system(filename)
           
                haarcasecade_path = ("haarcascade_frontalface_default.xml"
                )
                trainimagelabel_path = (
                    "TrainingImageLabel\\Trainner.yml"
                )
                trainimage_path = "TrainingImage"

                studentdetail_path = (
                    "StudentDetails\\studentdetails.csv"
                )
                attendance_path = "Attendance-Management-system-using-face-recognition"


                window = Tk()
                window.title("Face recognizer")
                window.geometry("1280x720")
                dialog_title = "QUIT"
                dialog_text = "Are you sure want to close?"
                window.configure(background="black")


                # to destroy screen
                def del_sc1():
                    sc1.destroy()


                # error message for name and no
                def err_screen():
                    global sc1
                    sc1 = tk.Tk()
                    sc1.geometry("400x110")
                    sc1.iconbitmap("AMS.ico")
                    sc1.title("Warning!!")
                    sc1.configure(background="black")
                    sc1.resizable(0, 0)
                    tk.Label(
                        sc1,
                        text="Enrollment & Name required!!!",
                        fg="yellow",
                        bg="black",
                        font=("times", 20, " bold "),
                        ).pack()
                    tk.Button(
                        sc1,
                        text="OK",
                        command=del_sc1,
                        fg="yellow",
                        bg="black",
                        width=9,
                        height=1,
                        activebackground="Red",
                        font=("times", 20, " bold "),
                    ).place(x=110, y=50)


                def testVal(inStr, acttyp):
                    if acttyp == "1":  # insert
                        if not inStr.isdigit():
                            return False
                    return True


                logo = Image.open("UI_Image/0001.png")
                logo = logo.resize((50, 47), Image.ANTIALIAS)
                logo1 = ImageTk.PhotoImage(logo)
                titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
                titl.pack(fill=X)
                l1 = tk.Label(window, image=logo1, bg="black",)
                l1.place(x=470, y=10)

                titl = tk.Label(
                    window, text="Institue of Management And Enterpunership Development", bg="black", fg="Blue", font=("arial", 27),
                )
                titl.place(x=150, y=10)

                a = tk.Label(
                    window,
                    text="Welcome to the Face Recognition Based\nAttendance Management System",
                    bg="black",
                    fg="yellow",
                    bd=10,
                    font=("arial", 35),
                )
                a.pack()

                ri = Image.open("UI_Image/register.png")
                r = ImageTk.PhotoImage(ri)
                label1 = Label(window, image=r)
                label1.image = r
                label1.place(x=100, y=270)

                ai = Image.open("UI_Image/attendance.png")
                a = ImageTk.PhotoImage(ai)
                label2 = Label(window, image=a)
                label2.image = a
                label2.place(x=980, y=270)

                vi = Image.open("UI_Image/verifyy.png")
                v = ImageTk.PhotoImage(vi)
                label3 = Label(window, image=v)
                label3.image = v
                label3.place(x=600, y=270)


                def TakeImageUI():
                    ImageUI = Tk()
                    ImageUI.title("Take Student Image..")
                    ImageUI.geometry("780x480")
                    ImageUI.configure(background="black")
                    ImageUI.resizable(0, 0)
                    titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
                    titl.pack(fill=X)
                    # image and title
                    titl = tk.Label(
                        ImageUI, text="Register Your Face", bg="black", fg="green", font=("arial", 30),
                    )
                    titl.place(x=270, y=12)

                    # heading
                    a = tk.Label(
                        ImageUI,
                        text="Enter the details",
                        bg="black",
                        fg="yellow",
                        bd=10,
                        font=("arial", 24),
                    )
                    a.place(x=280, y=75)

                    # ER no
                    lbl1 = tk.Label(
                        ImageUI,
                        text="Enrollment No",
                        width=10,
                        height=2,
                        bg="black",
                        fg="yellow",
                        bd=5,
                        relief=RIDGE,
                        font=("times new roman", 12),
                    )
                    lbl1.place(x=120, y=130)
                    txt1 = tk.Entry(
                        ImageUI,
                        width=17,
                        bd=5,
                        validate="key",
                        bg="black",
                        fg="yellow",
                        relief=RIDGE,
                        font=("times", 25, "bold"),
                    )
                    txt1.place(x=250, y=130)
                    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

                    # name
                    lbl2 = tk.Label(
                        ImageUI,
                        text="Name",
                        width=10,
                        height=2,
                        bg="black",
                        fg="yellow",
                        bd=5,
                        relief=RIDGE,
                        font=("times new roman", 12),
                    )
                    lbl2.place(x=120, y=200)
                    txt2 = tk.Entry(
                        ImageUI,
                        width=17,
                        bd=5,
                        bg="black",
                        fg="yellow",
                        relief=RIDGE,
                        font=("times", 25, "bold"),
                    )
                    txt2.place(x=250, y=200)

                    lbl3 = tk.Label(
                        ImageUI,
                        text="Notification",
                        width=10,
                        height=2,
                        bg="black",
                        fg="yellow",
                        bd=5,
                        relief=RIDGE,
                        font=("times new roman", 12),
                    )
                    lbl3.place(x=120, y=270)

                    message = tk.Label(
                        ImageUI,
                        text="",
                        width=32,
                        height=2,
                        bd=5,
                        bg="black",
                        fg="yellow",
                        relief=RIDGE,
                        font=("times", 12, "bold"),
                    )
                    message.place(x=250, y=270)

                    def take_image():
                        l1 = txt1.get()
                        l2 = txt2.get()
                        takeImage.TakeImage(
                            l1,
                            l2,
                            haarcasecade_path,
                            trainimage_path,
                            message,
                            err_screen,
                            text_to_speech,
                        )
                        txt1.delete(0, "end")
                        txt2.delete(0, "end")

                    # take Image button
                    # image
                    takeImg = tk.Button(
                        ImageUI,
                        text="Take Image",
                        command=take_image,
                        bd=10,
                        font=("times new roman", 18),
                        bg="black",
                        fg="yellow",
                        height=2,
                        width=12,
                        relief=RIDGE,
                    )
                    takeImg.place(x=130, y=350)

                    def train_image():
                        trainImage.TrainImage(
                            haarcasecade_path,
                            trainimage_path,
                            trainimagelabel_path,
                            message,
                            text_to_speech,
                        )

                    # train Image function call
                    trainImg = tk.Button(
                        ImageUI,
                        text="Train Image",
                        command=train_image,
                        bd=10,
                        font=("times new roman", 18),
                        bg="black",
                        fg="yellow",
                        height=2,
                        width=12,
                        relief=RIDGE,
                    )
                    trainImg.place(x=360, y=350)


                r = tk.Button(
                    window,
                    text="Register a new student",
                    command=TakeImageUI,
                    bd=10,
                    font=("times new roman", 16),
                    bg="black",
                    fg="yellow",
                    height=2,
                    width=17,
                )
                r.place(x=100, y=520)


                def automatic_attedance():
                    automaticAttedance.subjectChoose(text_to_speech)


                r = tk.Button(
                    window,
                    text="Take Attendance",
                    command=automatic_attedance,
                    bd=10,
                    font=("times new roman", 16),
                    bg="black",
                    fg="yellow",
                    height=2,
                    width=17,
                )
                r.place(x=600, y=520)


                def view_attendance():
                    show_attendance.subjectchoose(text_to_speech)


                r = tk.Button(
                    window,
                    text="View Attendance",
                    command=view_attendance,
                    bd=10,
                    font=("times new roman", 16),
                    bg="black",
                    fg="yellow",
                    height=2,
                    width=17,
                )
                r.place(x=1000, y=520)
                r = tk.Button(
                    window,
                    text="EXIT",
                    bd=10,
                    command=quit,
                    font=("times new roman", 16),
                    bg="black",
                    fg="yellow",
                    height=2,
                    width=17,
                )
                r.place(x=600, y=660)
            except:
                messagebox.showerror("Alert", "You entered wrong E-mail/Password/OTP")

               
        def mark():
            if var1.get()==1:
                self.text_pass1.configure(show="")
            elif var1.get()==0:
                self.text_pass1.configure(show="*")
           

        var1 = IntVar()
        cb = Checkbutton(frame_login,command = mark, offvalue = 0, onvalue = 1, variable=var1 ,text="👁️",bg="lightgrey").place(x=300, y=215)

        #
        login_btn = Button(self.root,command=login_function ,text="Login", fg="white",bg="#585858", font=("Georgia", 16, "bold")).place(x=370, y=460,width=150)

    

        
    # def frgt_pass(self):
    #     frame1 = Frame(self.root, bg="white",border=5, borderwidth=10)
    #     frame1.place(x=170, y=100,width=550, height=400)

    #     title2 = Label(frame1, text="Forgot Password", font=("Impact", 35,"bold", "underline"),bg="white").place(x=95, y=10)
    #     desc1 = Label(frame1, text="Please provide your username", font=("Cooper Black", 12),fg="#353332",bg="white").place(x=130, y=75)

    #     lbl_user_frgt = Label(frame1, text="Username", font=("Goudy old style", 15, "bold"),fg="#353332",bg="white").place(x=120, y=125)
    #     self.text_user_frgt= Entry(frame1, font=("times new roman", 12 ),bg="lightgrey")
    #     self.text_user_frgt.place(x=120, y=155,width=290, height=35)

    #     cb = Checkbutton(frame1,text="above information is correct",bg="white").place(x=170, y=207)
    # # def chk_btn(self):
    # #     if var.get()==1:

    
    #     submit_butn = Button(frame1 ,text="Submit",command=self.send_message, fg="white",bg="#585858", font=("Georgia", 16, "bold")).place(x=180, y=250,width=150)

    # def send_message(self):
    #     sender_email = "minorprojectsem2@gmail.com"
    #     receiver_email = self.text_user_frgt.get()
    #     email_info = "hello"
    #     sender_password = "Qwerty@1234"
    #     # message = "Accident has been detected"
    #     server = smtplib.SMTP('smtp.gmail.com',587)
    #     server.starttls()
    #     server.login(sender_email,sender_password)
    #     print("loggined")
    #     server.sendmail(sender_email,receiver_email,email_info)
    #     print("Message Send..!!")
    #     messagebox.showinfo("Alert", "Message")

    #     self.text_user_frgt.delete(0,END)



    # def login_function(self):
    #     if self.text_pass.get()=="" or self.text_user.get()=="":
    #         messagebox.showerror("Error!!", "Please Enter Correct Username/Password", parent=self.root)
    #     else:
    #         messagebox.showinfo("Welcome", "You are logged In", parent=self.root)
            


root = Tk()
obj = login(root)
root.mainloop()
