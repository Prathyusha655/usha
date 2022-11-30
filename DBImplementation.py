from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time
import socket
import pymysql

#connecting to the database
db = mysql.connector.connect(host="localhost",user="root",password="pass@123",database="demo1")
mycur = db.cursor()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err,text="All fields are required..",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="orange",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="orange", width=8, height=1, command=succ_destroy).pack()

def register_user():
    FirstName_info = FirstName.get()
    LastName_info = LastName.get()    
    UserName_info = UserName.get()
    Password_info = Password.get()
    if FirstName_info == "":
        error()
    elif LastName_info == "":
        error()
    elif UserName_info == "":
        error ()
    elif Password_info == "":
        error()    

    else:
        sql = "insert into login values(%s,%s, %s, %s)"
        t = (FirstName_info,LastName_info,UserName_info,Password_info)
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        success()



def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration Portal")
    root1.geometry("500x400")
    global FirstName
    global LastName
    global UserName
    global Password
    Label(root1,text="Register your account",bg="orange",fg="black",font="bold",width=400).pack()
    FirstName = StringVar()
    LastName = StringVar()
    UserName = StringVar()
    Password = StringVar()
    Label(root1,text="").pack()
        
    Label(root1,text="FirstName :",font="bold").pack()
    Entry(root1,textvariable=FirstName,show="").pack()
        
    Label(root1,text="LastName :",font="bold").pack()
    Entry(root1,textvariable=LastName,show="").pack()
    
    Label(root1,text="UserName :",font="bold").pack()
    Entry(root1,textvariable=UserName,show="").pack()
    Label(root1, text="").pack()
    Label(root1, text="Password :", font="bold").pack()
    Entry(root1, textvariable=Password,show="*").pack()
    Label(root1, text="").pack()
    Button(root1,text="Register",bg="red",command=register_user).pack()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Log-In Portal")
    root2.geometry("400x400")
    global UserName_varify
    global Password_varify
    Label(root2, text="Log-In Portal", bg="grey", fg="black", font="bold",width=300).pack()
    UserName_varify = StringVar()
    Password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="UserName :", font="bold").pack()
    Entry(root2, textvariable=UserName_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :").pack()
    Entry(root2, textvariable=Password_varify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In", bg="red",command=login_varify).pack()
    Label(root2, text="")

def logg_destroy():
    logg.destroy()
    root2.destroy()

def fail_destroy():
    fail.destroy()

def logged():
    global logg
    logg = Toplevel(root2)
    logg.title("Welcome")
    logg.geometry("200x100")
    Label(logg, text="Welcome {} ".format(UserName_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="orange", width=8, height=1, command=logg_destroy).pack()


def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="orange", width=8, height=1, command=fail_destroy).pack()


def login_varify():
    user_varify = UserName_varify.get()
    pas_varify = Password_varify.get()
    sql = "select * from login where UserName = %s and Password = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    a=time.localtime()
    c1=time.asctime(a)
    print(c1)
    hostname = socket.gethostname()
    myip = socket.gethostbyname(hostname)
    print("IP ADDRESS IS" +myip)
    query1 = "INSERT INTO LOGINDETAILS1(username,time,ipaddress) Values('{}','{}','{}')".format(user_varify,c1,myip)
    mycur.execute(query1)
    db.commit()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()


def main_screen():
    global root
    root = Tk()
    root.title("Log-IN Portal")
    root.geometry("300x300")
    Label(root,text="Welcome to Log-In Protal",font="bold",bg="grey",fg="black",width=400).pack()
    Label(root,text="").pack()
    Button(root,text="Log-IN",width="8",height="1",bg="red",font="bold",command=login).pack()
    Label(root,text="").pack()
    Button(root, text="Registration",height="1",width="15",bg="red",font="bold",command=registration).pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Label(root,text="Developed By Prathyusha").pack()

main_screen()
root.mainloop()
