from tkinter import *
from tkinter import messagebox as ms
import mysql.connector
from mysql.connector import Error
from tkinter import ttk
from random import randint
import datetime
from datetime import *
from xlrd import *
from xlsxwriter import *
from tkinter import simpledialog
import datetime
from tkcalendar import Calendar, DateEntry



class vriable_int:
    def __init__(self, master):
       self.master = master
#----------------STUDENT REG SECTION--------------
       self.user_name = StringVar()
       self.reg_number = StringVar()
       self.address = StringVar() 
       self.telephone = StringVar()
       self.expiring_date = StringVar()
#----------------STUDENT UPDATE REG SECTION--------------
       self.u_user_name = StringVar()
       self.u_reg_number = StringVar()
       self.u_address = StringVar() 
       self.u_telephone = StringVar()
       self.u_expiring_date = StringVar()
 #------------------admin reg ........
       self.ad_username_reg = StringVar()
       self.ad_password_reg = StringVar()
#--------------book section----------
       self.b_author = StringVar()
       self.b_publisher = StringVar()
       self.b_title = StringVar()
       self.b_edition = StringVar()
       self.b_total = StringVar()
       self.b_classification = StringVar()
       self.b_ref_no = StringVar()
       self.b_price = StringVar()
       self.b_date = StringVar()
       #self.b_status = StringVar()
#-----------books update-------------
       self.ub_author = StringVar()
       self.ub_publisher = StringVar()
       self.ub_title = StringVar()
       self.ub_edition = StringVar()
       self.ub_classification = StringVar()
       self.ub_ref_no = StringVar()
       self.ub_price = StringVar()
       self.ub_date = StringVar()
       self.ub_total = StringVar()
#----------borrowers sec input-------------
       self.title_of_book = StringVar()
       self.author = StringVar()
       self.ref_number = StringVar()
       self.borrowers_name = StringVar()
       self.reg_no = StringVar()
       self.date_of_rent = StringVar()
       self.date_of_exp = StringVar()
#-----------------------ALL SEARCH INPUT---------------------------------------

       self.search = StringVar()
       self.search_for_books = StringVar()
       self.search_for_borrowers_section = StringVar()
       #self.options = StringVar()


#-----------------borrowers update sec input-------------
       self.u_title_of_book = StringVar()
       self.u_author = StringVar()
       self.u_ref_number = StringVar()
       self.u_borrowers_name = StringVar()
       self.u_reg_no = StringVar()
       self.u_date_of_rent = StringVar()
       self.u_date_of_exp = StringVar()
       

       self.username_login_input = StringVar()
       self.password_login_input = StringVar()
       self.name_u = StringVar()
       self.class_u = StringVar()
       self.reg_u = StringVar()
       self.books_u = StringVar()

       Label(self.master, text = "WELCOM TO DON BOSCO SCHOOL LIBARY MANAGEMENT SYSTEM", bg = "blue", width = "200", height = "2", font=("calibri", 13)).grid(sticky=NSEW, pady=10,row=0, column=0, rowspan=3)
       background_img = PhotoImage(file = 'C:\\Users\\starprince\\Desktop\\main project\\images\\book11.png')
       background_img.image = background_img
       Label(self.master, image=background_img).place(x=30, y=20)
       Button(self.master, text="LOGIN ADMIN", command=self.login_win).place(x=215, y=230, height=90, width = 190)

#-----------------------------------------------------------login and registration section page-------------------------------------------------------------------------------------------------------------------
       
#----------------------------------------------regster an admin----------------------------------------------------
    def admin_reg_window(self):
        self.master.withdraw()
        self.admin_reg_win = Toplevel(root)
        self.admin_reg_win.geometry("500x500")
        self.admin_reg_win.title("ADMIN")
        Label(self.admin_reg_win, text = "PLEASE INPUT YOUR DETAILS", bg = "coral", width = "300", height = "2", font=("calibri", 13)).pack()
        Label(self.admin_reg_win, text = "USERNAME*", width = "300", height = "2", font=("calibri", 13)).pack()
        Entry(self.admin_reg_win, width=50, textvariable=self.ad_username_reg).pack()
        Label(self.admin_reg_win, text = "PASSWORD*", width = "300", height = "2", font=("calibri", 13)).pack()
        Entry(self.admin_reg_win, width=50, textvariable=self.ad_password_reg).pack()
        Button(self.admin_reg_win, text="REGISTER AN ADMIN", command=self.admin_registration_fuc).pack(pady = "15")
        
#-------------------------admin check and reg insert fuct---------------------------------------------------
    def admin_registration_fuc(self):
            user_var = self.ad_username_reg.get()
            pass_var = self.ad_password_reg.get()
            if (user_var == ""):
                ms.showerror("WARNING!!","Empty User Name")
            elif (pass_var == ""):
                 ms.showerror("WARNING!!","Empty Password")
            else:
                 self.conn = mysql.connector.connect(
                     host="localhost", user="root", passwd="", db="project_tables")
                 self.cur = self.conn.cursor()
                 mySql_insert_query = "SELECT Name FROM admin WHERE Name=%s"
                 recordTuple = (user_var,)
                 self.cur.execute(mySql_insert_query, recordTuple)
                 self.records = self.cur.fetchone()
                 self.conn.commit()
                 self.conn.close()
                 if (self.records):
                  ms.showerror("WARNING!!","user with the same name already exist")
                 else:
                    self.admin_insert_registration_fuc()        
     
#---------------------------------insert fuct for admin------------------------
    def admin_insert_registration_fuc(self):
        try:
            user_var = self.ad_username_reg.get()
            pass_var = self.ad_password_reg.get()
            self.conn = mysql.connector.connect(
                host="localhost", user="root", passwd="", db="project_tables")
            self.cur = self.conn.cursor()
            mySql_insert_query = """INSERT INTO admin (Name, password)
                                VALUES (%s, %s) """
            recordTuple = (user_var, pass_var,)
            self.cur.execute(mySql_insert_query, recordTuple)
            self.conn.commit()
            ms.showinfo("Sucess!!","Registration Complete")
            self.admin_reg_win.destroy()
            #self.username_inputr.set("")
            #self.reg_number.set("")
            #self.class_input.set("")
            #self.books.set("")
            #self.admin_reg_window()
            print("Record inserted successfully into Laptop table")
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
            self.conn.close()

#--------------------------------this is the login window----------------------------------------------------------
    def login_win(self):
        self.master.withdraw()
        self.login_window = Toplevel(root)
        self.login_window.geometry("500x500")
        self.login_window.title("LOGIN")
        Label(self.login_window, text = "PLEASE INPUT YOUR LOGIN DETAILS", bg = "blue", width = "300", height = "2", font=("calibri", 13)).pack()
        Label(self.login_window, text = "USERNAME*", width = "300", height = "2", font=("calibri", 13)).pack()
        Entry(self.login_window, width=50, textvariable=self.username_login_input).pack()
        Label(self.login_window, text = "PASSWORD*", width = "300", height = "2", font=("calibri", 13)).pack()
        password_e = Entry(self.login_window, width=50, textvariable=self.password_login_input)
        password_e.config(show="*")
        password_e.pack()
        Button(self.login_window, text="LOGIN", command=self.login_check_fuc).pack(pady = "15")

#-------------------------------------------closes all window------------------------------------------------
    def close_all_windows(self):
        self.master.destroy()

#----------validation for login details
    def login_check_fuc(self):
            pass_var = self.password_login_input.get()
            user_var = self.username_login_input.get()
            
            self.conn = mysql.connector.connect(
                host="localhost", user="root", passwd="", db="project_tables")
            self.cur = self.conn.cursor()
            mySql_insert_query = "SELECT Name FROM admin WHERE Name=%s"
            recordTuple = (user_var,)
            self.cur.execute(mySql_insert_query, recordTuple)
            self.name_records = self.cur.fetchall()
            self.conn.commit()
            self.conn.close()
            print(self.name_records)
            
            self.conn = mysql.connector.connect(
             host="localhost", user="root", passwd="", db="project_tables")
            self.curp = self.conn.cursor()
            mySql_insert_query = "SELECT password FROM admin WHERE password=%s"
            recordTuple = (pass_var,)
            self.curp.execute(mySql_insert_query, recordTuple)
            self.pass_cup = self.curp.fetchall()
            self.conn.commit()
            self.conn.close()
            print(self.pass_cup) 
            
            if (user_var == ""):
                ms.showerror("WARNING!!","Please The Username Input Should Not be Empty")
            elif (pass_var == ""):
                 ms.showerror("WARNING!!","please the password input should not be empty")
            elif (user_var == pass_var):
                ms.showerror("WARNING!!","The username and the password can not be the same")
            elif (self.name_records == []):
                ms.showerror("WARNING!!","Invalid User Name or User Dont Exist")
            elif (self.pass_cup == []):
                ms.showerror("WARNING!!","Invalid Password")
            else:
                self.login_window.destroy()
                self.books_win()
                ms.showinfo("SUCESS!!","WELCOME ADMIN")
                 
    def open_close(self):
        self.admin__window()
        self.books_window.destroy()

