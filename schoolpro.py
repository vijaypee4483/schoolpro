from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3
     
try:
    sdata=sqlite3.connect(database="student.sqlite")
    cursor=sdata.cursor()
    table1="create table sresult(name text,sclass text,rollno integer primary key ,hindi integer,english integer,maths integer,science integer,sscience integer,gk integer,art integer,sports integer,total integer)"
    table2="create table sdetail(name text,sclass text,rollno integer primary key,firstname text,lastname text,mother text,father text,dob text,adhar integer,email text,mobile integer,address1 text,address2 text,address3 text,address4 text,address5 text)"
    cursor.execute(table1)
    cursor.execute(table2)
    sdata.commit()
    sdata.close()
    print("Tables created")
except Exception as e:
    print(e)

win=Tk()
img=Image.open('copy.jpg')
image=ImageTk.PhotoImage(img)
win.geometry('1720x1080')
win.title("Our School by vp")
lable= Label(win,image=image)
lable.pack()

def home_frm():
    frm=Frame(win,highlightthickness=3,highlightbackground='plum',background='thistle')
    frm.place(x=420,y=55,width=500,height=210)

    def mainpage():
        frm.destroy()
        mainpage_frame()

    lbl_welcome=Label (frm,text=" Welcome to Our School Application ",font=('',20,'bold'),fg="blue",bg="red")
    lbl_welcome.place(x=0,y=0)
    lbl_main= Label (frm,text='Click here to start\nworking',font=('',15,'bold'),justify='center',fg="green",bg='thistle')
    lbl_main.place(x=125,y=100)

    btn_start=Button(frm,text='Get Start',font=('',20,'bold'),fg="black",bd=3,command=mainpage)
    btn_start.place(x=160,y=150)

def mainpage_frame():
    frm=Frame(win,highlightthickness=3,highlightbackground='plum',background='thistle')
    frm.place(x=420,y=55,width=500,height=310)

    def showdetail():
        global studentdetail_row
        studentdetail_row=[0,1,2]
        n=ename.get().upper()
        studentdetail_row[0]=n
        c=eclass.get().upper()
        studentdetail_row[1]=c
        r=ernum.get().upper()
        studentdetail_row[2]=r
        try:
            con=sqlite3.connect(database="student.sqlite")
            cursor=con.cursor()
            cursor.execute("select * from sdetail where name=? and sclass=? and rollno=?",(n,c,r))
            con.close()
            if (len(n)==0 or len(c)==0 or len(r)==0):
                messagebox.showerror("Detail","Fill All Details!!!")
            else:
                frm.destroy()
                detail_frame()
        except Exception as e:
            messagebox.showerror("Detail",str(e))
        

    def adddetail():
        global studentdetail_row
        studentdetail_row=[0,1,2]
        n=ename.get().upper()
        studentdetail_row[0]=n
        c=eclass.get().upper()
        studentdetail_row[1]=c
        r=ernum.get().upper()
        studentdetail_row[2]=r
        try:
            con=sqlite3.connect(database="student.sqlite")
            cursor=con.cursor()
            cursor.execute("select * from sdetail where name=? and sclass=? and rollno=?",(n,c,r))
            con.close()
            if (len(n)==0 or len(c)==0 or len(r)==0):
                messagebox.showerror("Detail","Fill All Details!!!")
            else:
                frm.destroy()
                adddetail_frame()
        except Exception as e:
            messagebox.showerror("Detail",str(e))

    def reset():
        ename.delete(0,"end")
        eclass.delete(0,"end")
        ernum.delete(0,"end")
        ernum.focus()

    main_strip=Label (frm,text= "  Please Enter Student Data Below  ",font=('',20,'bold'),fg="blue",bg="red")
    main_strip.place(x=0,y=0)
    sname= Label (frm,text='Name',font=('',15,'bold'),bg='thistle')
    sname.place(x=50,y=50)
    sclass= Label (frm,text='Class',font=('',15,'bold'),bg='thistle')
    sclass.place(x=50,y=90)
    srnum= Label (frm,text='Roll Number',font=('',15,'bold'),bg='thistle')
    srnum.place(x=50,y=130)

    ename=Entry(frm,font=('',15,'bold'),bd=3)
    ename.place(x=190,y=45)
    eclass=Combobox(frm,values=["Nursery","Prep","1st","2nd","3rd","4th","5th","6th","7th","8th"],font=('',15,'bold'))
    eclass.current(2)
    eclass.place(x=190,y=85)
    ernum=Spinbox(frm,font=('',15,'bold'),bd=3,from_=1000,to=9999)
    ernum.place(x=190,y=125)
    ernum.focus()

    btn_showd=Button(frm,text='Show Detail',font=('',20,'bold'),fg="black",bd=3,width=10,command=showdetail)
    btn_showd.place(x=65,y=200)
    btn_addd=Button(frm,text='Add Detail',font=('',20,'bold'),fg="black",bd=3,width=10,command=adddetail)
    btn_addd.place(x=260,y=200)
    btn_aresult=Button(frm,text='Reset',font=('',20,'bold'),fg="black",bd=3,width=5,command=reset)
    btn_aresult.place(x=200,y=250)

