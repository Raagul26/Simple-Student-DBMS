# GUI module
from tkinter import messagebox
from tkinter import *
import tkinter.ttk as ttk
from tkcalendar.dateentry import DateEntry
# Database module
# import mysql.connector
import sqlite3
# Supporting modules
from datetime import datetime
import os

icon='student.ico'
# Database Connection
database_file = 'Student_Database.db'  # Change your database name here
try:
    if os.path.isfile(database_file):
        connect = sqlite3.connect(database_file)
        print('Database file')
    else:
        try:
            import mysql.connector
        except:
            Tk().withdraw()  # Hides window
            messagebox.showwarning('Requirements', 'Install mysql module')
            exit()
        connect = mysql.connector.connect(
            host='localhost',  # Enter host name here
            user='root',  # Enter user name here
            password='admin',  # Enter password here
            database='studentdatabasemgnt')  # Change your MySQL database here
        print('Mysql')
    conn = connect.cursor()  # Handler
except mysql.connector.errors.InterfaceError:
    Tk().withdraw()
    messagebox.showwarning('Database', 'Mysql Connection Problem')
    exit()


# Student Registration function
def student_register():
    # Registration window
    reg_window = Tk()
    reg_window.geometry('800x500')
    reg_window.title('ADD NEW STUDENT')
    reg_window.resizable(0, 0)
    reg_window.iconbitmap(icon)
    s = ttk.Style()
    s.configure('TLabel', font=('comic sans', 12))
    s.configure('TButton', font=12, padding=2)

    # Labels
    ttk.Label(reg_window, text='STUDENT REGISTRATION').pack(pady=10)
    ttk.Label(reg_window, text='  First Name: ').place(x=80, y=80)
    ttk.Label(reg_window, text='  Last Name: ').place(x=80, y=120)
    ttk.Label(reg_window, text='     Gender: ').place(x=80, y=160)
    ttk.Label(reg_window, text='     Course: ').place(x=80, y=200)
    ttk.Label(reg_window, text='  SSLC Mark: ').place(x=80, y=240)
    ttk.Label(reg_window, text='   HSC Mark: ').place(x=80, y=280)
    ttk.Label(reg_window, text='Register no: ').place(x=80, y=320)
    ttk.Label(reg_window, text="Father's Name: ").place(x=400, y=80)
    ttk.Label(reg_window, text="Mother's Name: ").place(x=400, y=120)
    ttk.Label(reg_window, text='Date of birth: ').place(x=400, y=160)
    ttk.Label(reg_window, text='    Mobile no: ').place(x=400, y=200)
    ttk.Label(reg_window, text='      Address: ').place(x=400, y=240)

    # Input boxes
    fname = StringVar()
    ttk.Entry(reg_window, text=fname).place(x=180, y=80, height=24, width=200)
    lname = StringVar()
    ttk.Entry(reg_window, text=lname).place(x=180, y=120, height=24, width=200)
    gen = StringVar()
    ttk.Combobox(reg_window, text=gen, values=['Male', 'Female', 'Others']).place(x=180, y=160, height=24, width=200)
    course = StringVar()
    ttk.Combobox(reg_window, text=course,
                 values=['IT', 'CSE', 'ECE', 'EEE', 'MECH', 'CIVIL']).place(x=180, y=200, height=24, width=200)
    sslc = StringVar()
    ttk.Entry(reg_window, text=sslc).place(x=180, y=240, height=24, width=200)
    hsc = StringVar()
    ttk.Entry(reg_window, text=hsc).place(x=180, y=280, height=24, width=200)
    regno = StringVar()
    ttk.Entry(reg_window, text=regno).place(x=180, y=320, height=24, width=200)
    frname = StringVar()
    ttk.Entry(reg_window, text=frname).place(x=520, y=80, height=24, width=200)
    mrname = StringVar()
    ttk.Entry(reg_window, text=mrname).place(x=520, y=120, height=24, width=200)
    dob = DateEntry(reg_window, date_pattern='y-mm-dd', calendar_cursor='hand2', year=2000)
    dob.place(x=520, y=160, height=24, width=200)
    mob = StringVar()
    ttk.Entry(reg_window, text=mob).place(x=520, y=200, height=24, width=200)
    add = Text(reg_window, border=1)
    add.place(x=520, y=240, height=100, width=200)

    # Register Button
    def register():
        # Getting Entered values
        first_name = fname.get()
        last_name = lname.get()
        gender = gen.get()
        dept = course.get()
        sslc_mark = sslc.get()
        hsc_mark = hsc.get()
        register_no = regno.get()
        father_name = frname.get()
        mother_name = mrname.get()
        temp_date_of_birth = dob.get()
        date_of_birth = datetime.strptime(str(temp_date_of_birth), '%Y-%m-%d').strftime('%d %B %Y').lower()
        mobile_no = mob.get()
        address = add.get(1.0, END)

        # print(first_name, last_name, gender, dept, sslc_mark, hsc_mark, register_no, father_name,
        #      mother_name, date_of_birth, mobile_no, address)
        conn.execute(
            "INSERT INTO stu_reg (`fname`, `lname`, `gender`, `course`, `sslc`, `hsc`, `regno`, `frname`, `mrname`, `dob`, `mobile`, `address`)VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"
                .format(first_name, last_name, gender, dept, sslc_mark, hsc_mark, register_no, father_name, mother_name,
                        date_of_birth, mobile_no, address))
        connect.commit()
        messagebox.showinfo('New Student', 'Created Successfully')

    ttk.Button(reg_window, text='REGISTER', command=register).place(x=200, y=400, height=40, width=120)

    # Close Button
    def close():
        reg_window.destroy()

    ttk.Button(reg_window, text='CLOSE', command=close).place(x=500, y=400, height=40, width=100)

    reg_window.mainloop()


# Login window
login_window = Tk()
login_window.title('LOGIN')
login_window.geometry('600x400')
login_window.resizable(0, 0)
login_window.iconbitmap(icon)
style = ttk.Style()
style.configure('TLabel', font=18)
style.configure('TButton', font=18, padding=2, relief='groove', background='black')

# Labels
label1 = ttk.Label(login_window, text="STAFF LOGIN").pack(pady=20)
label2 = ttk.Label(login_window, text="USER ID : ").place(x=100, y=100)
label3 = ttk.Label(login_window, text="PASSWORD : ").place(x=100, y=180)

# Entry boxes
user_name = StringVar()
entry1 = ttk.Entry(login_window, text=user_name).place(x=250, y=100, width=220, height=27)
password = StringVar()
entry2 = ttk.Entry(login_window, text=password, show=u'\u2731').place(x=250, y=180, width=220, height=27)


# Login Button
def user_login():
    user_id = user_name.get()
    passwd = password.get()
    conn.execute('select * from logininfo')
    if (user_id, passwd) in conn.fetchall():
        login_window.destroy()
        student_register()
    else:
        messagebox.showinfo('Login', 'Invalid USER ID or PASSWORD')


login_button = ttk.Button(login_window, text="LOGIN", command=user_login).place(x=180, y=280, height=40, width=100)


# Cancel Button
def cancel():
    login_window.destroy()


cancel_button = ttk.Button(login_window, text="CANCEL", command=cancel).place(x=330, y=280, height=40, width=100)

login_window.mainloop()