#------------------------------------------------BORROWERS SECTION-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------borrower's section---------------------------------------------------
    def borrowers_window(self):
            self.borrowers_win = Toplevel(root)
            logo_img = PhotoImage(file = 'C:\\Users\\starprince\\Desktop\\main project\\images\\bookk.png')
            logo_img.image = logo_img
            Label(self.borrowers_win, image=logo_img).place(x=0, y=0)
            background_img = PhotoImage(file = 'C:\\Users\\starprince\\Desktop\\main project\\images\\LOGO2.png')
            background_img.image = background_img
            Label(self.borrowers_win, image=background_img).place(x=0, y=0)
            self.borrowers_win.state('zoomed')
            self.borrowers_win.title("BORROWERS SECTION")
            Label(self.borrowers_win, text = "DON BOSCO LIBRARY MANAGEMENT SYSTEM", bg = "coral", font=("Weltron Special Power", 40)).place(x=0, y=0, width = 1368, height=80)
            Label(self.borrowers_win, text = "BORROWER'S SECTION", bg = "ORANGE", font=("Freshman", 20)).place(x=0, y=75, width = 1368, height=38)
        
            #TREEVIEW.......
            self.table1=ttk.Treeview(self.borrowers_win, style="Custom.Treeview", height=150)
            vsb = ttk.Scrollbar(self.borrowers_win, orient="vertical", command=self.table1.yview)
            vsb.place(x=1325, y=150, height=520)
            self.table1.configure(yscrollcommand=vsb.set)
            self.table1.place(x=2, y=150, height=525)
            self.table1["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
            self.table1["show"] = "headings"
            self.table1.column("1", width = 30)
            self.table1.column("2", width = 200)
            self.table1.column("3", width = 180)
            self.table1.column("4", width = 120)
            self.table1.column("5", width = 200)
            self.table1.column("6", width = 170)
            self.table1.column("7", width = 120)
            self.table1.column("8", width = 120)
            self.table1.column("9", width = 180)
            self.table1.column("1", anchor="center")
            self.table1.column("2", anchor="center")
            self.table1.column("3", anchor="center")
            self.table1.column("4", anchor="center")
            self.table1.column("5", anchor="center")
            self.table1.column("6", anchor="center")
            self.table1.column("7", anchor="center")
            self.table1.column("8", anchor="center")
            self.table1.column("9", anchor="center")
            self.table1.heading("1", text="ID")
            self.table1.heading("2", text="BOOK TITLE")
            self.table1.heading("3", text="AUTHOR")
            self.table1.heading("4", text="REF NUMBER")
            self.table1.heading("5", text="BORROWER'S NAME")
            self.table1.heading("6", text="REG NUMBER")
            self.table1.heading("7", text="DATE OF RENT")
            self.table1.heading("8", text="DATE OF EXP")
            self.table1.heading("9", text="BOOK CLASSIFICATION")
            self.button13 = Button(self.borrowers_win, text="ADD", command = self.add_pop_up_window, bg= "green2")
            # self.button14 = Button(self.borrowers_win, text="DELETE", state = DISABLED, command = self.delete_borrowers_info_fuc, bg= "red")
            # self.button15 = Button(self.borrowers_win, text="UPDATE", state = DISABLED, command = self.bow_update_fuc, bg= "yellow")
            #self.button16 = Button(self.borrowers_win, text="NEW ADMIN", command = self.admin_reg_window)
            # self.button17 = Button(self.borrowers_win, text="BOOK SECTION", command = self.close_bow_open_win)
            # self.button18 = Button(self.borrowers_win, bg= "DARKORANGE", text="BACK", command = self.close_b_open_b_win)
            # self.button19 = Button(self.borrowers_win, bg= "khaki1", text="EXPORT DATA", command = self.export_fuc)
            self.button13.place(x=1180, y=700, height=30, width = 150)
            self.table1.bind("<Double-1>", self.bow_sel_fuc)
            self.button_s = Button(self.borrowers_win, command =self.search_fuc_for_borrowers_section, text="SEARCH")
            self.button_s.place(x=1250, y=115, height=30, width = 60)
            self.e3 = Entry(self.borrowers_win, textvariable=self.search_for_borrowers_section)
            self.e3.place(x=935, y=120,  width=300)
            #NAVE AND HOME button.....
            self.testbutton1 = Button(self.borrowers_win, text="BACK", command =self.close_b_open_b_win)
            self.testbutton1.place(x=10, y=115, height=30, width = 100)
            self.testbutton2 = Button(self.borrowers_win, text="HOME BUTTON", command =self.pop_up_window)
            self.testbutton2.place(x=120, y=115, height=30, width = 100)
            self.testbutton3 = Button(self.borrowers_win, text="BOOKS BUTTON", command =self.pop_up_window)
            self.testbutton3.place(x=220, y=115, height=30, width = 100)
            # ------------------------------
            self.borrowers_win.protocol("WM_DELETE_WINDOW", self.close_all_windows)
            if (self.search_for_borrowers_section.get() == ""):
                self.borrowers_show_data_fuc()
            else:
               self.search_fuc_for_borrowers_section()
               
#--------------------------this section closes borrowers section opens books window---------------------              
    def close_bow_open_win(self):
            self.borrowers_win.destroy()
            self.books_win()

#------------------this fuction CLOSES BORROWERS section & OPEN the main libRARY users WINDOW-------------------------
    def close_b_open_b_win(self):
        self.borrowers_win.destroy()
        self.books_win()

#--------------------------clear treeview table FOR BORROWERS SECTION-----------------------------------------
    def clear_table_for_borrowers_section(self):
        self.table1.place_forget()
        x = self.table1.get_children()
        print ('get_children values: ', x ,'\n')
        if x != '()': # checks if there is something in the first row
            for child in x:
                self.table1.delete(child)

#-----------------------------search fuction for borrowers section----------------------------------------
    def search_fuc_for_borrowers_section(self):
        self.clear_table_for_borrowers_section()
        connection = mysql.connector.connect(host='localhost',
                                               database='project_tables',
                                               user='root',
                                               password='') 
        sql_select_Query ="""SELECT * FROM borrowers_table WHERE title_of_book LIKE %s 
                                     OR author LIKE %s OR ref_number LIKE %s OR borrowers_name LIKE %s OR reg_no LIKE %s OR date_of_rent LIKE %s OR date_of_exp LIKE %s"""
                                    ##OR PostalCode LIKE '%".$search."%' 
                                    #OR Country LIKE '%".$search."%'  "
        ser = (self.search_for_borrowers_section.get(), self.search_for_borrowers_section.get(), self.search_for_borrowers_section.get(), self.search_for_borrowers_section.get(), self.search_for_borrowers_section.get(), self.search_for_borrowers_section.get(), self.search_for_borrowers_section.get())
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, ser)
        records = cursor.fetchall()
        connection.close()
        cursor.close()
        if (records):
            print("yess it exit")
            index = iid = 0
            for i in records:
                self.table1.insert("", index, iid, values=i ) 
                index = iid = index + 1
            print  (records)
        else:
            print("noo")
            self.table1.place_forget()
            self.search_for_books.set("")
            self.borrowers_show_data_fuc()
            self.table1.place(x=2, y=150, height=550)
            ms.showwarning("SEARCH ERROR!!","Search not found")
        self.table1.place(x=2, y=150, height=550)

#------------------the fuction below displays BORROWERS INFO data frm the data base--------
    def borrowers_show_data_fuc(self):
        connection = mysql.connector.connect(host='localhost',
                                               database='project_tables',
                                               user='root',
                                               password='') 
        sql_select_Query = "select * from borrowers_table"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()    
        connection.close()
        cursor.close()
        index = iid = 0  
        for i in records:
            self.table1.insert("", index, iid, values=i ) 
            index = iid = index + 1

#--------------------select fuction for borrowers section------------------------
    def bow_sel_fuc(self, event):
        if (self.table1.selection() == ()):
            print("yess its emty")
        else:
            for selection in self.table1.selection():
              item = self.table1.item(selection)
              last_name = item["values"][0:1]
              text = "{}"
              call = (text.format(last_name))
              w = call
              w = w.replace("[", "")
              w = w.replace("]", "")
              self.conn1 = mysql.connector.connect(
                         host="localhost", user="root", passwd="", db="project_tables")
              self.curp = self.conn1.cursor()
              mySql_insert_query = "SELECT * FROM borrowers_table WHERE id=%s"
              rect = (w,)
              self.curp.execute(mySql_insert_query, rect)
              self.fetchquery = self.curp.fetchall()
              self.conn1.commit()
              self.conn1.close()
            for self.rec in self.fetchquery:
                self.u_s_id = self.rec[0]
                title_of_book = self.rec[1]
                author =  self.rec[2]
                ref_number = self.rec[3]
                borrowers_name =  self.rec[4]
                reg_no = self.rec[5]
                date_of_rent = self.rec[6]
                date_of_exp =  self.rec[7]

                self.pop_up_window()
                self.u_title_of_book.set(title_of_book)
                self.u_author.set(author)
                self.u_ref_number.set(ref_number)
                self.u_borrowers_name.set(borrowers_name)
                self.u_reg_no.set(reg_no)
                self.u_date_of_rent.set(date_of_rent)
                self.u_date_of_exp.set(date_of_exp)

#------------------this is the BORROWERS update fuction below------------------------
    def bow_update_fuc(self):
        update_book_classificaation_var = self.options1.get()
        title_of_book = self.u_title_of_book.get()
        author = self.u_author.get()
        ref_number = self.u_ref_number.get()
        borrowers_name = self.u_borrowers_name.get()
        reg_no = self.u_reg_no.get()
        date_of_rent = self.date_rent_sel
        date_of_exp = self.date_put
        id = self.u_s_id
        mydb = mysql.connector.connect(host='localhost',
                                         database='project_tables',
                                         user='root',
                                         password='')
        mycursor = mydb.cursor()        
        sql = "UPDATE borrowers_table SET title_of_book = %s, author = %s, ref_number = %s, borrowers_name = %s, reg_no = %s, date_of_rent = %s, date_of_exp = %s, book_classification = %s WHERE id = %s"
        recordTuple = (title_of_book,author,ref_number,borrowers_name,reg_no,date_of_rent,date_of_exp,update_book_classificaation_var,id,)
        mycursor.execute(sql, recordTuple)        
        mydb.commit()
        self.table1.place_forget()
        self.u_title_of_book.set("")
        self.u_author.set("")
        self.u_ref_number.set("")
        self.u_borrowers_name.set("")
        self.u_reg_no.set("")
        self.u_date_of_rent.set("")
        self.u_date_of_exp.set("")
        self.pop_up_win.destroy()
        self.clear_table_for_borrowers_section()
        self.table1.place(x=2, y=150, height=550)
        self.borrowers_show_data_fuc()
        ms.showinfo("SUCESS!!","UPDATE SUCESSFUL")
        
        print(mycursor.rowcount, "record(s) affected")

