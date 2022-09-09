from tkinter import *
from tkinter  import ttk
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Management System')
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System", font=("georgia",40,"bold"),bg="#E0B0FF",fg="#FCDFFF")
        title.pack(side=TOP,fill='x')

        #---------All variables-------------
        self.Roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.dob_var=StringVar()
        self.contact_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()



                #------------Manage Frame-----------
        Manage_frame=Frame(self.root,bd=2,relief='ridge',bg="#FFE6E8")
        Manage_frame.place(x=20,y=100,width=450,height=560)
        m_title=Label(Manage_frame,text='Manage Student',font=("georgia",16,"bold"),fg='black',bg="#FFE6E8")
        m_title.grid(row=0,columnspan=2,pady=20)
        


        lbl_roll=Label(Manage_frame, text='Roll No',font=("georgia",12,"bold"),bg="#FFE6E8",fg='black')
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_frame, textvariable=self.Roll_no_var,font=("georgia",12,"bold"),fg='black')
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_frame, text='Name',font=("georgia",12,"bold"),bg="#FFE6E8",fg='black')
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')

        txt_name=Entry(Manage_frame,textvariable=self.name_var, font=("georgia",12,"bold"),fg='black')
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_frame, text='Email',font=("georgia",12,"bold"),bg="#FFE6E8",fg='black')
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky='w')

        txt_email=Entry(Manage_frame,textvariable=self.email_var, font=("georgia",12,"bold"),fg='black')
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky='w')

        lbl_gender=Label(Manage_frame, text='Pronouns',font=("georgia",12,"bold"),bg="#FFE6E8",fg='black')
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky='w')

        combo_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var, font=("georgia",10,"bold"),width=18,state='readonly')
        combo_gender['values']=("he/him","she/her","they","prefer not to say")
        combo_gender.grid(row=4,column=1,pady=8,padx=20,sticky='w')

        lbl_dob=Label(Manage_frame, text='date of Birth',font=("georgia",10,"bold"),bg="#FFE6E8",fg='black')
        lbl_dob.grid(row=5,column=0,pady=10,padx=20,sticky='w')

        txt_dob=Entry(Manage_frame,textvariable=self.dob_var, font=("georgia",12,"bold"),fg='black')
        txt_dob.grid(row=5,column=1,pady=10,padx=20,sticky='w')

        lbl_contact=Label(Manage_frame, text='Contact No',font=("georgia",10,"bold"),bg="#FFE6E8",fg='black')
        lbl_contact.grid(row=6,column=0,pady=10,padx=20,sticky='w')

        txt_contact=Entry(Manage_frame,textvariable=self.contact_var, font=("georgia",12,"bold"),fg='black')
        txt_contact.grid(row=6,column=1,pady=10,padx=20,sticky='w')

        lbl_address=Label(Manage_frame, text='address',font=("georgia",12,"bold"),bg="#FFE6E8",fg='black')
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky='w')

        self.txt_address=Text(Manage_frame, width=25, height=4)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky='w')

        #----------button frame----------
        btn_frame=Frame(Manage_frame,bd=4,bg="#FFE6E8")
        btn_frame.place(x=7,y=480,width=430)

        Addbtn=Button(btn_frame,text='Add',width=9,command=self.add_students,fg="#FCDFFF",bg='black',font=('georgia',8,'bold')).grid(row=0,column=0,padx=10,pady=10)
        upddbtn=Button(btn_frame,text='Update',width=9,fg="#FCDFFF",bg='black',font=('georgia',8,'bold'),command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delbtn=Button(btn_frame,text='Delete',width=9,fg="#FCDFFF",bg='black',font=('georgia',8,'bold'),command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clrbtn=Button(btn_frame,text='Clear',width=9,fg="#FCDFFF",bg='black',font=('georgia',8,'bold'),command=self.clear).grid(row=0,column=3,padx=10,pady=10)


         #------detail fram------------
        Detail_frame=Frame(self.root,bd=2,relief='ridge',bg="#FFE6E8")
        Detail_frame.place(x=500,y=100,width=800,height=560)

        lbl_search=Label(Detail_frame, text='Search By',font=("georgia",12,"bold"),bg="#FFE6E8",fg='black')
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky='w')

        combo_search=ttk.Combobox(Detail_frame,textvariable=self.search_by,font=("georgia",10,"bold"),width=12,state='readonly')
        combo_search['values']=("roll_no","name","contacts")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky='w')

        txt_search=Entry(Detail_frame,textvariable=self.search_txt,width=20, font=("georgia",10),fg='black')
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')

        searchbtn=Button(Detail_frame,command=self.search_data,text='Search',width=9,fg="#FCDFFF",bg='black',font=('georgia',8,'bold'),pady=5).grid(row=0,column=3,padx=10,pady=10)
        shwbtn=Button(Detail_frame,text='Show all',command=self.fetch_data,width=9,fg="#FCDFFF",bg='black',font=('georgia',8,'bold'),pady=5).grid(row=0,column=4,padx=10,pady=10)



        #---------Table Frame-----------
        
        Table_frame=Frame(Detail_frame,bd=2,relief='ridge',bg="#FFE6E8")
        Table_frame.place(x=10,y=70,width=760,height=469)

        scroll_x=Scrollbar(Table_frame,orient='horizontal')
        scroll_y=Scrollbar(Table_frame,orient='vertical')

        self.Student_table=ttk.Treeview(Table_frame, columns=('name','roll','email','gender','dob','contact','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side='bottom',fill='x')
        scroll_y.pack(side='right',fill='y')
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading('roll',text='roll no')
        self.Student_table.heading('name',text='Name')
        self.Student_table.heading('email',text='Email')
        self.Student_table.heading('gender',text='Gender')
        self.Student_table.heading('dob',text='D.O.B')
        self.Student_table.heading('contact',text='Contacts')
        self.Student_table.heading('address',text='Address')
        self.Student_table['show']='headings'
        self.Student_table.column('roll',width=100)
        self.Student_table.column('name',width=100)
        self.Student_table.column('email',width=100)
        self.Student_table.column('gender',width=100)
        self.Student_table.column('dob',width=100)
        self.Student_table.column('contact',width=100)
        self.Student_table.column('address',width=150)
        self.Student_table.pack(fill='both',expand=1)
        self.fetch_data()
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        



    def add_students(self):
      con=pymysql.connect(host='localhost',user='root',password="",database="stm")
      cur=con.cursor()
      cur.execute('insert into students values(%s,%s,%s,%s,%s,%s,%s)',(self.Roll_no_var.get()
                                                                       ,self.name_var.get(), self.email_var.get(),self.gender_var.get()
                                                                       ,self.dob_var.get(),self.contact_var.get(),
                                                                       self.txt_address.get('1.0',END)))
      con.commit()
      self.fetch_data()
      self.clear()
      con.close()
    def fetch_data(self): 
        con=pymysql.connect(host='localhost',user='root',password="",database="stm")
        cur=con.cursor()
        cur.execute('select * from students')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                 self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        
        self.Roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[6])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host='localhost',user='root',password="",database="stm")
        cur=con.cursor()
        cur.execute('update students set name=%s,email=%s,gender=%s,%s,D.o.B=%s,contact=%s,address=%s where roll_no=',(self.Roll_no_var.get()
                                                                       ,self.name_var.get(), self.email_var.get(),self.gender_var.get()
                                                                       ,self.dob_var.get(),self.contact_var.get(),
                                                                       self.txt_address.get('1.0',END)))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def delete_data(self): 
        con=pymysql.connect(host='localhost',user='root',password="",database="stm")
        cur=con.cursor()
        cur.execute('delete from students where roll_no=%s',self.Roll_no_var.get())
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def search_data(self): 
        con=pymysql.connect(host='localhost',user='root',password="",database="stm")
        cur=con.cursor()

        cur.execute("select * from students where"+str(self.search_by.get()) + "like '%" + str(self.search_by.get()) +"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                 self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
        
    



            

             

            
        





root=Tk()
ob=Student(root)
root.mainloop()
