# GUI modules
from tkinter import Tk, StringVar, messagebox
import tkinter.ttk as ttk
from tkcalendar.dateentry import DateEntry
# Database modules
# import mysql.connector
import sqlite3
# Supporting modules
from datetime import datetime
import os

icon='student.ico'
# MySQL connection
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
    Tk().withdraw()  # Hides window
    messagebox.showwarning('Database', 'Mysql Connection Problem')
    exit()


# Result window
def result_window(res):
    window1 = Tk()
    window1.title('RESULT')
    window1.geometry('500x400')
    window1.resizable(0, 0)
    window1.iconbitmap(icon)
    sty = ttk.Style()
    sty.configure('T.TLabel', font=('Cambria', 14))
    sty.configure('TLabel', font=('comic sans', 12))

    ttk.Label(window1, text='Apr-May 2020 Examination', style='T.TLabel').pack(pady=20)
    ttk.Label(window1, text='Register No :   {}'.format(res[0][0])).place(x=100, y=100)
    ttk.Label(window1, text='Date Of Birth :   {}'.format(res[0][1])).place(x=100, y=160)
    ttk.Label(window1, text='Grade :   {}'.format(res[0][2])).place(x=100, y=220)
    ttk.Label(window1, text='CGPA :   {}%'.format(res[0][3])).place(x=100, y=280)
    if float(res[0][3]) < 50:
        ttk.Label(window1, text='Better Luck Next Time', foreground='red').place(x=230, y=280)
    else:
        ttk.Label(window1, text='Pass!', foreground='green').place(x=230, y=280)
    window1.mainloop()


# Submit window
submit_window = Tk()
submit_window.title('RESULT')
submit_window.geometry('600x400')
submit_window.resizable(0, 0)
submit_window.iconbitmap(icon)
style1 = ttk.Style()
style1.configure('TLabel', font=16)
style1.configure('TButton', font=18, padding=2, relief='groove', background='black')

label1 = ttk.Label(submit_window, text="Register no : ").place(x=100, y=100)
label2 = ttk.Label(submit_window, text="Date of birth : ").place(x=100, y=180)

register_no = StringVar()
entry1 = ttk.Entry(submit_window, text=register_no)
entry1.place(x=250, y=100, width=220, height=27)

entry2 = DateEntry(submit_window, date_pattern='y-mm-dd', calendar_cursor='hand2', year=2000)
entry2.place(x=250, y=180, width=220, height=27)


# Submit Button
def result():
    reg_no = entry1.get()
    temp_dob = entry2.get()
    dob = datetime.strptime(str(temp_dob), '%Y-%m-%d').strftime('%d %B %Y').lower()
    try:
        conn.execute("select * from result where regno={} and dob='{}'".format(reg_no, dob))
        fetch = conn.fetchall()
        if fetch:  # non empty list
            submit_window.destroy()
            result_window(fetch)

        else:  # empty list
            messagebox.showinfo('Login', 'Invalid register no or date of birth')  # Invalid reg and dob
    except mysql.connector.errors.ProgrammingError:
        messagebox.showinfo('Login', 'Invalid register no or date of birth')  # Invalid format


b1 = ttk.Button(submit_window, text="SUBMIT", command=result).place(x=150, y=280, height=40, width=100)


# Cancel Button
def cancel():
    submit_window.destroy()


b2 = ttk.Button(submit_window, text="CANCEL", command=cancel).place(x=360, y=280, height=40, width=100)

submit_window.mainloop()