#------------------this is the insert fuction for BORROWERS section----------
    def insert_fuc_for_borr(self):
        
        update_book_classificaation_var = self.options.get()
        title_of_book = self.title_of_book.get()
        self.title_of_book.get()
        print(title_of_book)
        author = self.author.get()
        ref_number = self.ref_number.get()
        borrowers_name = self.borrowers_name.get()
        reg_no = self.reg_no.get()
        try:
            date_of_rent = self.date_of_rent_add_selector_var
            date_of_exp = self.date_of_exp_add_sel_var   
            conn = mysql.connector.connect(host="localhost", user="root", passwd="", db="project_tables")
            curp = conn.cursor()
            mySql_insert_query = "SELECT title FROM books WHERE title=%s"
            recordTuple = (title_of_book,)
            curp.execute(mySql_insert_query, recordTuple)
            pass_cup = curp.fetchall()
            conn.commit()
            conn.close()
            print(pass_cup) 
            if (pass_cup == []):
                ms.showerror("WARNING!!","BOOK DONT EXIST")
            else:
                # ms.showinfo("SUCESS!!","title ADMIN")
                if (title_of_book == "" or author == "" or ref_number == "" or borrowers_name == "" or reg_no == ""):
                    ms.showerror("ERROR!!","PLEASE FILL OUT ALL THE INPUTS")
                else:
                    mydb = mysql.connector.connect(host='localhost',
                                             database='project_tables',
                                             user='root',
                                             password='')
                    mycursor = mydb.cursor()        
                    sql = "UPDATE books SET total_books = total_books - 1 WHERE title = %s"
                    recordTuple = (title_of_book,)
                    mycursor.execute(sql, recordTuple)        
                    mydb.commit()
                    try:
                        self.conn = mysql.connector.connect(
                            host="localhost", user="root", passwd="", db="project_tables")
                        self.cur = self.conn.cursor()
                        mySql_insert_query = """INSERT INTO borrowers_table (title_of_book, author, ref_number, borrowers_name, reg_no, date_of_rent, date_of_exp, book_classification)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
                        recordTuple = (title_of_book, author, ref_number, borrowers_name,reg_no, date_of_rent, date_of_exp, update_book_classificaation_var)
                        self.cur.execute(mySql_insert_query, recordTuple)
                        self.conn.commit()
                        self.table1.place_forget()
                        self.title_of_book.set("")
                        self.author.set("")
                        self.ref_number.set("")
                        self.borrowers_name.set("")
                        self.reg_no.set("")
                        self.date_of_rent.set("")
                        self.date_of_exp.set("")
                        self.clear_table_for_borrowers_section()
                        self.table1.place(x=2, y=150, height=550)
                        self.borrowers_show_data_fuc()
                        self.add_pop_up_win.destroy()
                        ms.showinfo("Success!!","ADD SUCCESSFUL")
                        print("Record inserted successfully into Laptop table")
                    except mysql.connector.Error as error:
                        print("Failed to insert into MySQL table {}".format(error))
                        self.conn.close()
        except:
            ms.showerror("WARNING!!","PLEASE SELECT AND CHOSE BOTH DATE OF RENT AND EXP DATE")
            
#---------------------------delete fuction for borrowers info---------------------------------
    def delete_borrowers_info_fuc(self):
            mydb = mysql.connector.connect(host='localhost',
                                                   database='project_tables',
                                                   user='root',
                                                   password='') 
            mycursor = mydb.cursor()
            sql = "DELETE FROM borrowers_table WHERE id = %s"
            recordTuple = (self.u_s_id,)
            mycursor.execute(sql, recordTuple)
            mydb.commit()
            ms.showinfo("SUCESS!!","DELETE SUCESSFUL")
            self.borrowers_win.destroy()
            self.u_title_of_book.set("")
            self.u_author.set("")
            self.u_ref_number.set("")
            self.u_borrowers_name.set("")
            self.u_reg_no.set("")
            self.u_date_of_rent.set("")
            self.u_date_of_exp.set("")
            self.pop_up_win.destroy()
            self.borrowers_window()
            print(mycursor.rowcount, "record(s) affected")

# ------------------------------------------popup add info window for borrowers information------------------------------
    def add_pop_up_window(self):
            try:
                pop_up_win.winfo_exist()
                # self.add_pop_up_wind.withdraw()
                #self.pop_up_window()
                
            except:
                self.add_pop_up_win = Toplevel(root)
                self.add_pop_up_win.geometry("500x250")
                self.add_pop_up_win.title("ADD BORROWERS INFORMATION")
                frame1 = Frame(self.add_pop_up_win)
                frame1.pack(fill=X)
                lbl1 = Label(frame1, text="AUTHOR")
                lbl1.pack(side=LEFT, padx=5, pady=5)
                entry1 = Entry(frame1, textvariable=self.author, bg = "gray84")
                entry1.pack(fill=X, padx=5, expand=True)
                #entry1.insert(0, "Place Holder")
                frame2 = Frame(self.add_pop_up_win)
                frame2.pack(fill=X)
                lbl2 = Label(frame2, text="BORROWER'S NAME")
                lbl2.pack(side=LEFT, padx=5, pady=5)
                entry2 = Entry(frame2, textvariable=self.borrowers_name, bg = "gray84")
                entry2.pack(fill=X, padx=5, expand=True)
                frame3 = Frame(self.add_pop_up_win)
                frame3.pack(fill=X)
                lbl3 = Label(frame3, text="TITILE",)
                lbl3.pack(side=LEFT, padx=5, pady=5)
                entry3 = Entry(frame3, textvariable=self.title_of_book, bg = "gray84")
                entry3.pack(fill=X, padx=5, expand=True)
                
                frame4 = Frame(self.add_pop_up_win)
                frame4.pack(fill=X)
        
                lbl4 = Label(frame4, text="REG NUMBER")
                lbl4.pack(side=LEFT, padx=5, pady=5)
        
                entry4 = Entry(frame4, textvariable=self.reg_no, bg = "gray84")
                entry4.pack(fill=X, padx=5, expand=True)
                
                frame5 = Frame(self.add_pop_up_win)
                frame5.pack(fill=X)
        
                lbl5 = Label(frame5, text="REF NUMBER")
                lbl5.pack(side=LEFT, padx=5, pady=5,)
        
                entry5 = Entry(frame5, textvariable=self.ref_number, bg = "gray84")
                entry5.pack(fill=X, padx=5, expand=True)
                
                
                frame7 = Frame(self.add_pop_up_win)
                frame7.pack(fill=X)
                
                
                date_button = Button(frame7, text="DATE OF RENT", command=self.date_of_rent_add_selector)
                date_button.pack(side=LEFT, padx=30, pady=5)
                
                self.options = StringVar(frame7)
                self.options.set("BOOK CLASSIFICATION") # default value
                om1 = OptionMenu(frame7, self.options, "GENERAL WORKES(000-099)", "PHILOSOPHY(100-199)", "RELIGION(200-299)", "SOCIAL SCIENCES(300-399)", "LANGUAGE(400-499)", "NATURAL SCIENCE(500-599)", "ARTS(600-699)", "LITERATURE(800-899)", "HISTORY(900-999)")
                om1.pack(side=LEFT, padx=5, pady=5)
                
                date_button = Button(frame7, text="DATE OF EXP", command=self.date_of_exp_add_selector)
                date_button.pack(pady=5, padx=5,)
                
                frame8 = Frame(self.add_pop_up_win)
                frame8.pack(fill=X)
                
                
                button = Button(frame8, text="ADD", width=10, command = self.insert_fuc_for_borr, bg= "green")
                button.pack(side=RIGHT, padx=50, pady=5)
                              
#------------------------------DATE OF RENT CALENDER SELECTOR ADD FOR BORROWERS------------------------------------
    def date_of_rent_add_selector(self):
            def print_sel():
                self.date_of_rent_add_selector_var = cal.selection_get()
                print(cal.selection_get())
                self.date_of_rent_add_sel.destroy()
            
            self.date_of_rent_add_sel = Toplevel(root)
            cal = Calendar(self.date_of_rent_add_sel, font="Arial 14", selectmode='day', cursor="hand1", year=2020, month=2, day=5)
            cal.pack(fill="both", expand=True)
            cal.selection_set(datetime.datetime.now())
            button = Button(self.date_of_rent_add_sel, text="ok", width=6, command=print_sel)
            button.pack()
            
    def date_of_exp_add_selector(self):
            def print_sel():
                self.date_of_exp_add_sel_var = cal.selection_get()
                print(cal.selection_get())
                self.date_of_exp_add_sel.destroy()
            
            self.date_of_exp_add_sel = Toplevel(root)
            cal = Calendar(self.date_of_exp_add_sel, font="Arial 14", selectmode='day', cursor="hand1", year=2020, month=2, day=5)
            cal.pack(fill="both", expand=True)
            cal.selection_set(datetime.datetime.now())
            button = Button(self.date_of_exp_add_sel, text="ok", width=6, command=print_sel)
            button.pack()

#---------------------------popo up window for borrowers update -------------------------------------------        
    def pop_up_window(self):
        try:
            #pop_up_win.winfo_exist()
            self.pop_up_win.withdraw()
            self.pop_up_window()
        except:
            self.pop_up_win = Toplevel(root)
            self.pop_up_win.geometry("500x250")
            self.pop_up_win.title("UPDATE BORROWERS INFORMATION")
            frame1 = Frame(self.pop_up_win)
            frame1.pack(fill=X)
            lbl1 = Label(frame1, text="AUTHOR")
            lbl1.pack(side=LEFT, padx=5, pady=5)
            entry1 = Entry(frame1, textvariable=self.u_author, bg = "gray84")
            entry1.pack(fill=X, padx=5, expand=True)
            #entry1.insert(0, "Place Holder")
            frame2 = Frame(self.pop_up_win)
            frame2.pack(fill=X)
            lbl2 = Label(frame2, text="BORROWER'S NAME")
            lbl2.pack(side=LEFT, padx=5, pady=5)
            entry2 = Entry(frame2, textvariable=self.u_borrowers_name, bg = "gray84")
            entry2.pack(fill=X, padx=5, expand=True)
            frame3 = Frame(self.pop_up_win)
            frame3.pack(fill=X)
            lbl3 = Label(frame3, text="TITILE",)
            lbl3.pack(side=LEFT, padx=5, pady=5)
            entry3 = Entry(frame3, textvariable=self.u_title_of_book, bg = "gray84")
            entry3.pack(fill=X, padx=5, expand=True)
            
            frame4 = Frame(self.pop_up_win)
            frame4.pack(fill=X)
    
            lbl4 = Label(frame4, text="REG NUMBER")
            lbl4.pack(side=LEFT, padx=5, pady=5)
    
            entry4 = Entry(frame4, textvariable=self.u_reg_no, bg = "gray84")
            entry4.pack(fill=X, padx=5, expand=True)
            
            frame5 = Frame(self.pop_up_win)
            frame5.pack(fill=X)
    
            lbl5 = Label(frame5, text="REF NUMBER")
            lbl5.pack(side=LEFT, padx=5, pady=5,)
    
            entry5 = Entry(frame5, textvariable=self.u_ref_number, bg = "gray84")
            entry5.pack(fill=X, padx=5, expand=True)
            
            
            frame7 = Frame(self.pop_up_win)
            frame7.pack(fill=X)
            
            
            date_button = Button(frame7, text="DATE OF RENT", command=self.date_selector)
            date_button.pack(side=LEFT, padx=30, pady=5)
            
            self.options1 = StringVar(frame7)
            self.options1.set("CHOSE A BOOK CLASSIFICATION") # default value
            om1 = OptionMenu(frame7, self.options1, "GENERAL WORKES(000-099)", "PHILOSOPHY(100-199)", "RELIGION(200-299)", "SOCIAL SCIENCES(300-399)", "LANGUAGE(400-499)", "NATURAL SCIENCE(500-599)", "ARTS(600-699)", "LITERATURE(800-899)", "HISTORY(900-999)")
            om1.pack(side=LEFT, padx=5, pady=5)
            
            
            
            date_button = Button(frame7, text="DATE OF EXP", command=self.exp_date_selector)
            date_button.pack(pady=5, padx=5,)
            
            frame8 = Frame(self.pop_up_win)
            frame8.pack(fill=X)
            
            
            button = Button(frame8, text="DELETE", width=10, command = self.delete_borrowers_info_fuc, bg= "red")
            button.pack(side=RIGHT, padx=50, pady=5)
    
            button = Button(frame8, text="UPDATE", width=10, command = self.bow_update_fuc, bg= "yellow")
            button.pack(side=RIGHT, padx=1, pady=5)
            
            conn1 = mysql.connector.connect(
                             host="localhost", user="root", passwd="", db="project_tables")
            curp = conn1.cursor()
            mySql_insert_query = "SELECT * FROM borrowers_table WHERE id=%s"
            rect = (self.u_s_id,)
            curp.execute(mySql_insert_query, rect)
            fetchquery = curp.fetchall()
            conn1.commit()
            conn1.close()
            for rec in fetchquery:
                date_rent_sel = rec[6]
                date_of_exp = rec[7]
                book_clsss = rec[8]
                
            print(book_clsss)
            self.options1.set(book_clsss)
            self.date_rent_sel = date_rent_sel
            self.date_put = date_of_exp

#-----------------------------calender date of rent selector popup to update borrowers info------------------------------
    def date_selector(self):
        
        def print_sel():
            self.date_rent_sel = cal.selection_get()
            print(cal.selection_get())
            self.date_select.destroy()
        
        self.date_select = Toplevel(root)
        cal = Calendar(self.date_select, font="Arial 14", selectmode='day', cursor="hand1", year=2020, month=2, day=5)
        cal.pack(fill="both", expand=True)
        conn1 = mysql.connector.connect(
                         host="localhost", user="root", passwd="", db="project_tables")
        curp = conn1.cursor()
        mySql_insert_query = "SELECT * FROM borrowers_table WHERE id=%s"
        rect = (self.u_s_id,)
        curp.execute(mySql_insert_query, rect)
        fetchquery = curp.fetchall()
        conn1.commit()
        conn1.close()
        for rec in fetchquery:
            date_rent_sel = rec[6]
        #x = date_of_rent.replace("-", "/")
        #cal.selection_set(x)
        #print(date_of_rent)
        self.date_rent_sel = date_rent_sel
        cal.selection_set(self.date_rent_sel)
        
        button = Button(self.date_select, text="ok", width=6, command=print_sel)
        button.pack()

#-----------------------------calender date of exp selector popup to update borrowers info------------------------------
    def exp_date_selector(self):
        
        def print_sel():  
            self.date_put = cal.selection_get()
            print(cal.selection_get())
            self.exp_date_sel.destroy()
        
        self.exp_date_sel = Toplevel(root)
        cal = Calendar(self.exp_date_sel, font="Arial 14", selectmode='day', cursor="hand1", year=2020, month=2, day=5)
        cal.pack(fill="both", expand=True)
        conn1 = mysql.connector.connect(
                         host="localhost", user="root", passwd="", db="project_tables")
        curp = conn1.cursor()
        mySql_insert_query = "SELECT * FROM borrowers_table WHERE id=%s"
        rect = (self.u_s_id,)
        curp.execute(mySql_insert_query, rect)
        fetchquery = curp.fetchall()
        conn1.commit()
        conn1.close()
        for rec in fetchquery:
            date_of_exp = rec[7]
        self.date_put = date_of_exp
        #print(self.date_put)
        cal.selection_set(self.date_put)
        button = Button(self.exp_date_sel, text="ok", width=6, command=print_sel)
        button.pack()
#---------------------------------------------END OF BORROWERS SECTION---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------LIBRARY REGISTERED USE SECTIN-----------------------------------------------------------------------------------------------------------------------------------------------

#---------------main admin window  and library registed user-----------------
    def admin__window(self):
        self.admin_win = Toplevel(root)
        #logo_img = PhotoImage(file = 'C:\\Users\\starprince\\Desktop\\main project\\images\\bookk.png')
        #logo_img.image = logo_img
        #Label(self.admin_win, image=logo_img).place(x=0, y=0)
        #background_img = PhotoImage(file = 'C:\\Users\\starprince\\Desktop\\main project\\images\\LOGO2.png')
        #background_img.image = background_img
        #Label(self.admin_win, image=background_img).place(x=0, y=0)
        self.admin_win.state('zoomed')
        self.admin_win.title("ADMIN")
        Label(self.admin_win, text = "DON BOSCO LIBRARY MANAGEMENT SYSTEM", bg = "coral", font=("Weltron Special Power", 40)).place(x=0, y=0, width = 1370, height=80)
        Label(self.admin_win, text = "WELCOME ADMIN", bg = "ORANGE", font=("Freshman", 20)).place(x=0, y=75, width = 1370, height=38)
        Label(self.admin_win,bg = "light sky blue2", borderwidth=4, relief="groove").place(x=875, y=150, width = 470, height=400)
        Label(self.admin_win,bg = "light sky blue2", borderwidth=4, relief="groove").place(x=875, y=565, width = 470, height=125)
        #TREEVIEW.......
        self.table=ttk.Treeview(self.admin_win, style="Custom.Treeview", height=150)
        vsb = ttk.Scrollbar(self.admin_win, orient="vertical", command=self.table.yview)
        vsb.place(x=853, y=150, height=550)
        self.table.configure(yscrollcommand=vsb.set)
        self.table.place(x=2, y=150, height=550)
        self.table["columns"] = ("1", "2", "3", "4", "5", "6")
        self.table["show"] = "headings"
        self.table.column("1", width = 20)
        self.table.column("2", width = 220)
        self.table.column("3", width = 150)
        self.table.column("4", width = 200)
        self.table.column("5", width = 155)
        self.table.column("6", width = 110)
        self.table.column("1", anchor="center")
        self.table.column("2", anchor="center")
        self.table.column("3", anchor="center")
        self.table.column("4", anchor="center")
        self.table.column("5", anchor="center")
        self.table.column("6", anchor="center")
        self.table.heading("1", text="ID")
        self.table.heading("2", text="FULL NAME")
        self.table.heading("3", text="REG NUMBER")
        self.table.heading("4", text="ADDRESS")
        self.table.heading("5", text="TELEPHONE")
        self.table.heading("6", text="EXP DATE")
        self.button5 = Button(self.admin_win, text="REGISTER", bg= "green2", command = self.insert_registration_fuc)
        self.button6 = Button(self.admin_win, text="DELETE", state = DISABLED, bg= "red", command = self.delete_fuc)
        self.button7 = Button(self.admin_win, text="UPDATE", state = DISABLED, bg= "yellow", command = self.library_users_update_fuc)
        self.button8 = Button(self.admin_win, text="NEW ADMIN", command = self.admin_reg_window)
        self.button9 = Button(self.admin_win, text="BOOK SECTION", command = self.open_close_win)
        #self.button10 = Button(self.admin_win, text="GUEST SECTION", command = self.borrowers_window)
        self.button11 = Button(self.admin_win, bg= "khaki1", text="EXPORT DATA", command = self.library_export_fuc)
        self.button12 = Button(self.admin_win, text="BORROWER'S SECTION", command = self.borrowers_window)
        self.button5.place(x=885, y=320, height=30, width = 200)
        self.button6.place(x=1135, y=500, height=30, width = 200)
        self.button7.place(x=885, y=500, height=30, width = 200)
        self.button8.place(x=1135, y=575, height=30, width = 200)
        self.button9.place(x=885, y=575, height=30, width = 200)
        #self.button10.place(x=885, y=650, height=30, width = 200)
        self.button11.place(x=1135, y=650, height=30, width = 200)
        self.button12.place(x=885, y=650, height=30, width = 200)
        #RISTER LABEL....
        Label(self.admin_win,text = "NAME :").place(x=885, y=170)
        Label(self.admin_win,text = "REG NUMBER :",).place(x=885, y=199)
        Label(self.admin_win,text = "ADDRESS :").place(x=885, y=228)
        Label(self.admin_win,text = "TELEPHONE :",).place(x=885, y=257)
        Label(self.admin_win,text = "EXP DATE :",).place(x=885, y=286)
        #UPDATE AND DELETE LABEL...
        Label(self.admin_win,text = "NAME :").place(x=885, y=358)
        Label(self.admin_win,text = "REG NUMBER :",).place(x=885, y=387)
        Label(self.admin_win,text = "ADDRESS :").place(x=885, y=416)
        Label(self.admin_win,text = "TELEPHONE :").place(x=885, y=445)
        Label(self.admin_win,text = "EXP DATE :").place(x=885, y=474)
        self.table.bind("<Double-1>", self.onclick)
        #SEARCH BUTTON AND ENTRY-------------
        self.button22 = Button(self.admin_win, command =self.search_fuc, text="SEARCH")
        self.button22.place(x=1250, y=115, height=30, width = 60)
        self.e1 = Entry(self.admin_win, textvariable=self.search)
        self.e1.place(x=935, y=120,  width=300)
        #RISTER ENTRY....
        Entry(self.admin_win, textvariable=self.user_name).place(x=935, y=170,  width=400)
        Entry(self.admin_win, textvariable=self.reg_number).place(x=974, y=199, width=361)
        Entry(self.admin_win, textvariable=self.address).place(x=950, y=228, width=384)
        Entry(self.admin_win, textvariable=self.telephone).place(x=966, y=257, width=370)
        Entry(self.admin_win, textvariable=self.expiring_date).place(x=952, y=286, width=384)
        #UPDATE AND DELETE ENTRY.....
        Entry(self.admin_win, textvariable=self.u_user_name).place(x=935, y=358,  width=400)
        Entry(self.admin_win, textvariable=self.u_reg_number).place(x=974, y=387, width=361)
        Entry(self.admin_win, textvariable=self.u_address).place(x=950, y=416, width=384)
        Entry(self.admin_win, textvariable=self.u_telephone).place(x=966, y=445, width=370)
        Entry(self.admin_win, textvariable=self.u_expiring_date).place(x=952, y=474, width=384)
        self.admin_win.protocol("WM_DELETE_WINDOW", self.close_all_windows)
        #test button.....
        self.testbutton = Button(self.admin_win, text="pop up", command =self.pop_up_window)
        self.testbutton.place(x=10, y=115, height=30, width = 100)
        #self.admin_show_data_fuc()
        #self.hold = "web"
        if (self.search.get() == ""):
            self.admin_show_data_fuc()
            #self.table.after(3000, self.test1)
            #self.table.after(6000, self.test2)
        else:
            self.search_fuc()
            
#------------------this fuction open book section & closes the main libRARY users WINDOW-------------------------
    def open_close_win(self):
        self.admin_win.destroy()
        self.books_win()

#-----------------clear treeview table FOR REGISTERED USERS-----------------------------------------
    def clear_table_treeview(self):
        self.table.place_forget()
        x = self.table.get_children()
        print ('get_children values: ', x ,'\n')
        if x != '()': # checks if there is something in the first row
            for child in x:
                self.table.delete(child)

#------------------------------------search fuction for library student users-------------------------------------
    def search_fuc(self):
        self.clear_table_treeview()
        connection = mysql.connector.connect(host='localhost',
                                               database='project_tables',
                                               user='root',
                                               password='') 
        sql_select_Query ="""SELECT * FROM library_users WHERE address LIKE %s 
                                     OR user_name LIKE %s OR reg_number LIKE %s OR telephone LIKE %s OR expiring_date LIKE %s"""
                                    ##OR PostalCode LIKE '%".$search."%' 
                                    #OR Country LIKE '%".$search."%'  "
        ser = (self.search.get(), self.search.get(), self.search.get(), self.search.get(), self.search.get())
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, ser)
        records = cursor.fetchall()
        connection.close()
        cursor.close()
        if (records):
            print("yess it exit")
            index = iid = 0
            for i in records:
                self.table.insert("", index, iid, values=i ) 
                index = iid = index + 1
            print  (records)
        else:
            print("noo")
            self.table.place_forget()
            self.search.set("")
            self.admin_show_data_fuc()
            self.table.place(x=2, y=150, height=550)
            ms.showwarning("SEARCH ERROR!!","Search not found")
        self.table.place(x=2, y=150, height=550)

#---------------the fuction below displays library registed user data frm the data base--------
    def admin_show_data_fuc(self):
        connection = mysql.connector.connect(host='localhost',
                                               database='project_tables',
                                               user='root',
                                               password='') 
        sql_select_Query = "select * from library_users"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        connection.close()
        cursor.close()
        index = iid = 0
        for i in records:
            self.sell = self.table.insert("", index, iid, values=i )
            index = iid = index + 1    
        #self.table.delete(i)
        #self.sell = self.table.get_children()
        #print ('get_children values: ', self.sell ,'\n')
        #self.sell.delete(i)

#---------------prints out selected info frm the library resgisterd user treeview-----------
    def onclick(self, event):
        if (self.table.selection() == ()):
            print("yess its emty")
        else:
            for selection in self.table.selection():
              item = self.table.item(selection)
              last_name = item["values"][0:1]
              text = "{}"
              call = (text.format(last_name))
              w = call
              w = w.replace("[", "")
              w = w.replace("]", "")
              self.conn1 = mysql.connector.connect(
                         host="localhost", user="root", passwd="", db="project_tables")
              self.curp = self.conn1.cursor()
              mySql_insert_query = "SELECT * FROM library_users WHERE id=%s"
              rect = (w,)
              self.curp.execute(mySql_insert_query, rect)
              self.fetchquery = self.curp.fetchall()
              self.conn1.commit()
              self.conn1.close()
            for self.rec in self.fetchquery:
                self.u_id = self.rec[0]
                user_name = self.rec[1]
                reg_number =  self.rec[2]
                address = self.rec[3]
                telephone =  self.rec[4]
                self.expiring_date = self.rec[5]
                x = expiring_date.replace("-", "/")
                print(x)


                self.u_user_name.set(user_name)
                self.u_reg_number.set(reg_number)
                self.u_address.set(address)
                self.u_telephone.set(telephone)
                self.u_expiring_date.set(expiring_date)
                self.button6["state"] = NORMAL
                self.button7["state"] = NORMAL

#---------------------------------delete fuction for student library users---------------------------
    def delete_fuc(self):
        id = self.u_id
        mydb = mysql.connector.connect(host='localhost',
                                               database='project_tables',
                                               user='root',
                                               password='') 
        mycursor = mydb.cursor()
        sql = "DELETE FROM library_users WHERE id = %s"
        recordTuple = (id,)
        mycursor.execute(sql, recordTuple)     
        mydb.commit()
        ms.showinfo("SUCESS!!","DELETE SUCESSFUL")
        self.table.place_forget()
        self.u_user_name.set("")
        self.u_reg_number.set("")
        self.u_address.set("")
        self.u_telephone.set("")
        self.u_expiring_date.set("")
        self.search.set("")
        self.clear_table_treeview()
        self.admin_show_data_fuc()
        self.table.place(x=2, y=150, height=550)
        print(mycursor.rowcount, "record(s) affected")

#----------------this is the insert fuction for reg  library users----------
    def insert_registration_fuc(self):
        user_name = self.user_name.get()
        reg_number = self.reg_number.get()
        address = self.address.get()
        telephone = self.telephone.get()
        expiring_date = self.expiring_date.get()
        if (user_name == "" or reg_number == "" or address == "" or telephone == "" or expiring_date == ""):
            ms.showerror("ERROR!!","PLEASE FILL OUT ALL THE INPUTS")
        else:
            try:
                startdate = datetime.strptime(expiring_date, '%Y-%m-%d')
            except:
                ms.showerror("ERROR!!","Wrong datetime format, must be YYYY-MM-DD")
                print('Wrong datetime format, must be YYYY-MM-DD')
            else:
                print("iirht date")
                try:
                    self.conn = mysql.connector.connect(
                        host="localhost", user="root", passwd="", db="project_tables")
                    self.cur = self.conn.cursor()
                    mySql_insert_query = """INSERT INTO library_users (user_name, reg_number, address, telephone, expiring_date)
                                        VALUES (%s, %s, %s, %s, %s) """
                    recordTuple = (user_name, reg_number, address, telephone,expiring_date)
                    self.cur.execute(mySql_insert_query, recordTuple)
                    self.conn.commit()
                    self.table.place_forget()
                    self.user_name.set("")
                    self.reg_number.set("")
                    self.address.set("")
                    self.telephone.set("")
                    self.expiring_date.set("")
                    self.search.set("")
                    self.clear_table_treeview()
                    self.admin_show_data_fuc()
                    self.table.place(x=2, y=150, height=550)
                    ms.showinfo("Sucess!!","Registration Complete")
                    print("Record inserted successfully into Laptop table")
                except mysql.connector.Error as error:
                    print("Failed to insert into MySQL table {}".format(error))
                    self.conn.close()

#------------------this is the  library student update fuction below------------------------
    def library_users_update_fuc(self):
        user_name = self.u_user_name.get()
        reg_number = self.u_reg_number.get()
        address = self.u_address.get()
        telephone = self.u_telephone.get()
        expiring_date = self.u_expiring_date.get()
        if (user_name == "" or reg_number == "" or address == "" or telephone == "" or expiring_date == ""):
            ms.showerror("ERROR!!","PLEASE FILL OUT ALL THE INPUTS")
        else:
            try:
                startdate = datetime.strptime(expiring_date, '%Y-%m-%d')
            except:
                ms.showerror("ERROR!!","Wrong datetime format, must be YYYY-MM-DD")
                print('Wrong datetime format, must be YYYY-MM-DD')
            else:
                print("iirht date")
                id = self.u_id
                mydb = mysql.connector.connect(host='localhost',
                                                 database='project_tables',
                                                 user='root',
                                                 password='')

                mycursor = mydb.cursor()        

                sql = "UPDATE library_users SET user_name = %s, reg_number = %s, address = %s, telephone = %s, expiring_date = %s WHERE id = %s"
                recordTuple = (user_name,reg_number,address,telephone,expiring_date,id)
                mycursor.execute(sql, recordTuple)        
                mydb.commit()       
                self.table.place_forget()
                self.u_user_name.set("")
                self.u_reg_number.set("")
                self.u_address.set("")
                self.u_telephone.set("")
                self.u_expiring_date.set("")
                self.search.set("")
                self.clear_table_treeview()
                self.admin_show_data_fuc()
                self.table.place(x=2, y=150, height=550)
                self.button6["state"] = DISABLED
                self.button7["state"] = DISABLED
                ms.showinfo("SUCESS!!","UPDATE SUCESSFUL7")
                print(mycursor.rowcount, "record(s) affected")

#-------------------export all libraray users info to ms word fuc-----------------------------
    def library_export_fuc(self):
        connection = mysql.connector.connect(host='localhost',
                                               database='project_tables',
                                               user='root',
                                               password='') 
        sql_select_Query = "select user_name, reg_number, address, telephone, expiring_date from library_users"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        wb = Workbook('ALL_LIBARY_USERS_RECORD.xlsx')
        sheet1 = wb.add_worksheet()
        sheet1.write(0,0,'NAME')
        sheet1.write(0,1,'REG NUMBER')
        sheet1.write(0,2,'ADDRESS')
        sheet1.write(0,3,'TELEPHONE NUM')
        sheet1.write(0,4,'DATE OF EXP')

        row_number = 1
        for row in records:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1
        wb.close()
        ms.showinfo("SUCESS!!","EXPORT SUCESSFUL")

#-------------------------------------------END OF LIBRARY REGISTERED USE SECTIN------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------BOOK SECTION--------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------books management section and main window-----------------------
    def books_win(self):
        self.books_window = Toplevel(root)
        #logo_img = PhotoImage(file = 'C:\\Users\\starprince\\Desktop\\main project\\images\\bookk.png')
        #logo_img.image = logo_img
        #Label(self.books_window, image=logo_img).place(x=0, y=0)
        #background_img = PhotoImage(file = 'C:\\Users\\starprince\\Desktop\\main project\\images\\LOGO2.png')
        #background_img.image = background_img
        #Label(self.books_window, image=background_img).place(x=0, y=0)
        self.books_window.state('zoomed')
        self.books_window.title("BOOKS")
        Label(self.books_window, text = "DON BOSCO BOOKS MANAGEMENT SECTION", bg = "coral", font=("Freshman", 30)).place(x=0, y=0, width = 1500, height=80)
        Label(self.books_window, text = "WELCOME ADMIN", bg = "ORANGE", font=("Freshman", 20)).place(x=0, y=75, width = 1500, height=38)
        # Label(self.books_window, bg = "light sky blue2", borderwidth=2, relief="sunken").place(x=980, y=115, width = 377, height=593)
        self.treev=ttk.Treeview(self.books_window, style="Custom.Treeview", height=150)
        vsb = ttk.Scrollbar(self.books_window, orient="vertical", command=self.treev.yview)
        vsb.place(x=1170, y=150, height=525)
        self.treev.configure(yscrollcommand=vsb.set)
        self.treev.place(x=2, y=150, height=525)
        self.treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        self.treev["show"] = "headings"
        self.treev.column("1", width = 30)
        self.treev.column("2", width = 170)
        self.treev.column("3", width = 150)
        self.treev.column("4", width = 150)
        self.treev.column("5", width = 100)
        self.treev.column("6", width = 120)
        self.treev.column("7", width = 100)
        self.treev.column("8", width = 120)
        self.treev.column("9", width = 120)
        self.treev.column("10", width = 120)
        #self.treev.column("9", width = 90)
        self.treev.column("1", anchor="center")
        self.treev.column("2", anchor="center")
        self.treev.column("3", anchor="center")
        self.treev.column("4", anchor="center")
        self.treev.column("5", anchor="center")
        self.treev.column("6", anchor="center")
        self.treev.column("7", anchor="center")
        self.treev.column("8", anchor="center")
        self.treev.column("9", anchor="center")
        self.treev.column("10", anchor="center")
        #self.treev.column("9", anchor="center")
        self.treev.heading("1", text="ID")
        self.treev.heading("2", text="AUTHOR")
        self.treev.heading("3", text="PUBLISHER")
        self.treev.heading("4", text="TITLE")
        self.treev.heading("5", text="EDITION")
        self.treev.heading("6", text="CLASSIFICATION")
        self.treev.heading("7", text="REF NO")
        self.treev.heading("8", text="PRICE")
        self.treev.heading("9", text="DATE")
        self.treev.heading("10", text="TOTAL BOOKS")

        #reg books labels....
        # Label(self.books_window,text = "AUTHOR :", bg = "light sky blue2", font=("Stretch", 10)).place(x=985, y=120)
        # Label(self.books_window,text = "PUBLISHER :", bg = "light sky blue2", font=("Stretch", 10)).place(x=985, y=149)
        # Label(self.books_window,text = "TITLE :", bg = "light sky blue2", font=("Stretch", 10)).place(x=985, y=178)
        # Label(self.books_window,text = "EDITION :", bg = "light sky blue2", font=("Stretch", 10)).place(x=985, y=207)
        # Label(self.books_window,text = "CLASSIFICATION :", bg = "light sky blue2", font=("Stretch", 10)).place(x=985, y=236)
        # Label(self.books_window,text = "REF NO :", bg = "light sky blue2", font=("Stretch", 10)).place(x=985, y=265)
        # Label(self.books_window,text = "PRICE :", bg = "light sky blue2", font=("Stretch", 10)).place(x=985, y=294)
        # Label(self.books_window,text = "DATE :", bg = "light sky blue2", font=("Stretch", 10)).place(x=985, y=323)
        # #Label(self.books_window,text = "AVALIABLE :", bg = "light sky blue2", font=("Stretch", 10)).place(x=1000, y=352)
        # #BOOKS ADD ENTRY.......
        # Entry(self.books_window, textvariable=self.b_author, bg = "gray84").place(x=1070, y=120,  width=282)
        # Entry(self.books_window, textvariable=self.b_publisher, bg = "gray84").place(x=1070, y=149, width=282)
        # Entry(self.books_window, textvariable=self.b_title, bg = "gray84").place(x=1070, y=178, width=282)
        # Entry(self.books_window, textvariable=self.b_edition, bg = "gray84").place(x=1070, y=207, width=282)
        # Entry(self.books_window, textvariable=self.b_classification, bg = "gray84").place(x=1070, y=236,  width=282)
        # Entry(self.books_window, textvariable=self.b_ref_no, bg = "gray84").place(x=1070, y=265, width=282)
        # Entry(self.books_window, textvariable=self.b_price, bg = "gray84").place(x=1070, y=294, width=282)
        # Entry(self.books_window, textvariable=self.b_date, bg = "gray84").place(x=1070, y=323, width=282)
        # #Entry(self.books_window, textvariable=self.b_status, bg = "gray84").place(x=1070, y=352, width=282)
        self.button1 = Button(self.books_window, text="ADD BOOK",bg= "green2",  command = self.add_popup_book_window)
        # self.button2 = Button(self.books_window, text="UPDATE", bg= "yellow", state = DISABLED, command = self.update_books_fuc)
        # self.button3 = Button(self.books_window, text="DELETE", bg= "red", state = DISABLED, command = self.delete_books_fuc)
        self.button4 = Button(self.books_window, text="ADD NEW ADMIN", bg= "DARKORANGE", command = self.open_close)
        self.button1.place(x=1140, y=700, height=30, width = 200)
        # self.button2.place(x=1005, y=640, height=30, width = 130)
        # self.button3.place(x=1200, y=640, height=30, width = 130)
        self.button4.place(x=750, y=700, height=30, width = 130)
        Button(self.books_window, text="EXPORT DATA", bg= "khaki1", command = self.export_fuc).place(x=920, y=700, height=30, width = 130)
        #SEARCH BUTTON AND ENTRY....................
        self.button22 = Button(self.books_window, command =self.search_books_fuc, text="SEARCH")
        self.button22.place(x=1300, y=115, height=30, width = 60)
        self.e2 = Entry(self.books_window, textvariable=self.search_for_books)
        self.e2.place(x=1000, y=120,  width=300)
        #upadte books labels....
 
        #Label(self.books_window,text = "AVALIABLE :",bg = "light sky blue2", font=("Stretch", 10)).place(x=1000, y=632)
        self.treev.bind("<Double-1>", self.books_print_selection)
        #BOOKS update ENTRY.......

        self.books_window.protocol("WM_DELETE_WINDOW", self.close_all_windows)
        #test button.....
        self.testbutton = Button(self.books_window, text="BORROWERS SECTION", command =self.borrowers_window)
        self.testbutton.place(x=200, y=115, height=30, width = 130)
        self.testbutto = Button(self.books_window, text="STUDENTS SECTION", command =self.admin__window)
        self.testbutto.place(x=10, y=115, height=30, width = 130)
        #Entry(self.books_window, textvariable=self.b_status, bg = "gray84").place(x=1070, y=632, width=282)
        if (self.search_for_books.get() == ""):
            self.show_books_info()
            #self.table.after(3000, self.test1)
            #self.table.after(6000, self.test2)
        else:
            self.search_books_fuc()

#----------------------shoow all books----------
    def show_books_info(self):
        connection = mysql.connector.connect(host='localhost',
                                               database='project_tables',
                                               user='root',
                                               password='') 
        sql_select_Query = "select id,author,publisher,title,edition,classification,ref_no,price,date,total_books from books"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()    
        connection.close()
        cursor.close()
        index = iid = 0  
        for i in records:
            self.treev.insert("", index, iid, values=i ) 
            index = iid = index + 1

#---------------------print section for books---------------
    def books_print_selection(self, event):
        print(self.treev.selection())
        if (self.treev.selection() == ()):
            print("yess its emty")
        else:
            for selection in self.treev.selection():
              item = self.treev.item(selection)
              last_name = item["values"][0:1]
              text = "{}"
              call = (text.format(last_name)) 
              print(call)
              if (call != "0"):
                  print ("no call")
              w = call
              w = w.replace("[", "")
              print(w)
              w = w.replace("]", "")
              print(w)
    
              conn1 = mysql.connector.connect(
                         host="localhost", user="root", passwd="", db="project_tables")
              curp = conn1.cursor()
              mySql_insert_query = "SELECT * FROM books WHERE id=%s"
              rect = (w,)
              curp.execute(mySql_insert_query, rect)
              fetchquery = curp.fetchall()
              conn1.commit()
              conn1.close()
              print(fetchquery)
            for records in fetchquery:
                self.books_id = records[0]
                author = records[1]
                publisher =  records[2]
                title = records[3]
                edition =  records[4]
                classification =  records[5]
                ref_no =  records[6]
                price =  records[7]
                date =  records[8]
                ub_total = records[9]
                
                self.edit_popup_book_window()
                self.ub_author.set(author)
                self.ub_publisher.set(publisher)
                self.ub_title.set(title)
                self.ub_edition.set(edition)
                self.ub_classification.set(classification)
                self.ub_ref_no.set(ref_no)
                self.ub_price.set(price)
                self.ub_date.set(date)
                self.ub_total.set(ub_total)
                self.button2["state"] = NORMAL
                self.button3["state"] = NORMAL

#-----------------------books update fuction-------------------------------------
    def update_books_fuc(self):
        id = self.books_id
        ub_author = self.ub_author.get()
        ub_publisher = self.ub_publisher.get()
        ub_title = self.ub_title.get()
        ub_edition = self.ub_edition.get()
        ub_classification = self.ub_classification.get()
        ub_ref_no = self.ub_ref_no.get()
        ub_total = self.ub_total.get()
        ub_price = self.ub_price.get()
        ub_date = self.book_date
        mydb = mysql.connector.connect(host='localhost',
                                         database='project_tables',
                                         user='root',
                                         password='') 
        mycursor = mydb.cursor()         
        sql = "UPDATE books SET author = %s, publisher = %s, title = %s, edition = %s, classification = %s, ref_no = %s, price = %s, date = %s WHERE id = %s"
        recordTuple = (ub_author,ub_publisher,ub_title,ub_edition,ub_classification,ub_ref_no,ub_price,ub_date,id)
        mycursor.execute(sql, recordTuple)
        mydb.commit()
        ms.showinfo("SUCESS!!","UPDATE SUCESSFUL")
        self.treev.place_forget()
        self.edit_popup_book_win.destroy()
        self.clear_table_for_books()
        self.treev.place(x=2, y=150, height=558)
        self.show_books_info()
        print(mycursor.rowcount, "record(s) affected")

#---------------------delete books fuc......................
    def delete_books_fuc(self):
        if (self.books_id == 0):
            ms.showwarning("WARNING!!","PLEASE SELECT AN INFO TO DELETE")
        else:
            mydb = mysql.connector.connect(host='localhost',
                                                   database='project_tables',
                                                   user='root',
                                                   password='') 
            mycursor = mydb.cursor()
            sql = "DELETE FROM books WHERE id = %s"
            recordTuple = (self.books_id,)
            mycursor.execute(sql, recordTuple)
            mydb.commit()
            ms.showinfo("SUCESS!!","DELETE SUCESSFUL")
            self.treev.place_forget()
            self.ub_author.set("")
            self.ub_publisher.set("")
            self.ub_title.set("")
            self.ub_edition.set("")
            self.ub_classification.set("")
            self.ub_ref_no.set("")
            self.ub_price.set("")
            self.ub_date.set("")
            self.clear_table_for_books()
            self.show_books_info()
            self.treev.place(x=2, y=150, height=558)
            print(mycursor.rowcount, "record(s) affected")

#-----------------insert books into data base fuction----------------------
    def insert_books_fuc(self):
        if (self.b_author.get() == "" or self.b_publisher.get() =="" or self.b_title.get() == "" or
           self.b_edition.get() == "" or self.b_ref_no.get() =="" or self.b_price.get()== ""):
           ms.showerror("ERROR!!","PLEASE FILL OUT ALL THE INPUTS")
        else:
            try:
                b_classification = self.options3.get()
                b_date = self.cal_popup_for_b_add_var
                b_author = self.b_author.get()
                b_publisher = self.b_publisher.get()
                b_title = self.b_title.get()
                b_edition = self.b_edition.get()
                print(b_classification)
                b_ref_no = self.b_ref_no.get()
                b_price = self.b_price.get()
                b_total = self.b_total.get()
                
                conn = mysql.connector.connect(
                        host="localhost", user="root", passwd="", db="project_tables")
                cur = conn.cursor()
                mySql_insert_query = """INSERT INTO books (author, publisher, title, edition, classification, ref_no, price, date, total_books)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
                recordTuple = (b_author, b_publisher, b_title, b_edition, b_classification, b_ref_no, b_price, b_date, b_total,)
                cur.execute(mySql_insert_query, recordTuple)
                conn.commit()
                self.treev.place_forget()
                self.b_author.set("")
                self.b_publisher.set("")
                self.b_title.set("")
                self.b_edition.set("")
                self.b_classification.set("")
                self.b_ref_no.set("")
                self.b_price.set("")
                self.b_date.set("")
                self.search.set("")
                self.clear_table_for_books()
                self.show_books_info()
                self.treev.place(x=2, y=150, height=558)
                ms.showinfo("SUCESS!!","BOOK ADDED SUCCESSFULLY")
                self.master.withdraw()
            except:
                ms.showerror("WARNING!", "PLEASE CHOSE DATE")
           