def adddetail_frame():
    frm=Frame(win,highlightthickness=3,highlightbackground='plum',background='thistle')
    frm.place(x=5,y=55,width=900,height=500)

    def back():
        frm.destroy()
        mainpage_frame()

    def savedetail():
        n=f"{studentdetail_row[0]}"
        c=f"{studentdetail_row[1]}"
        r=f"{studentdetail_row[2]}"
        n1=ename1.get().upper()
        n2=ename2.get().upper()
        mn=emname.get().upper()
        fn=efname.get().upper()
        d=edob.get().upper()
        a=eadhar.get().upper()
        e=eemail.get().upper()
        m=emob.get().upper()
        ad1=eaddress1.get().upper()
        ad2=eaddress2.get().upper()
        ad3=eaddress3.get().upper()
        ad4=eaddress4.get().upper()
        ad5=eaddress5.get().upper()

        try:
            if(len(n)==0 or len(c)==0 or len(r)==0 or len(n1)==0 or len(n2)==0 or len(mn)==0 or len(fn)==0 or len(d)==0 or len(a)==0 or len(e)==0 or len(m)==0 or len(ad1)==0 or len(ad2)==0 or len(ad3)==0 or len(ad4)==0 or len(ad5)==0):
                messagebox.showwarning('Validation',"Please Fill All Details!!")
            else:
                con=sqlite3.connect(database="student.sqlite")
                cursor=con.cursor()
                cursor.execute("insert into sdetail values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(n,c,r,n1,n2,mn,fn,d,a,e,m,ad1,ad2,ad3,ad4,ad5))
                con.commit()
                con.close()
                messagebox.showinfo("Detail","Detail Saved!")
                frm.destroy()
                mainpage_frame()
        except Exception as e:
            messagebox.showerror("Detail",str(e))

    def reset_detail():
        ename1.delete(0,"end")
        ename2.delete(0,"end")
        emname.delete(0,"end")
        efname.delete(0,"end")
        edob.delete(0,"end")
        eadhar.delete(0,"end")
        eemail.delete(0,"end")
        emob.delete(0,"end")
        eaddress1.delete(0,"end")
        eaddress2.delete(0,"end")
        eaddress3.delete(0,"end")
        eaddress4.delete(0,"end")
        eaddress5.delete(0,"end")

    def seeresult():
        n=f"{studentdetail_row[0]}"
        c=f"{studentdetail_row[1]}"
        r=f"{studentdetail_row[2]}"
        try:
            con=sqlite3.connect(database="student.sqlite")
            cursor=con.cursor()
            cursor.execute("select * from sresult where name=? and sclass=? and rollno=?",(n,c,r))
            con.close()
            frm.destroy()
            result_frame()
        except Exception as e:
            messagebox.showerror("Detail",str(e))
        

    def setresult():
        n=f"{studentdetail_row[0]}"
        c=f"{studentdetail_row[1]}"
        r=f"{studentdetail_row[2]}"
        n1=ename1.get().upper()
        n2=ename2.get().upper()
        mn=emname.get().upper()
        fn=efname.get().upper()
        d=edob.get().upper()
        a=eadhar.get().upper()
        e=eemail.get().upper()
        m=emob.get().upper()
        ad1=eaddress1.get().upper()
        ad2=eaddress2.get().upper()
        ad3=eaddress3.get().upper()
        ad4=eaddress4.get().upper()
        ad5=eaddress5.get().upper()
        try:
            con=sqlite3.connect(database="student.sqlite")
            cursor=con.cursor()
            cursor.execute("select * from sresult where name=? and sclass=? and rollno=?",(n,c,r))
            cursor.execute("insert into sdetail values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(n,c,r,n1,n2,mn,fn,d,a,e,m,ad1,ad2,ad3,ad4,ad5))
            con.commit()
            messagebox.showinfo("Detail","Detail Saved!")
            con.close()
            if(len(n)==0 or len(c)==0 or len(r)==0 or len(n1)==0 or len(n2)==0 or len(mn)==0 or len(fn)==0 or len(d)==0 or len(a)==0 or len(e)==0 or len(m)==0 or len(ad1)==0 or len(ad2)==0 or len(ad3)==0 or len(ad4)==0 or len(ad5)==0):
                messagebox.showwarning('Validation',"Please Fill All Details!!")
            else:
                frm.destroy()
                setresult_frame()
        except Exception as e:
            messagebox.showerror("Detail",str(e))

    add_strip=Label (frm,text="                Fill All The Details Carefully                  ",
    font=('',20,'bold'),fg="blue",bg="black")
    add_strip.place(x=0,y=0)
    
    sname1= Label (frm,text='First Name',font=('',15,'bold'),bg='thistle')
    sname1.place(x=20,y=50)
    sname2= Label (frm,text='Last Name',font=('',15,'bold'),bg='thistle')
    sname2.place(x=460,y=50)
    mname= Label (frm,text="Mother's Name",font=('',15,'bold'),bg='thistle')
    mname.place(x=20,y=90)
    fname= Label (frm,text="Fater's Name",font=('',15,'bold'),bg='thistle')
    fname.place(x=460,y=90)
    dob= Label (frm,text='Date of Birth',font=('',15,'bold'),bg='thistle')
    dob.place(x=20,y=130)
    adhar= Label (frm,text='Adhar Number',font=('',15,'bold'),bg='thistle')
    adhar.place(x=460,y=130)
    email= Label (frm,text='Email Id',font=('',15,'bold'),bg='thistle')
    email.place(x=20,y=170)
    mob= Label (frm,text='Mobile Number',font=('',15,'bold'),bg='thistle')
    mob.place(x=460,y=170)
    add_strip=Label (frm,text="Address Line",font=('',15,'bold'),fg="green",bg='thistle',justify=CENTER)
    add_strip.place(x=20,y=210)
    address1= Label (frm,text='House Number',font=('',15,'bold'),bg='thistle')
    address1.place(x=20,y=250)
    address2= Label (frm,text='Street',font=('',15,'bold'),bg='thistle')
    address2.place(x=20,y=290)
    address3= Label (frm,text='District',font=('',15,'bold'),bg='thistle')
    address3.place(x=460,y=290)
    address4= Label (frm,text='State',font=('',15,'bold'),bg='thistle')
    address4.place(x=20,y=330)
    address5= Label (frm,text='Pin',font=('',15,'bold'),bg='thistle')
    address5.place(x=460,y=330)

    ename1=Entry(frm,font=('',15,'bold'),bd=3)
    ename1.focus()
    ename1.place(x=190,y=45)
    ename2=Entry(frm,font=('',15,'bold'),bd=3)
    ename2.place(x=630,y=45)
    efname=Entry(frm,font=('',15,'bold'),bd=3)
    efname.place(x=190,y=85)
    emname=Entry(frm,font=('',15,'bold'),bd=3)
    emname.place(x=630,y=85)
    edob=DateEntry(frm,font=('',15,'bold'),bd=3,width=20)
    edob.place(x=190,y=125)
    eadhar=Spinbox(frm,font=('',15,'bold'),width=19,bd=3,from_=100000000000,to=999999999999)
    eadhar.place(x=630,y=125)
    eemail=Entry(frm,font=('',15,'bold'),bd=3)
    eemail.place(x=190,y=165)
    emob=Spinbox(frm,font=('',15,'bold'),width=19,bd=3,from_=1000000000,to=9999999999)
    emob.place(x=630,y=165)
    eaddress1=Entry(frm,font=('',15,'bold'),bd=3,width=57)
    eaddress1.place(x=186,y=245)
    eaddress2=Entry(frm,font=('',15,'bold'),bd=3)
    eaddress2.place(x=190,y=285)
    eaddress3=Entry(frm,font=('',15,'bold'),bd=3)
    eaddress3.place(x=630,y=285)
    eaddress4=Entry(frm,font=('',15,'bold'),bd=3)
    eaddress4.place(x=190,y=325)
    eaddress5=Spinbox(frm,font=('',15,'bold'),bd=3,from_=100000,to=999999,width=19)
    eaddress5.place(x=630,y=325)
    
    btn_save=Button(frm,text='Save',font=('',20,'bold'),fg="black",bd=3,width=7,command=savedetail)
    btn_save.place(x=230,y=370)
    btn_back=Button(frm,text='Back',font=('',20,'bold'),fg="black",bd=3,width=7,command=back)
    btn_back.place(x=385,y=370)
    btn_reset=Button(frm,text='Reset',font=('',20,'bold'),fg="black",bd=3,width=7,command=reset_detail)
    btn_reset.place(x=540,y=370)
    btn_result=Button(frm,text='See Result',font=('',20,'bold'),fg="black",bd=3,width=10,command=seeresult)
    btn_result.place(x=260,y=430)
    btn_new=Button(frm,text='Set Result',font=('',20,'bold'),fg="black",bd=3,width=10,command=setresult)
    btn_new.place(x=460,y=430)
    
def setresult_frame():
    frm=Frame(win,highlightthickness=3,highlightbackground='plum',background='thistle')
    frm.place(x=5,y=55,width=905,height=520)

    def back():
        frm.destroy()
        adddetail_frame()

    def home():
        frm.destroy()
        home_frm()

    def save_result():
        n=f"{studentdetail_row[0]}"
        c=f"{studentdetail_row[1]}"
        r=f"{studentdetail_row[2]}"
        h=ehindi.get()
        e=eeng.get()
        m=emath.get()
        s=esci.get()
        ss=essci.get()
        g=egk.get()
        a=eart.get()
        sp=esport.get()
        t=etotal.get()

        if(len(n)==0 or len(c)==0 or len(r)==0 or len(h)==0 or len(e)==0 or len(m)==0 or len(s)==0 or len(ss)==0 or len(g)==0 or len(a)==0 or len(sp)==0 or len(t)==0):
            messagebox.showwarning('Validation',"Please Fill All Details!!")
        else:
            try:
                con=sqlite3.connect(database="student.sqlite")
                cursor=con.cursor()
                cursor.execute("insert into sresult values(?,?,?,?,?,?,?,?,?,?,?,?)",(n,c,r,h,e,m,s,ss,g,a,sp,t))
                con.commit()
                con.close()
                messagebox.showinfo("Result","Result Saved!")
                frm.destroy()
                mainpage_frame()
            except Exception as e:
                messagebox.showerror("Result",str(e))

    def reset_result():
        ehindi.delete(0,"end")
        eeng.delete(0,"end")
        emath.delete(0,"end")
        esci.delete(0,"end")
        essci.delete(0,"end")
        egk.delete(0,"end")
        eart.delete(0,"end")
        esport.delete(0,"end")
        etotal.delete(0,"end")

    result_strip=Label (frm,text="                             Result                             ",
    font=('',20,'bold'),fg="blue",bg="black")
    result_strip.place(x=0,y=0)
    sname= Label (frm,text=f"{studentdetail_row[0]}",font=('',15,'bold'),fg='green',bg='thistle')
    sname.place(x=250,y=50)
    sclass= Label (frm,text=f"{studentdetail_row[1]}",font=('',15,'bold'),fg='green',bg='thistle')
    sclass.place(x=250,y=90)
    sroll= Label (frm,text=f"{studentdetail_row[2]}",font=('',15,'bold'),fg='green',bg='thistle')
    sroll.place(x=660,y=90)

    pname= Label (frm,text='Name=>',font=('',15,'bold'),bg='thistle')
    pname.place(x=150,y=50)
    pclass= Label (frm,text='Class=>',font=('',15,'bold'),bg='thistle')
    pclass.place(x=150,y=90)
    proll= Label (frm,text="Roll no=>",font=('',15,'bold'),bg='thistle')
    proll.place(x=550,y=90)

    line= Label (frm,text="==========================================================================",
    font=('',15,'bold'),bg='thistle')
    line.place(x=0,y=120)
    subject=Label (frm,text="Subject",font=('',15,'bold'),fg="green",bg='thistle',justify=CENTER)
    subject.place(x=50,y=150)
    max= Label (frm,text="Max",font=('',15,'bold'),fg="green",bg='thistle')
    max.place(x=250,y=150)
    maxh= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxh.place(x=250,y=190)
    maxe= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxe.place(x=250,y=230)
    maxm= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxm.place(x=250,y=270)
    maxs= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxs.place(x=250,y=310)
    maxss= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxss.place(x=250,y=350)
    maxg= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxg.place(x=250,y=390)
    maxa= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxa.place(x=250,y=430)
    maxsp= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxsp.place(x=250,y=470)
    obt= Label (frm,text='Obt Marks',font=('',15,'bold'),fg="green",bg='thistle')
    obt.place(x=450,y=150)
    hindi= Label (frm,text='Hindi',font=('',15,'bold'),bg='thistle')
    hindi.place(x=50,y=190)
    eng= Label (frm,text='English',font=('',15,'bold'),bg='thistle')
    eng.place(x=50,y=230)
    math= Label (frm,text='Maths',font=('',15,'bold'),bg='thistle')
    math.place(x=50,y=270)
    sci= Label (frm,text='Science',font=('',15,'bold'),bg='thistle')
    sci.place(x=50,y=310)
    ssci= Label (frm,text='S.Science',font=('',15,'bold'),bg='thistle')
    ssci.place(x=50,y=350)
    gk= Label (frm,text='Gk',font=('',15,'bold'),bg='thistle')
    gk.place(x=50,y=390)
    art= Label (frm,text='Art',font=('',15,'bold'),bg='thistle')
    art.place(x=50,y=430)
    sport= Label (frm,text='Sports',font=('',15,'bold'),bg='thistle')
    sport.place(x=50,y=470)
    total= Label (frm,text='Total',font=('',15,'bold'),fg='green',bg='thistle')
    total.place(x=700,y=150)

    ehindi=Spinbox(frm,font=('',15,'bold'),bd=3,from_=00,to=100,width=8)
    ehindi.place(x=450,y=185)
    eeng=Spinbox(frm,font=('',15,'bold'),bd=3,from_=00,to=100,width=8)
    eeng.place(x=450,y=225)
    emath=Spinbox(frm,font=('',15,'bold'),bd=3,from_=00,to=100,width=8)
    emath.place(x=450,y=265)
    esci=Spinbox(frm,font=('',15,'bold'),bd=3,from_=00,to=100,width=8)
    esci.place(x=450,y=305)
    essci=Spinbox(frm,font=('',15,'bold'),bd=3,from_=00,to=100,width=8)
    essci.place(x=450,y=345)
    egk=Spinbox(frm,font=('',15,'bold'),bd=3,from_=00,to=100,width=8)
    egk.place(x=450,y=385)
    eart=Spinbox(frm,font=('',15,'bold'),bd=3,from_=00,to=100,width=8)
    eart.place(x=450,y=425)
    esport=Spinbox(frm,font=('',15,'bold'),bd=3,from_=00,to=100,width=8)
    esport.place(x=450,y=465)
    etotal=Spinbox(frm,font=('',15,'bold'),bd=3,from_=00,to=800,width=8)
    etotal.place(x=700,y=185)
    
    btn_save=Button(frm,text='Save',font=('',20,'bold'),fg="black",bd=3,width=7,command=save_result)
    btn_save.place(x=700,y=300)
    btn_back=Button(frm,text='Back',font=('',20,'bold'),fg="black",bd=3,width=7,command=back)
    btn_back.place(x=700,y=350)
    btn_result=Button(frm,text='Reset',font=('',20,'bold'),fg="black",bd=3,width=7,command=reset_result)
    btn_result.place(x=700,y=400)
    btn_new=Button(frm,text='Home',font=('',20,'bold'),fg="black",bd=3,width=7,command=home)
    btn_new.place(x=700,y=450)

def detail_frame():
    frm=Frame(win,highlightthickness=3,highlightbackground='plum',background='thistle')
    frm.place(x=5,y=55,width=900,height=500)

    sname1= Label (frm,text='First Name',font=('',15,'bold'),bg='thistle')
    sname1.place(x=20,y=50)
    sname2= Label (frm,text='Last Name',font=('',15,'bold'),bg='thistle')
    sname2.place(x=460,y=50)
    mname= Label (frm,text="Mother's Name",font=('',15,'bold'),bg='thistle')
    mname.place(x=20,y=90)
    fname= Label (frm,text="Fater's Name",font=('',15,'bold'),bg='thistle')
    fname.place(x=460,y=90)
    dob= Label (frm,text='Date of Birth',font=('',15,'bold'),bg='thistle')
    dob.place(x=20,y=130)
    adhar= Label (frm,text='Adhar Number',font=('',15,'bold'),bg='thistle')
    adhar.place(x=460,y=130)
    email= Label (frm,text='Email Id',font=('',15,'bold'),bg='thistle')
    email.place(x=20,y=170)
    mob= Label (frm,text='Mobile Number',font=('',15,'bold'),bg='thistle')
    mob.place(x=460,y=170)
    add_strip=Label (frm,text="Address Line",font=('',15,'bold'),fg="green",bg='thistle',justify=CENTER)
    add_strip.place(x=20,y=210)
    address1= Label (frm,text='House Number',font=('',15,'bold'),bg='thistle')
    address1.place(x=20,y=250)
    address2= Label (frm,text='Street',font=('',15,'bold'),bg='thistle')
    address2.place(x=20,y=290)
    address3= Label (frm,text='District',font=('',15,'bold'),bg='thistle')
    address3.place(x=460,y=290)
    address4= Label (frm,text='State',font=('',15,'bold'),bg='thistle')
    address4.place(x=20,y=330)
    address5= Label (frm,text='Pin',font=('',15,'bold'),bg='thistle')
    address5.place(x=460,y=330)

    def seeresult():
        frm.destroy()
        result_frame()

    def setresult():
        frm.destroy()
        setresult_frame()

    def back():
        frm.destroy()
        mainpage_frame()

    detail_strip=Label (frm,text="                         Student Details                        ",font=('',20,'bold'),fg="blue",bg="black")
    detail_strip.place(x=00,y=00)

    n=f"{studentdetail_row[0]}"
    c=f"{studentdetail_row[1]}"
    r=f"{studentdetail_row[2]}"

    try:
        con=sqlite3.connect("student.sqlite")
        cursor=con.cursor()
        details=cursor.execute("select * from sdetail where name=(?) and sclass=(?) and rollno=(?)",(n,c,r,))
        details=cursor.fetchall()
        if(len(details)==0):
            messagebox.showerror("Detail","Detail is not exist")
        else:
            for detail in details:
                ename1=Label(frm,text=detail[3],font=('',15,'bold'),fg='blue',bg='thistle')
                ename1.place(x=190,y=50)
                ename2=Label(frm,text=detail[4],font=('',15,'bold'),fg='blue',bg='thistle')
                ename2.place(x=630,y=50)
                efname=Label(frm,text=detail[5],font=('',15,'bold'),fg='blue',bg='thistle')
                efname.place(x=190,y=90)
                emname=Label(frm,text=detail[6],font=('',15,'bold'),fg='blue',bg='thistle')
                emname.place(x=630,y=90)
                edob=Label(frm,text=detail[7],font=('',15,'bold'),fg='blue',bg='thistle')
                edob.place(x=190,y=130)
                eadhar=Label(frm,text=detail[8],font=('',15,'bold'),fg='blue',bg='thistle')
                eadhar.place(x=630,y=130)
                eemail=Label(frm,text=detail[9],font=('',15,'bold'),fg='blue',bg='thistle')
                eemail.place(x=190,y=170)
                emob=Label(frm,text=detail[10],font=('',15,'bold'),fg='blue',bg='thistle')
                emob.place(x=630,y=170)
                eaddress1=Label(frm,text=detail[11],font=('',15,'bold'),fg='blue',bg='thistle')
                eaddress1.place(x=186,y=250)
                eaddress2=Label(frm,text=detail[12],font=('',15,'bold'),fg='blue',bg='thistle')
                eaddress2.place(x=190,y=290)
                eaddress3=Label(frm,text=detail[13],font=('',15,'bold'),fg='blue',bg='thistle')
                eaddress3.place(x=630,y=290)
                eaddress4=Label(frm,text=detail[14],font=('',15,'bold'),fg='blue',bg='thistle')
                eaddress4.place(x=190,y=330)
                eaddress5=Label(frm,text=detail[15],font=('',15,'bold'),fg='blue',bg='thistle')
                eaddress5.place(x=630,y=330)
        con.close()
    except Exception as e:
        messagebox.showerror("Detail Error",str(e))

    btn_seer=Button(frm,text='See Result',font=('',20,'bold'),fg="black",bd=3,width=10,command=seeresult)
    btn_seer.place(x=280,y=400)
    btn_setr=Button(frm,text='Set Result',font=('',20,'bold'),fg="black",bd=3,width=10,command=setresult)
    btn_setr.place(x=470,y=400)
    btn_back=Button(frm,text='Back',font=('',20,'bold'),fg="black",bd=3,width=5,command=back)
    btn_back.place(x=410,y=450)

def result_frame():
    frm=Frame(win,highlightthickness=3,highlightbackground='plum',background='thistle')
    frm.place(x=5,y=55,width=900,height=500)

    def home():
        frm.destroy()
        mainpage_frame()

    result_strip=Label (frm,text="                          Student Result                        ",font=('',20,'bold'),fg="blue",bg="black")
    result_strip.place(x=00,y=00)

    pname= Label (frm,text='Name',font=('',15,'bold'),bg='thistle')
    pname.place(x=150,y=50)
    pclass= Label (frm,text='Class',font=('',15,'bold'),bg='thistle')
    pclass.place(x=150,y=90)
    proll= Label (frm,text="Roll no",font=('',15,'bold'),bg='thistle')
    proll.place(x=550,y=90)

    line= Label (frm,text="==========================================================================",
    font=('',15,'bold'),bg='thistle')
    line.place(x=0,y=120)
    subject=Label (frm,text="Subject",font=('',15,'bold'),fg="green",bg='thistle',justify=CENTER)
    subject.place(x=50,y=150)
    max= Label (frm,text="Max",font=('',15,'bold'),fg="green",bg='thistle')
    max.place(x=250,y=150)
    maxh= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxh.place(x=250,y=190)
    maxe= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxe.place(x=250,y=230)
    maxm= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxm.place(x=250,y=270)
    maxs= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxs.place(x=250,y=310)
    maxss= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxss.place(x=250,y=350)
    maxg= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxg.place(x=250,y=390)
    maxa= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxa.place(x=250,y=430)
    maxsp= Label (frm,text="100",font=('',15,'bold'),bg='thistle')
    maxsp.place(x=250,y=470)
    obt= Label (frm,text='Obt Marks',font=('',15,'bold'),fg="green",bg='thistle')
    obt.place(x=450,y=150)
    hindi= Label (frm,text='Hindi',font=('',15,'bold'),bg='thistle')
    hindi.place(x=50,y=190)
    eng= Label (frm,text='English',font=('',15,'bold'),bg='thistle')
    eng.place(x=50,y=230)
    math= Label (frm,text='Maths',font=('',15,'bold'),bg='thistle')
    math.place(x=50,y=270)
    sci= Label (frm,text='Science',font=('',15,'bold'),bg='thistle')
    sci.place(x=50,y=310)
    ssci= Label (frm,text='S.Science',font=('',15,'bold'),bg='thistle')
    ssci.place(x=50,y=350)
    gk= Label (frm,text='Gk',font=('',15,'bold'),bg='thistle')
    gk.place(x=50,y=390)
    art= Label (frm,text='Art',font=('',15,'bold'),bg='thistle')
    art.place(x=50,y=430)
    sport= Label (frm,text='Sports',font=('',15,'bold'),bg='thistle')
    sport.place(x=50,y=470)
    total= Label (frm,text='Total',font=('',15,'bold'),fg='green',bg='thistle')
    total.place(x=700,y=150)

    n=f"{studentdetail_row[0]}"
    c=f"{studentdetail_row[1]}"
    r=f"{studentdetail_row[2]}"
    
    try:
        con=sqlite3.connect(database="student.sqlite")
        cursor=con.cursor()
        results=cursor.execute("select * from sresult where name=(?) and sclass=(?) and rollno=(?)",(n,c,r,))
        results=cursor.fetchall()
        if(len(results)==0):
            messagebox.showerror("Result","Result is not exist")
        else:
            for result in results:
                ename= Label (frm,text=result[0],font=('',15,'bold'),bg='thistle',fg='brown')
                ename.place(x=300,y=50)
                eclass= Label (frm,text=result[1],font=('',15,'bold'),bg='thistle',fg='brown')
                eclass.place(x=300,y=90)
                eroll= Label (frm,text=result[2],font=('',15,'bold'),bg='thistle',fg='brown')
                eroll.place(x=700,y=90)
                ehindi=Label(frm,text=result[3],font=('',15,'bold'),fg='blue',bg='thistle')
                ehindi.place(x=450,y=190)
                eeng=Label(frm,text=result[3],font=('',15,'bold'),fg='blue',bg='thistle')
                eeng.place(x=450,y=230)
                emath=Label(frm,text=result[5],font=('',15,'bold'),fg='blue',bg='thistle')
                emath.place(x=450,y=270)
                esci=Label(frm,text=result[6],font=('',15,'bold'),fg='blue',bg='thistle')
                esci.place(x=450,y=310)
                essci=Label(frm,text=result[7],font=('',15,'bold'),fg='blue',bg='thistle')
                essci.place(x=450,y=350)
                egk=Label(frm,text=result[8],font=('',15,'bold'),fg='blue',bg='thistle')
                egk.place(x=450,y=390)
                eart=Label(frm,text=result[9],font=('',15,'bold'),fg='blue',bg='thistle')
                eart.place(x=450,y=430)
                esport=Label(frm,text=result[10],font=('',15,'bold'),fg='blue',bg='thistle')
                esport.place(x=450,y=470)
                etotal=Label(frm,text=result[11],font=('',15,'bold'),fg='blue',bg='thistle')
                etotal.place(x=700,y=190)
        con.close()
    except Exception as e:
        messagebox.showerror("Result Error",str(e))

    btn_home=Button(frm,text='Home',font=('',20,'bold'),fg="black",bd=3,width=5,command=home)
    btn_home.place(x=700,y=225)

home_frm()
win.mainloop()