# -------------------------------------------POPUP FOR ADDING BOOKS WINDOW---------------------------
    def add_popup_book_window(self):
                    self.add_popup_book_win = Toplevel(root)
                    self.add_popup_book_win.geometry("500x300")
                    self.add_popup_book_win.title("ADD BORROWERS INFORMATION")
                    frame1 = Frame(self.add_popup_book_win)
                    frame1.pack(fill=X)
                    lbl1 = Label(frame1, text="AUTHOR")
                    lbl1.pack(side=LEFT, padx=5, pady=5)
                    entry1 = Entry(frame1, textvariable=self.b_author, bg = "gray84")
                    entry1.pack(fill=X, padx=5, expand=True)
                    #entry1.insert(0, "Place Holder")
                    frame2 = Frame(self.add_popup_book_win)
                    frame2.pack(fill=X)
                    lbl2 = Label(frame2, text="PUBLISHER")
                    lbl2.pack(side=LEFT, padx=5, pady=5)
                    entry2 = Entry(frame2, textvariable=self.b_publisher, bg = "gray84")
                    entry2.pack(fill=X, padx=5, expand=True)
                    frame3 = Frame(self.add_popup_book_win)
                    frame3.pack(fill=X)
                    lbl3 = Label(frame3, text="TITILE",)
                    lbl3.pack(side=LEFT, padx=5, pady=5)
                    entry3 = Entry(frame3, textvariable=self.b_title, bg = "gray84")
                    entry3.pack(fill=X, padx=5, expand=True)
                    
                    frame4 = Frame(self.add_popup_book_win)
                    frame4.pack(fill=X)
                    
                    lbl4 = Label(frame4, text="EDITION")
                    lbl4.pack(side=LEFT, padx=5, pady=5)
            
                    entry4 = Entry(frame4, textvariable=self.b_edition, bg = "gray84")
                    entry4.pack(fill=X, padx=5, expand=True)
                    
                    frame5 = Frame(self.add_popup_book_win)
                    frame5.pack(fill=X)
            
                    lbl5 = Label(frame5, text="TOTAL BOOKS")
                    lbl5.pack(side=LEFT, padx=5, pady=5,)
            
                    entry5 = Entry(frame5, textvariable=self.b_total, bg = "gray84")
                    entry5.pack(fill=X, padx=5, expand=True)
                    
                    frame6 = Frame(self.add_popup_book_win)
                    frame6.pack(fill=X)
            
                    lbl6 = Label(frame6, text="REF NUMBER")
                    lbl6.pack(side=LEFT, padx=5, pady=5,)
            
                    entry6 = Entry(frame6, textvariable=self.b_ref_no, bg = "gray84")
                    entry6.pack(fill=X, padx=5, expand=True)
                    
                    frame7 = Frame(self.add_popup_book_win)
                    frame7.pack(fill=X)
            
                    lbl7 = Label(frame7, text="PRICE")
                    lbl7.pack(side=LEFT, padx=5, pady=5,)
            
                    entry7 = Entry(frame7, textvariable=self.b_price, bg = "gray84")
                    entry7.pack(fill=X, padx=5, expand=True)
                    
                    
                    frame8 = Frame(self.add_popup_book_win)
                    frame8.pack(fill=X)
                    
                    
                    date_button = Button(frame8, text="DATE", command=self.cal_popup_for_b_add)
                    date_button.pack(side=LEFT, padx=30, pady=5)
                    
                    self.options3 = StringVar(frame8)
                    self.options3.set("BOOK CLASSIFICATION") # default value
                    om1 = OptionMenu(frame8, self.options3, "GENERAL WORKES(000-099)", "PHILOSOPHY(100-199)", "RELIGION(200-299)", "SOCIAL SCIENCES(300-399)", "LANGUAGE(400-499)", "NATURAL SCIENCE(500-599)", "ARTS(600-699)", "LITERATURE(800-899)", "HISTORY(900-999)")
                    om1.pack(side=RIGHT, padx=5, pady=5)
                
                    
                    frame9 = Frame(self.add_popup_book_win)
                    frame9.pack(fill=X)
                    
                    button = Button(frame9, text="ADD", width=10, command=self.insert_books_fuc, bg= "green")
                    button.pack(side=RIGHT, padx=50, pady=5)
                    
                    
#--------------------------------POPUP WINDOW FOR  EDITING/UPDATING BOOKS ----------------------------------------------
    def edit_popup_book_window(self):
        self.edit_popup_book_win = Toplevel(root)
        self.edit_popup_book_win.geometry("500x300")
        self.edit_popup_book_win.title("ADD BORROWERS INFORMATION")
        frame1 = Frame(self.edit_popup_book_win)
        frame1.pack(fill=X)
        lbl1 = Label(frame1, text="AUTHOR")
        lbl1.pack(side=LEFT, padx=5, pady=5)
        entry1 = Entry(frame1, textvariable=self.ub_author, bg = "gray84")
        entry1.pack(fill=X, padx=5, expand=True)
        #entry1.insert(0, "Place Holder")
        frame2 = Frame(self.edit_popup_book_win)
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="PUBLISHER")
        lbl2.pack(side=LEFT, padx=5, pady=5)
        entry2 = Entry(frame2, textvariable=self.ub_publisher, bg = "gray84")
        entry2.pack(fill=X, padx=5, expand=True)
        frame3 = Frame(self.edit_popup_book_win)
        frame3.pack(fill=X)
        lbl3 = Label(frame3, text="TITILE",)
        lbl3.pack(side=LEFT, padx=5, pady=5)
        entry3 = Entry(frame3, textvariable=self.ub_title, bg = "gray84")
        entry3.pack(fill=X, padx=5, expand=True)
        
        frame4 = Frame(self.edit_popup_book_win)
        frame4.pack(fill=X)
        
        lbl4 = Label(frame4, text="EDITION")
        lbl4.pack(side=LEFT, padx=5, pady=5)
            
        entry4 = Entry(frame4, textvariable=self.ub_edition, bg = "gray84")
        entry4.pack(fill=X, padx=5, expand=True)
        
        frame5 = Frame(self.edit_popup_book_win)
        frame5.pack(fill=X)
            
        lbl5 = Label(frame5, text="TOTAL BOOKS")
        lbl5.pack(side=LEFT, padx=5, pady=5,)
            
        entry5 = Entry(frame5, textvariable=self.ub_total, bg = "gray84")
        entry5.pack(fill=X, padx=5, expand=True)
        
        frame6 = Frame(self.edit_popup_book_win)
        frame6.pack(fill=X)
            
        lbl6 = Label(frame6, text="REF NUMBER")
        lbl6.pack(side=LEFT, padx=5, pady=5,)
            
        entry6 = Entry(frame6, textvariable=self.ub_ref_no, bg = "gray84")
        entry6.pack(fill=X, padx=5, expand=True)
        
        frame7 = Frame(self.edit_popup_book_win)
        frame7.pack(fill=X)
            
        lbl7 = Label(frame7, text="PRICE")
        lbl7.pack(side=LEFT, padx=5, pady=5,)
            
        entry7 = Entry(frame7, textvariable=self.ub_price, bg = "gray84")
        entry7.pack(fill=X, padx=5, expand=True)
        
        
        frame8 = Frame(self.edit_popup_book_win)
        frame8.pack(fill=X)
        
        
        date_button = Button(frame8, text="DATE", command=self.popup_cal_window_for_updating)
        date_button.pack(side=LEFT, padx=30, pady=5)
        
        self.ub_classification = StringVar(frame8)
        self.ub_classification.set("BOOK CLASSIFICATION") # default value
        om1 = OptionMenu(frame8, self.ub_classification, "GENERAL WORKES(000-099)", "PHILOSOPHY(100-199)", "RELIGION(200-299)", "SOCIAL SCIENCES(300-399)", "LANGUAGE(400-499)", "NATURAL SCIENCE(500-599)", "ARTS(600-699)", "LITERATURE(800-899)", "HISTORY(900-999)")
        om1.pack(side=RIGHT, padx=5, pady=5)
                
        
        frame9 = Frame(self.edit_popup_book_win)
        frame9.pack(fill=X)
        
        button = Button(frame9, text="UPDATE", width=10, command=self.update_books_fuc, bg= "YELLOW")
        button.pack(side=RIGHT, padx=50, pady=5)
        
        button = Button(frame9, text="DELETE", width=10, command=self.insert_books_fuc, bg= "RED")
        button.pack(side=RIGHT, padx=1, pady=5)
        
        conn1 = mysql.connector.connect(host="localhost", user="root", passwd="", db="project_tables")
        curp = conn1.cursor()
        mySql_insert_query = "SELECT * FROM books WHERE id=%s"
        rect = (self.books_id,)
        curp.execute(mySql_insert_query, rect)
        fetchquery = curp.fetchall()
        conn1.commit()
        conn1.close()
        for rec in fetchquery:
            	date = rec[8]
        # print(date)
        self.book_date = date
                    


#----------------------------POPUP CALENDER WINDOW  FOR EDITING/UPDATING BOOK---------------------------------------
    def popup_cal_window_for_updating(self):
        def print_sel():
            self.book_date = cal.selection_get()
            print(cal.selection_get())
            self.popup_cal_window_for_updating.destroy()
        
        self.popup_cal_window_for_updating = Toplevel(root)
        cal = Calendar(self.popup_cal_window_for_updating, font="Arial 14", selectmode='day', cursor="hand1", year=2020, month=2, day=5)
        cal.pack(fill="both", expand=True)
        conn1 = mysql.connector.connect(host="localhost", user="root", passwd="", db="project_tables")
        curp = conn1.cursor()
        mySql_insert_query = "SELECT * FROM books WHERE id=%s"
        rect = (self.books_id,)
        curp.execute(mySql_insert_query, rect)
        fetchquery = curp.fetchall()
        conn1.commit()
        conn1.close()
        for rec in fetchquery:
            	date = rec[8]
        # print(date)
        self.book_date = date
        cal.selection_set(date)
        
        button = Button(self.popup_cal_window_for_updating, text="ok", width=6, command=print_sel)
        button.pack()


                    
# ------------------------clender popup for books adding-------------------------------------------
    def cal_popup_for_b_add(self):
            def print_sel():
                self.cal_popup_for_b_add_var = cal.selection_get()
                print(cal.selection_get())
                self.cal_popup_for_b_add_win.destroy()
            
            self.cal_popup_for_b_add_win = Toplevel(root)
            cal = Calendar(self.cal_popup_for_b_add_win, font="Arial 14", selectmode='day', cursor="hand1", year=2020, month=2, day=5)
            cal.pack(fill="both", expand=True)
            cal.selection_set(datetime.datetime.now())
            button = Button(self.cal_popup_for_b_add_win, text="ok", width=6, command=print_sel)
            button.pack()
            


#-------------------export BOOKS to ms word fuc--------------------------------------
    def export_fuc(self):
        connection = mysql.connector.connect(host='localhost',
                                               database='project_tables',
                                               user='root',
                                               password='') 
        sql_select_Query = "select author, publisher, title, edition, classification, ref_no, price, date from books"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()  
        
        wb = Workbook('book_report.xlsx')  
        sheet1 = wb.add_worksheet()
        sheet1.write(0,0,'author')
        sheet1.write(0,1,'publisher')
        sheet1.write(0,2,'title')
        sheet1.write(0,3,'edition')
        sheet1.write(0,4,'classification')
        sheet1.write(0,5,'ref_no')
        sheet1.write(0,6,'price')
        sheet1.write(0,7,'date')

        row_number = 1
        for row in records:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1    
        wb.close()
        ms.showinfo("SUCESS!!","EXPORT SUCESSFUL")

#------------------------------------search fuction for books -------------------------------------
    def search_books_fuc(self):
        self.clear_table_for_books()
        connection = mysql.connector.connect(host='localhost',
                                               database='project_tables',
                                               user='root',
                                               password='') 
        sql_select_Query ="""SELECT * FROM books WHERE author LIKE %s 
                                     OR publisher LIKE %s OR title LIKE %s OR edition LIKE %s OR classification LIKE %s OR ref_no LIKE %s OR price LIKE %s OR date LIKE %s"""
                                    ##OR PostalCode LIKE '%".$search."%' 
                                    #OR Country LIKE '%".$search."%'  "
        ser = (self.search_for_books.get(), self.search_for_books.get(), self.search_for_books.get(), self.search_for_books.get(), self.search_for_books.get(), self.search_for_books.get(), self.search_for_books.get(), self.search_for_books.get())
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, ser)
        records = cursor.fetchall()
        connection.close()
        cursor.close()
        if (records):
            print("yess it exit")
            index = iid = 0
            for i in records:
                self.treev.insert("", index, iid, values=i ) 
                index = iid = index + 1
            print  (records)
        else:
            print("noo")
            self.treev.place_forget()
            self.search_for_books.set("")
            self.show_books_info()
            self.treev.place(x=2, y=150, height=558)
            ms.showwarning("SEARCH ERROR!!","Search not found")
        self.treev.place(x=2, y=150, height=550)

#--------------------------clear treeview table FOR BOOKS-----------------------------------------
    def clear_table_for_books(self):
        self.treev.place_forget()
        x = self.treev.get_children()
        print ('get_children values: ', x ,'\n')
        if x != '()': # checks if there is something in the first row
            for child in x:
                self.treev.delete(child)

#---------------------------------------END OF BOOK SECTION---------------------------------------------------------------------------------------------------------------------------------------------------

root = Tk()
c = vriable_int(root)
root.geometry("1200x500")
root.mainloop()
