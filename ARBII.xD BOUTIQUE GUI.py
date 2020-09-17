from tkinter import *
import random
import os, sys
import time
import sqlite3
import datetime
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font as tkfont

from tkinter import ttk


class Reg:

    def __init__(self, root):
        self.root = root


        self.frame = Frame(self.root)

        self.root.mainloop()

    def signup(self):

        signup = Frame(self.root).pack()
        c = Canvas(signup, width=600, height=600, bg='white')
        # ---------------------------------------------------------------------------------------
        l = Label(c, text='SIGNUP HERE', font=('times new roman', 15, 'bold'), fg='black', bg='white')
        l.grid(row=1, column=6)
        l32 = Label(c, text='', bg='white')
        l32.grid(row=2, column=6)
        l34 = Label(c, text='', bg='white')
        l34.grid(row=3, column=6)

        l1 = Label(c, text='UserName :', font=('times new roman', 15), fg='black')
        l1.grid(row=4, column=3)
        l7 = Label(c, text='EMAIL :', font=('times new roman', 15), fg='black')
        l7.grid(row=6, column=3)
        l9 = Label(c, text='PASSWORD :', font=('times new roman', 15), fg='black')
        l9.grid(row=8, column=3)
        l50 = Label(c, text='', bg='white')
        l50.grid(row=5, column=3)
        l0 = Label(c, text='', bg='white')
        l0.grid(row=7, column=3)
        l00 = Label(c, text='', bg='white').grid(row=10, column=6)

        self.username = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        #___________________________________________________________________________
        e1 = Entry(c, width=35, bg='light grey', textvariable=self.username)
        e1.grid(row=4, column=6)

        e2 = Entry(c, width=35, bg='light grey', textvariable=self.email)
        e2.grid(row=6, column=6)

        e3 = Entry(c, width=35, bg='light grey', textvariable=self.password)
        e3.grid(row=8, column=6)

        btn3 = Button(c, text='Sign-In', width=20, height = 2, command=lambda: [c.destroy(), self.put()]).grid(row=11, column=6)
        # print('ACCOUNT CREATED')
        btn1 = Button(c, text='QUIT', width=15, height = 2, command=lambda: [c.destroy(), sys.exit() ]).grid(row=11, column=3)
        #____________________________________________________________________________________________

        c.place(x=500, y=150)

        # __________________________________________________________________________________________________

    def put(self):
        if self.username.get() != '' and self.email.get() != '' and self.password.get() != '':
            conn = sqlite3.connect('arbii.db')
            obj = conn.cursor()
            obj.execute('SELECT * FROM records')
            self.c = obj.fetchall()
            print(self.c)
            for row in self.c:
                if row[1] == self.username.get():
                    messagebox.askokcancel('Sign-in FALIED', 'Username Already Exists...')
                    self.signup()
                    break


                # -------------------------------------------------------------------------------------------

                # -------------------------------------------------------------------------------------------
                elif row[1] != self.username.get():

                    conn = sqlite3.connect('arbii.db')
                    cur = conn.cursor()
                    cur.execute(
                        "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY,name text,email text, password text)")

                    cur.execute("INSERT INTO records Values(Null,?,?,?)",
                                (self.username.get(), self.email.get(), self.password.get()))
                    messagebox.showinfo('SUCCESSFULLY SIGN-IN', 'ACCOUNT CREATED SUCESSFULLY')
                    self.signup()

                    # root = Tk()
                    # root.geometry('500x500')
                    # btn1 = Button(root , text = 'destroy' , width = 30 , command = sys.exit).pack()
                    # root.mainloop()
                    # self.l = menu(self.root)

                    break

            conn.commit()
            conn.close()



        else:
            messagebox.showerror('Sign-in FAILED', 'Please fill these options correctly')
            self.signup()

        # self.frame.pack()

        self.frame.pack()

    def delRECORDS(self):
        frame = Frame(self.root)

        label = Label(frame, text='ENTER NAME YOU WANT TO DELETE : ', font=('times new roman', 15, 'bold')).grid(row=2, column=3)
        self.delt = StringVar()
        entry = Entry(frame, textvariable = self.delt).grid(row=2, column=6)
        btn1 = Button(frame , text = 'DELETE ACCOUNT',command = self.dell).grid(row = 3 , column = 3)
        btn1 = Button(frame , text = 'BACK',width = 15,command = lambda :[frame.destroy(),userinterface(self.root)]).grid(row = 3 , column = 6)


        frame.place(anchor = 'c' , relx = .5 , rely = .5)

    def dell(self):
        conn = sqlite3.connect('arbii.db')
        obj = conn.cursor()
        obj.execute('SELECT * FROM records')
        c = obj.fetchall()
        print(c)

        quirry = 'DELETE FROM records WHERE name = ?;'
        conn.execute(quirry, (self.delt.get(),))

        obj.execute('SELECT * FROM records')
        c = obj.fetchall()
        #print(c)
        #print("ACCOUNT DELETED.....")
        messagebox.showinfo('ACCOUNT DELETED' , 'ACCOUNT DELETED SUCCESSFULLY')
        conn.commit()
        conn.close()

    # ______________________________________________________________________________________________________




class fileread:

    def read(self, a,b):

        l = open(a, "r+")
        for line in l:
            b.append(line)
        l.close()



class menu(fileread):
    acc_name="none"
    TShirt = 500
    pent = 500
    kurta = 500
    pajama = 500
    shirt = 500
    jogger = 500
    tie = 500
    Trowser = 500
    watches = 500
    TShirtsprice = 500
    pentprice = 700
    kurtaprice = 400
    pajamasprice = 300
    shirtprice = 500
    joggersprice = 1500
    tieprice = 100
    trowserprice = 700
    watchesprice = 1000


    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)

        self.option()
        self.frame.pack()
        self.root.mainloop()

    def addi(self):
        #while True:
        ADMfrm = Frame(self.root)
        l1 = Label(ADMfrm, text="ADMIN PANEL\nADDING STOCK ", font=('times new roman', 25, 'bold')).grid(row=0, column=3)
        l1 = Label(ADMfrm, text="1. SHIRT PRICE 500 EACH", font=('times new roman', 15)).grid(row=1, column=4)
        l2 = Label(ADMfrm, text="2. T-SHIRT PRICE 500 EACH ", font=('times new roman', 15)).grid(row=2, column=4)
        l3 = Label(ADMfrm, text="3. PENT PRICE 700 EACH", font=('times new roman', 15)).grid(row=3, column=4)
        l4 = Label(ADMfrm, text="4. TIE PRICE 100 EACH ", font=('times new roman', 15)).grid(row=4, column=4)
        l5 = Label(ADMfrm, text="5. JOGGERS PRICE 1500 EACH", font=('times new roman', 15)).grid(row=5, column=4)
        l6 = Label(ADMfrm, text="6. TROWSER PRICE 700 EACH", font=('times new roman', 15)).grid(row=6, column=4)
        l7 = Label(ADMfrm, text="7. WATCH PRICE 1000 EACH", font=('times new roman', 15)).grid(row=7, column=4)
        l8 = Label(ADMfrm, text="8. KURTA PRICE 400 EACH ", font=('times new roman', 15)).grid(row=8, column=4)
        l9 = Label(ADMfrm, text="9. PAJAMAS PRICE  300 EACH", font=('times new roman', 15)).grid(row=8, column=4)



        label1 = Label(ADMfrm, text='ENTER OPTION NUMBER ', font=('times new roman', 15, 'bold'), fg='black').grid(row=10, column=3)
        label2 = Label(ADMfrm, text='ENTER QUANTITY YOU WANT TO ADD', font=('times new roman', 15, 'bold'), fg='black').grid(row=11, column=3)
        try:
            self.l = StringVar()
            self.m = StringVar()
            e1 = Entry(ADMfrm,width=35, bg='light grey', textvariable=self.l).grid(row = 10, column = 6 )
            e2 = Entry(ADMfrm, width=35, bg='light grey', textvariable=self.m).grid(row=11 , column = 6)
                    #m = int(input("enter the quantity you want to add : "))
            btn1  = Button(ADMfrm , text = 'ENTER' , command =self.manage).grid(row = 12, column = 6)
            btn1  = Button(ADMfrm , text = 'BACK' ,width = 15,height = 2, command =lambda: [ADMfrm.destroy(), userinterface(self.root)]).grid(row = 12, column = 4)

        except:
                   messagebox.showerror('VALUE ERROR', 'PLEASE ENTER DIGIT')
        ADMfrm.place(anchor='c', relx=.5, rely=.5)
    def manage(self):

        if int(self.l.get())== int(1):

            self.shirt = self.shirt + int(self.m.get())

            messagebox.showinfo('QUANTITY INCREASED', 'SHIRTS INCREASED : '+str(self.shirt))
        elif int(self.l.get())== int(2):
            self.TShirt = self.TShirt + int(self.m.get())

            messagebox.showinfo('QUANTITY INCREASED', 'TSHIRTS INCREASED : ' + str(self.TShirt))
        elif int(self.l.get()) == int(3):
            self.pent = self.pent + int(self.m.get())

            messagebox.showinfo('QUANTITY INCREASED', 'PENTS INCREASED : ' + str(self.pent))
        elif int(self.l.get()) == int(4):
            self.tie = self.tie + int(self.m.get())

            messagebox.showinfo('QUANTITY INCREASED', 'TIE INCREASED : ' + str(self.tie))
        elif int(self.l.get()) == int(5):
            self.jogger = self.jogger + int(self.m.get())

            messagebox.showinfo('QUANTITY INCREASED', 'JOGGERS INCREASED : ' + str(self.jogger))
        elif int(self.l.get()) == int(6):
            self.Trowser = self.Trowser + int(self.m.get())

            messagebox.showinfo('QUANTITY INCREASED', 'TROWSER INCREASED : ' + str(self.Trowser))
        elif int(self.l.get()) == int(7):
            self.watches = self.watches + int(self.m.get())

            messagebox.showinfo('QUANTITY INCREASED', 'WATCHES INCREASED : ' + str(self.watches))
        elif int(self.l.get()) == int(8):
            self.kurta = self.kurta + int(self.m.get())

            messagebox.showinfo('QUANTITY INCREASED', 'KURTA INCREASED : ' + str(self.kurta))
        elif int(self.l.get()) == int(9):
            self.pajama = self.pajama + int(self.m.get())

            messagebox.showinfo('QUANTITY INCREASED', 'PJAMAS INCREASED : ' + str(self.pajama))


    def login(self):
        login_frame = Frame(self.root).pack()
        c = Canvas(login_frame, width=500, height=500, bg='white')

        # self.a1 = input('ENTER EMAIL TO Login :')
        # self.a2 = input("ENTER PASSWORD TO Login : ")
        # _______________________________________________________________________________________________________
        self.emailL = StringVar()
        self.passwordL = StringVar()

        # ______________________________________________________________________________________________________
        l = Label(c, text='LOGIN HERE', font=('times new roman', 15, 'bold'), fg='black', bg='white')
        l.grid(row=1, column=6)
        l32 = Label(c, text='', bg='white')
        l32.grid(row=2, column=6)
        l34 = Label(c, text='', bg='white')
        l34.grid(row=3, column=6)

        l1 = Label(c, text='Email :', font=('times new roman', 17), fg='black')
        l1.grid(row=4, column=3)
        l7 = Label(c, text='Password :', font=('times new roman', 17), fg='black')
        l7.grid(row=6, column=3)
        # l9 = Label(c, text='PASSWORD :', font=('times new roman', 15), fg='black')
        # l9.grid(row=8, column=3)
        l50 = Label(c, text='', bg='blue')
        l50.grid(row=5, column=3)
        l0 = Label(c, text='', bg='white')
        l0.grid(row=7, column=3)
        l00 = Label(c, text='', bg='white').grid(row=10, column=6)
        l2 = Label(c, text='', bg='white').grid(row=5, column=3)
        # _______________________________________________________________________________________________________
        e1 = Entry(c, width=35, bg='light grey', textvariable=self.emailL)
        e1.grid(row=4, column=6)

        e2 = Entry(c, width=35, bg='light grey', textvariable=self.passwordL)
        e2.grid(row=6, column=6)
        # -------------------------------------------------------------------------------------------------------
        btn1 = Button(c, width=20,height = 1, text='Login', command=lambda: [c.destroy(), self.enter()]).grid(row=8, column=6)
        btn2 = Button(c, width=10,height = 1, text='Back', command=lambda: [c.destroy(), userinterface(self.root)]).grid(row=8, column=3)

        c.place(anchor = 'c' , relx = .5, rely=.5)
        # _______________________________________________________________________________________________________

    def enter(self):
        conn = sqlite3.connect('arbii.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM records WHERE email=? AND password=?", (self.emailL.get(), self.passwordL.get()))
        # cur.execute('SELECT * FROM records')

        self.row = cur.fetchall()

        print(self.row)


        if self.row == []:
            # l3.config(text = "InValid Entries..")
            messagebox.showerror('InValid Entries', 'Please fill these optons correctly')
            self.login()
        elif self.row != []:
            if self.passwordL.get() != '' and self.emailL.get() != '':
                user_name = self.row[0][1]
                # l3.config(text="user name found with name: "+user_name)
                messagebox.showinfo('Successfully Login', 'UserName found with NAME : ' + user_name)
                menu.acc_name = user_name
                #self.option()
                r = menu(self.root)

            else:
                messagebox.showerror('Login FAILED', 'INVALID ENTRIES')
                self.login()


        else:
            # l3.config(text="user not found ")
            messagebox.showerror('Failed To Login', 'User not found')
            self.login()

            # sys.exit()
        conn.commit()
        conn.close()

    def category(self):
        cat_frm = Frame(self.root)
        l1 = Label(cat_frm, text="CATEGORIES",font=('times new roman', 25, 'bold')).grid(row = 0 , column = 3)

        #scrollbar = Scrollbar(cat_frm).pack(side=RIGHT, fill=Y)
        l1 = Label(cat_frm, text="1. SHIRT PRICE 500 EACH",font=('times new roman', 15 )).grid(row = 1 , column = 4)
        l2 = Label(cat_frm, text="2. T-SHIRT PRICE 500 EACH ",font=('times new roman', 15)).grid(row=2, column=4)
        l3 = Label(cat_frm, text="3. PENT PRICE 700 EACH" ,font=('times new roman', 15)).grid(row=3, column=4)
        l4 = Label(cat_frm, text="4. TIE PRICE 100 EACH " ,font=('times new roman', 15)).grid(row=4, column=4)
        l5 = Label(cat_frm, text="5. JOGGERS PRICE 1500 EACH",font=('times new roman', 15) ).grid(row=5, column=4)
        l6 = Label(cat_frm, text="6. TROWSER PRICE 700 EACH",font=('times new roman', 15)).grid(row=6, column=4)
        l7 = Label(cat_frm, text="7. WATCH PRICE 1000 EACH",font=('times new roman', 15) ).grid(row=7, column=4)
        l8 = Label(cat_frm, text="8. KURTA PRICE 400 EACH " ,font=('times new roman', 15)).grid(row=8, column=4)
        l9 = Label(cat_frm, text="9. PAJAMAS PRICE  300 EACH" ,font=('times new roman', 15)).grid(row=8, column=4)

        btn1 = Button(cat_frm, text = 'Back', width = 30 ,height = 2 , command = lambda :[cat_frm.destroy(), self.option()]).grid(row = 10, column = 4)

        # l2 = ("2. T-SHIRT PRICE", self.TShirtsprice)
        #
        # print("3. PENT PRICE", self.pentprice)
        # print("4. TIE PRICE", self.tieprice)
        # print("5. JOGGERS PRICE", self.joggersprice)
        # print("6. TROWSER PRICE", self.trowserprice)
        # print("7. WATCH PRICE ", self.watchesprice)
        # print("8. KURTA PRICE", self.kurtaprice)
        # print("9. PAJAMAS PRICE", self.pajamasprice)
        cat_frm.place(anchor = 'c', relx = .5 , rely = .5)
    def adToCart(self):
        self.a = []
        frame = Frame(self.root)
        l1 = Label(frame, text="USER PANEL\nADD ITEMS TO CART", font=('times new roman', 25, 'bold')).grid(
            row=0,
            column=3)

        # scrollbar = Scrollbar(cat_frm).pack(side=RIGHT, fill=Y)
        l2 = Label(frame, text="1. SHIRT PRICE 500 EACH", font=('times new roman', 15)).grid(row=1, column=4)
        l3 = Label(frame, text="2. T-SHIRT PRICE 500 EACH ", font=('times new roman', 15)).grid(row=2, column=4)
        l4 = Label(frame, text="3. PENT PRICE 700 EACH", font=('times new roman', 15)).grid(row=3, column=4)
        l5 = Label(frame, text="4. TIE PRICE 100 EACH ", font=('times new roman', 15)).grid(row=4, column=4)
        l6 = Label(frame, text="5. JOGGERS PRICE 1500 EACH", font=('times new roman', 15)).grid(row=5, column=4)
        l7 = Label(frame, text="6. TROWSER PRICE 700 EACH", font=('times new roman', 15)).grid(row=6, column=4)
        l8 = Label(frame, text="7. WATCH PRICE 1000 EACH", font=('times new roman', 15)).grid(row=7, column=4)
        l9 = Label(frame, text="8. KURTA PRICE 400 EACH ", font=('times new roman', 15)).grid(row=8, column=4)
        l10 = Label(frame, text="9. PAJAMAS PRICE  300 EACH", font=('times new roman', 15)).grid(row=8, column=4)

        label1 = Label(frame, text='ENTER OPTION NUMBER ', font=('times new roman', 15, 'bold'), fg='black').grid(
            row=10, column=3)
        label2 = Label(frame, text='ENTER QUANTITY YOU WANT TO ADD', font=('times new roman', 15, 'bold'),
                       fg='black').grid(row=11, column=3)
        btn1 = Button(frame, text='ENTER', width=20, command=self.dd).grid(row=14, column=4)
        btn1 = Button(frame, text='BACK', width=20, command=lambda: [frame.destroy(),self.option()]).grid(row=14,column=5)
        #self.d = IntVar()
        #self.n = IntVar()
        self.id = Entry(frame)
        self.id.grid(row=10, column=4)
        self.amount = Entry(frame)
        self.amount.grid(row=11, column=4)
        #self.qq = int(float(self.d.get()))
        #self.oo = int(float(self.n.get()))
        frame.place(anchor='c', relx=.5, rely=.5)


    def dd(self):

        # print(self.id.get())
        # print(self.amount.get())
        if int(self.id.get()) == int(1):
            if int(self.amount.get())>self.shirt:
                messagebox.showinfo(" Sorry ", "we have not enough items")
            else:
                self.a.append([int(self.amount.get()), "SHIRT"])
                self.shirt = self.shirt - int(self.amount.get())
                messagebox.showinfo(str('ADDED SHIRTS SUCCESSFULLY'),str(self.amount.get())+" SHIRTS ADDED ")



        elif int(self.id.get()) == int(2):
            if int(self.id.get())>self.TShirt:
                messagebox.showinfo(" Sorry ", "we have not enough items")
            else:
                self.a.append([int(self.amount.get()), "TSHIRT"])
                self.TShirt -= int(self.amount.get())
                messagebox.showinfo(str('ADDED TSHIRTS SUCCESSFULLY'), str(self.amount.get())+" TSHIRTS ADDED " )



        elif int(self.id.get()) == int(3):
            if int(self.id.get())>self.pent:
                messagebox.showinfo(" Sorry ", "we have not enough items")
            else:
                self.a.append([int(self.amount.get()), "PENT"])
                self.pent -= int(self.amount.get())
                messagebox.showinfo(str('ADDED PENTS SUCCESSFULLY'),str(self.amount.get())+" PENTS ADDED ")


        elif int(self.id.get()) == int(4):
            if int(self.id.get()) > self.tie:
                messagebox.showinfo(" Sorry ", "we have not enough items")
            else:
                self.a.append([int(self.amount.get()), "TIE"])
                self.tie -= int(self.amount.get())
                messagebox.showinfo(str('ADDED TIE SUCCESSFULLY'),str(self.amount.get())+" TIE ADDED ")


        elif int(self.id.get()) == int(5):
            if int(self.id.get())>self.jogger:
                messagebox.showinfo(" Sorry ", "we have not enough items")
            else:
                self.a.append([int(self.amount.get()), "JOGGER"])
                self.jogger -= int(self.amount.get())
                messagebox.showinfo(str('ADDED JOGGERS SUCCESSFULLY'),str(self.amount.get())+" JOGGERS ADDED ")

        elif int(self.id.get()) == int(6):
            if int(self.id.get())>self.Trowser:
                messagebox.showinfo(" Sorry ", "we have not enough items")
            else:
                self.a.append([int(self.amount.get()), "TROWSER"])
                self.Trowser -= int(self.amount.get())
                messagebox.showinfo(str('ADDED TROWSERS SUCCESSFULLY'),str(self.amount.get())+" TROWSER ADDED ")


        elif int(self.id.get()) == int(7):
            if int(self.id.get()) > self.watches:
                messagebox.showinfo(" Sorry ", "we have not enough items")
            else:
                self.a.append([int(self.amount.get()), "WATCH"])
                self.watches -= int(self.amount.get())
                messagebox.showinfo(str('ADDED WATCHES SUCCESSFULLY'),str(self.amount.get())+" WATCH ADDED ")

        elif int(self.id.get()) == int(8):
            if int(self.id.get())>self.kurta:
                messagebox.showinfo(" Sorry ", "we have not enough items")
            else:
                self.a.append([int(self.amount.get()), "KURTA"])
                self.kurta -= int(self.amount.get())
                messagebox.showinfo(str('ADDED KURTA SUCCESSFULLY'),str(self.amount.get())+" KURTA ADDED ")

        elif int(self.id.get()) == int(9):
            if int(self.id.get()) > self.pajama:
                messagebox.showinfo(" Sorry ", "we have not enough items")
            else:
                self.a.append([int(self.amount.get()), "PJAMA"])
                self.pajama -= int(self.amount.get())
                messagebox.showinfo(str('ADDED PAJAMA SUCCESSFULLY'),str(self.amount.get())+" PAJAMAS ADDED ")


    def remove(self):
        #self.category()
        REMfrm = Frame(self.root)
        l1 = Label(REMfrm, text="USER PANEL\nREMOVING ITEMS FROM CART", font=('times new roman', 25, 'bold')).grid(row=0,
                                                                                                         column=3)

        # scrollbar = Scrollbar(cat_frm).pack(side=RIGHT, fill=Y)
        l2 = Label(REMfrm, text="1. SHIRT PRICE 500 EACH", font=('times new roman', 15)).grid(row=1, column=4)
        l3 = Label(REMfrm, text="2. T-SHIRT PRICE 500 EACH ", font=('times new roman', 15)).grid(row=2, column=4)
        l4 = Label(REMfrm, text="3. PENT PRICE 700 EACH", font=('times new roman', 15)).grid(row=3, column=4)
        l5 = Label(REMfrm, text="4. TIE PRICE 100 EACH ", font=('times new roman', 15)).grid(row=4, column=4)
        l6 = Label(REMfrm, text="5. JOGGERS PRICE 1500 EACH", font=('times new roman', 15)).grid(row=5, column=4)
        l7 = Label(REMfrm, text="6. TROWSER PRICE 700 EACH", font=('times new roman', 15)).grid(row=6, column=4)
        l8 = Label(REMfrm, text="7. WATCH PRICE 1000 EACH", font=('times new roman', 15)).grid(row=7, column=4)
        l9 = Label(REMfrm, text="8. KURTA PRICE 400 EACH ", font=('times new roman', 15)).grid(row=8, column=4)
        l10 = Label(REMfrm, text="9. PAJAMAS PRICE  300 EACH", font=('times new roman', 15)).grid(row=8, column=4)


        label1 = Label(REMfrm, text='ENTER OPTION NUMBER ', font=('times new roman', 15, 'bold'), fg='black').grid(
            row=10, column=3)
        label2 = Label(REMfrm, text='ENTER QUANTITY YOU WANT TO ADD', font=('times new roman', 15, 'bold'),
                       fg='black').grid(row=11, column=3)
        btn1 = Button(REMfrm , text = 'ENTER',width = 20 , command = self.mk).grid(row = 14 , column = 4)
        btn1 = Button(REMfrm, text='BACK', width=20, command=lambda :[REMfrm.destroy(), self.option()]).grid(row=14, column=5)

        self.item_id = Entry(REMfrm )
        self.item_id.grid(row=10, column=4)
        self.remove_quantity = Entry(REMfrm)
        self.remove_quantity.grid(row = 11 , column = 4)
        REMfrm.place(anchor = 'c' , relx = .5 , rely = .5)
    def mk(self):

        if int(self.item_id.get())== int(1):
            for i in range(len(self.a)):
                if self.a[i][1] == "SHIRT":
                    if self.a[i][0] >= int(self.remove_quantity.get()):
                        self.a[i][0] = self.a[i][0] - int(self.remove_quantity.get())
                        messagebox.showinfo('Item REMOVED', 'Item Removed sucessfully')
                        break
                    else:
                        messagebox.showinfo('Sorry', 'You have not enough this product in your cart ')
                        break
        elif int(self.item_id.get())== int(2):

            for i in range(len(self.a)):
                if self.a[i][1] == "TSHIRT":
                    if self.a[i][0] >= int(self.remove_quantity.get()):
                        self.a[i][0] = self.a[i][0] - int(self.remove_quantity.get())
                        messagebox.showinfo('Item REMOVED', 'Item Removed sucessfully')

                        break

                    else:
                        messagebox.showinfo('Sorry', 'You have not enough this product in your cart ')
                        break

        elif int(self.item_id.get()) == int(3):
            for i in range(len(self.a)):
                if self.a[i][1] == "PENT":
                    if self.a[i][0] >= int(self.remove_quantity.get()):
                        self.a[i][0] = self.a[i][0] - int(self.remove_quantity.get())
                        messagebox.showinfo('Item REMOVED', 'Item Removed sucessfully')
                        break
                    else:
                        messagebox.showinfo('Sorry', 'You have not enough this product in your cart ')
                        break

        elif int(self.item_id.get()) == int(4):
            for i in range(len(self.a)):
                if self.a[i][1] == "TIE":
                    if self.a[i][0] >= int(self.remove_quantity.get()):
                        self.a[i][0] = self.a[i][0] - int(self.remove_quantity.get())
                        messagebox.showinfo('Item REMOVED', 'Item Removed sucessfully')
                        break
                    else:
                        messagebox.showinfo('Sorry', 'You have not enough this product in your cart ')
                        break

        elif int(self.item_id.get()) == int(5):
            for i in range(len(self.a)):
                if self.a[i][1] == "JOGGER":
                    if self.a[i][0] >= int(self.remove_quantity.get()):
                        self.a[i][0] = self.a[i][0] - int(self.remove_quantity.get())
                        messagebox.showinfo('Item REMOVED', 'Item Removed sucessfully')

                        break
                    else:
                        messagebox.showinfo('Sorry', 'You have not enough this product in your cart ')
                        break

        elif int(self.item_id.get()) == int(6):
            for i in range(len(self.a)):
                if self.a[i][1] == "TROWSER":
                    if self.a[i][0] >= int(self.remove_quantity.get()):
                        self.a[i][0] = self.a[i][0] - int(self.remove_quantity.get())
                        messagebox.showinfo('Item REMOVED', 'Item Removed sucessfully')

                        break
                    else:
                        messagebox.showinfo('Sorry', 'You have not enough this product in your cart ')
                        break


        elif int(self.item_id.get()) == int(7):
            for i in range(len(self.a)):
                if self.a[i][1] == "WATCH":
                    if self.a[i][0] >= int(self.remove_quantity.get()):
                        self.a[i][0] = self.a[i][0] - int(self.remove_quantity.get())
                        messagebox.showinfo('Item REMOVED', 'Item Removed sucessfully')

                        break
                    else:
                        messagebox.showinfo('Sorry', 'You have not enough this product in your cart ')
                        break


        elif int(self.item_id.get()) == int(8):
            for i in range(len(self.a)):
                if self.a[i][1] == "KURTA":
                    if self.a[i][0] >= int(self.remove_quantity.get()):
                        self.a[i][0] = self.a[i][0] - int(self.remove_quantity.get())
                        messagebox.showinfo('Item', 'Remove sucessfully')
                        break

                    else:
                        messagebox.showinfo('Sorry', 'You have not enough this product in your cart ')
                        break

        elif int(self.item_id.get()) == int(9):
            for i in range(len(self.a)):
                if self.a[i][1] == "PAJAMA":
                    if self.a[i][0] >= int(self.remove_quantity.get()):
                        self.a[i][0] = self.a[i][0] - int(self.remove_quantity.get())
                        messagebox.showinfo('Item REMOVED', 'Item Removed sucessfully')
                        break

                    else:
                        messagebox.showinfo('Sorry', 'You have not enough this product in your cart ')
                        break


    def bill(self):


        self.total = 0
        print("__________________________________________")
        print("\n   CUSTOMER BILL     \n")
        self.localtime = time.asctime(time.localtime(time.time()))
        self.Invoice = random.randint(00000000, 99999999)
        print('DATE AND TIME : ' + self.localtime + "\n")
        print('FEE INVOICE : ' + str(self.Invoice) + '\n')
        # self.ff = self.acc_name+'.txt'
        #
        # print(self.ff)
        self.f = open(menu.acc_name +'.txt', "a+")
        self.f.write('DATE AND TIME : '+self.localtime + "\n")
        self.f.write('FEE INVOICE : ' + str(self.Invoice) + '\n')
        frame = Frame(self.root)


        for i in range(len(self.a)):

            if self.a[i][1] == "SHIRT":
                self.total += self.a[i][0] * self.shirtprice
                self.f.write("Shirts Quantity is " + str(self.a[i][0]) + " total price of the Shirt is : " + str(
                    self.a[i][0] * self.shirtprice) + "\n")
                l1 = Label(frame, text = "Shirts Quantity is "+ str(self.a[i][0])+ " total price of the Shirt is : "+
                                         str(self.a[i][0] * self.shirtprice))
                l1.grid(row = 1 , column = 3)
            if self.a[i][1] == "TSHIRT":
                self.total += self.a[i][0] * self.TShirtsprice
                self.f.write("TShirts Quantity is " + str(self.a[i][0]) + " total price of the TShirt is : " +
                             str(self.a[i][0] * self.TShirtsprice) + "\n")
                l2 = Label(frame, text = "TShirts Quantity is "+ str(self.a[i][0])+ " total price of the TShirt is : "+
                      str(self.a[i][0] * self.TShirtsprice))
                l2.grid(row = 2, column=3)
            if self.a[i][1] == "PENT":
                self.total += self.a[i][0] * self.pentprice
                self.f.write("Pents Quantity is " + str(self.a[i][0]) + " total price of the Pent is : " +
                             str(self.a[i][0] * self.pentprice) + "\n")
                l3 = Label(frame,"Pents Quantity is "+ str(self.a[i][0])+ " total price of the Pent is : "+
                      str(self.a[i][0] * self.pentprice))
                l3.grid(row = 3, column = 3)



            if self.a[i][1] == "TIE":
                self.total += self.a[i][0] * self.tieprice
                self.f.write("Tie Quantity is " + str(self.a[i][0]) + " total price of the tie is : " +
                             str(self.a[i][0] * self.tieprice) + "\n")
                l4 = Label(frame, text= "Tie Quantity is "+ str(self.a[i][0])+ " total price of the tie is : "+
                      str(self.a[i][0] * self.tieprice))
                l4.grid(row = 4, column = 3)
            if self.a[i][1] == "JOGGER":
                self.total += self.a[i][0] * self.joggersprice
                self.f.write("Jogger Quantity is " + str(self.a[i][0]) + " total price of the Joggers is : " +
                             str(self.a[i][0] * self.joggersprice) + "\n")
                l5 = Label(frame, text = "Jogger Quantity is "+ str(self.a[i][0])+ " total price of the Joggers is : "+
                      str(self.a[i][0] * self.joggersprice))
                l5.grid(row = 5, column =3)
            if self.a[i][1] == "TROWSER":
                self.total += self.a[i][0] * self.trowserprice
                self.f.write("Trowser Quantity is " + str(self.a[i][0]) + " total price of the Trowser is : " +
                             str(self.a[i][0] * self.trowserprice) + "\n")
                l6 = Label(frame, text = "Trowser Quantity is "+ str(self.a[i][0])+ " total price of the Trowser is : "+
                      str(self.a[i][0] * self.trowserprice))
                l6.grid(row = 6 , column = 3)
            if self.a[i][1] == "WATCH":
                self.total += self.a[i][0] * self.watchesprice
                self.f.write("Watch Quantity is " + self.a[i][0] + " total price of the Watches is : " +
                             str(self.a[i][0] * self.watchesprice) + "\n")
                l7 = Label(frame, text="Watch Quantity is "+ str(self.a[i][0])+ " total price of the Watches is : "+
                      str(self.a[i][0] * self.watchesprice))
                l7.grid(row = 7, column = 3)
            if self.a[i][1] == "KURTA":
                self.total += self.a[i][0] * self.kurtaprice
                self.f.write("Kurta Quantity is " + str(self.a[i][0]) + " total price of the Kurta is : " +
                             str(self.a[i][0] * self.kurtaprice) + "\n")
                l8 = Label(frame, text = "Kurta Quantity is "+ str(self.a[i][0])+ " total price of the Kurta is : "+
                      str(self.a[i][0] * self.kurtaprice))
                l8.grid(row= 8, column = 3)
            if self.a[i][1] == "PAJAMAS":
                self.total += self.a[i][0] * self.pajamasprice
                self.f.write("Pajama Quantity is " + self.a[i][0] + " total price of the Pajama is : " +
                             str(self.a[i][0] * self.pajamasprice) + "\n")
                l9 = Label(frame, text = "Pajama Quantity is "+ str(self.a[i][0])+ " total price of the Pajama is : "+
                      str(self.a[i][0] * self.pajamasprice))
                l9.grid(row = 9, column = 3)

        self.f.write("The total bill of the customer is : " + str(self.total) + "\n")
        label = Label(frame, text= "The total bill of the customer is : "+ str(self.total))
        label.grid(row = 10 , column = 3)
        btn1 = Button(frame, text='BACK', width=20, command=lambda: [frame.destroy(),self.option()]).grid(row=14,column=4)


        self.f.close()
        frame.place(anchor="c",relx = 0.5,rely = 0.5)

    def history(self):

        frame = Frame(self.root)
        #lbl = Label(frame, text= 'HISTORY OF SHOPPING').pack()

        btn1 = Button(frame, text='BACK', width=20, height = 2, command=lambda: [frame.destroy(), self.option()]).grid(row=14,column=5)

        self.lst = []
        self.read(self.acc_name+'.txt',self.lst)
        for i in range(len(self.lst)):
            temp_label = Label(frame,text=self.lst[i])
            temp_label.grid(row=i,column=0)

        frame.place(anchor="c",relx = 0.5,rely = 0.5)

    def Cheakout(self):
        CHKfrm = Frame(self.root)
        l = Label(CHKfrm , text = 'CHEAKOUT\nSHIPPING HERE\nENTER YOUR DETAILS HERE', fg = 'black').grid(row = 0 , column = 4)
        #print("CHEAKOUT\nSHIPPING HERE\nENTER YOUR DETAILS HERE")
        l1 = Label(CHKfrm , text = 'ENTER YOUR NAME : ' , fg = 'black').grid(row = 1, column = 2 )
        l2 = Label(CHKfrm, text = 'ENTER YOUR CITY NAME : ', fg = 'black').grid(row = 2 , column = 2)
        l3 = Label(CHKfrm, text='ENTER YOUR COUNTRY NAME : ', fg='black').grid(row=3, column=2)
        l4 = Label(CHKfrm, text='ENTER YOUR PHONE NUMBER : ', fg='black').grid(row=4, column=2)
        l5 = Label(CHKfrm, text='ENTER YOUR ZIP CODE : ', fg='black').grid(row=5, column=2)
        #_________________________________________________________________________________________________________
        self.i1 = StringVar()
        self.i2 = StringVar()
        self.i3 = StringVar()
        self.i4 = StringVar()
        self.i5 = StringVar()
        #________________________________________________________________________________________________________
        e = Entry(CHKfrm , textvariable = self.i1).grid(row = 1 , column =5 )
        e23 = Entry(CHKfrm, textvariable = self.i2 ).grid(row =2 , column = 5)
        e3 = Entry(CHKfrm, textvariable=self.i3).grid(row=3, column=5)
        e4 = Entry(CHKfrm, textvariable=self.i4).grid(row=4, column=5)
        e5 = Entry(CHKfrm, textvariable=self.i5).grid(row=5, column=5)
        #---------------------------------------------------------------------------------------------------------
        #btn1 = Button(CHKfrm , text = 'CHEAK-OUT' , command = lambda :[CHKfrm.destroy() , self.printCheakout()]).grid(row = 6 , column = 6)
        CHKfrm.place(anchor = 'c' , relx = .5 , rely = .5)




    def printCheakout(self):
        print_frame = Frame(self.root)
        label = Label(print_frame , text ='\nYOUR NAME : '+ str(self.i1.get()) + '\nYOUR CITY NAME : ' + str(self.i2.get()) + '\nYOUR COUNTRY NAME :' + str(self.i3.get()) + '\nYOUR PHONE NUMBER :' +int(self.i4.get())+ '\nYOUR ZIP CODE :' + int(self.i5.get())).grid(row = 2 , column = 2)
        print_frame.place(anchor= 'c' ,relx = .5 , rely = .5)


    def logout(self):
        self.login()

    def option(self):

        option_Frame = Frame(self.root)
        l1 = Label(option_Frame, text='HEY WELCOME : ' + menu.acc_name,  font=('times new roman', 20, 'bold'),  fg='black').grid(row=0, column=0)
        l2 = Label(option_Frame, text='CATEGORY', fg='black').grid(row= 1, column=0)
        l3 = Label(option_Frame, text='ADD TO CART', fg='black').grid(row=2, column=0)
        l4 = Label(option_Frame, text='REMOVE ITEMS', fg='black').grid(row=3, column=0)
        l5 = Label(option_Frame, text='CHEAK-OUT', fg='black').grid(row=4, column=0)
        #l6 = Label(option_Frame, text='CHEAK-OUT', fg='black').grid(row=5, column=0)
        l7 = Label(option_Frame, text='HISTORY', fg='black').grid(row=6, column=0)
        l8 = Label(option_Frame, text='LOG OUT', fg='black').grid(row=7, column=0)
        #--------------------------------------------------------------------------------------------
        btn1 = Button(option_Frame , text = 'VIEW CATEGORY', width = 30 ,height = 2, command = lambda :[option_Frame.destroy() , self.category()]).grid(row = 1 , column = 3)
        btn2 = Button(option_Frame, text='ADD TO CART',width = 30 ,height = 2,
                      command=lambda: [option_Frame.destroy(), self.adToCart()]).grid(row=2, column=3)
        btn3 = Button(option_Frame, text='REMOVE ITEMS', width = 30 ,height = 2,
                      command=lambda: [option_Frame.destroy(), self.remove()]).grid(row=3, column=3)
        btn4 = Button(option_Frame, text='CHEAK-OUT', width = 30 ,height = 2,
                      command=lambda: [option_Frame.destroy(), self.bill()]).grid(row=4, column=3)
        # btn5 = Button(option_Frame, text='CHEAK OUT', width = 30 ,height = 2,
        #               command=lambda: [option_Frame.destroy(), self.Cheakout()]).grid(row=5, column=3)
        btn6 = Button(option_Frame, text='HISTORY', width = 30 ,height = 2,
                      command=lambda: [option_Frame.destroy(), self.history()]).grid(row=6, column=3)
        btn7 = Button(option_Frame, text='LOG OUT', width = 30 ,height = 2,
                      command=lambda: [option_Frame.destroy(), self.logout()]).grid(row=7, column=3)
        btn8 = Button(option_Frame, text='back', width = 30 ,height = 2,
                      command=lambda: [option_Frame.destroy(), self.login()]).grid(row=10, column=0)

        option_Frame.place(anchor='c', relx=.5, rely=.5)

class Admin(menu, Reg):
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg='black')
        self.frame.pack()
    # def __init__(self):
    #     self.r = readDB(self)

    def addAccount(self):
        print('Adding Account...')
        super().signup()

    # def removeAccount(self):
    #     print('Removing Account...')
    #     super().del_records()

    def manageStock(self):
        print('MANAGE STOCK')
        super().addi()

    def calling(self):
        signup = Frame(self.root).pack()
        c = Canvas(signup, width=600, height=600, bg='white')
        # ---------------------------------------------------------------------------------------
        l = Label(c, text='Hey ADMIN !', font=('times new roman', 15, 'bold'), fg='black', bg='white')
        l.grid(row=1, column=5)
        l32 = Label(c, text='', bg='white')
        l32.grid(row=2, column=6)
        l34 = Label(c, text='', bg='white')
        l34.grid(row=3, column=6)

        l1 = Label(c, text='ADD ACCOUNT :', font=('times new roman', 15), fg='black')
        l1.grid(row=4, column=3)
        l7 = Label(c, text='REMOVE ACCOUNT :', font=('times new roman', 15), fg='black')
        l7.grid(row=6, column=3)
        l9 = Label(c, text='MANAGE ITEM STOCK :', font=('times new roman', 15), fg='black')
        l9.grid(row=8, column=3)
        l50 = Label(c, text='', bg='white')
        l50.grid(row=5, column=3)
        l0 = Label(c, text='', bg='white')
        l0.grid(row=7, column=3)
        l0 = Label(c, text='', bg='white')
        l0.grid(row=9, column=3)
        l00 = Label(c, text='', bg='white').grid(row=10, column=6)
        # -------------------------------------------------------------------------------------------
        btn1 = Button(c, text='ADD ACCOUNT', width=20, height=2, command=lambda: [c.destroy(), self.addAccount()]).grid(
            row=4, column=6)
        btn1 = Button(c, text='REMOVE ACCOUNT', width=20, height=2,
                      command=lambda: [c.destroy(), self.delRECORDS()]).grid(row=6, column=6)
        btn1 = Button(c, text='MANAGE ITEM STOCK', width=20, height=2, command=lambda: [c.destroy(), self.addi()]).grid(
            row=8, column=6)
        btn1 = Button(c, text='BACK', width=20, height=2, command=lambda: [c.destroy(), userinterface(self.root)]).grid(
            row=10, column=5)

        # -------------------------------------------------------------------------------------------

        c.place(anchor = 'c', relx = .5 , rely = .5)


class userinterface(Admin):
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg='black')
        # self.bg = ImageTk.PhotoImage(file = 'kill.jpg' )
        # self.bg_image = Label(self.master, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.button1 = tk.Button(self.frame, text='WELCOME TO AES BOUTIQUE', font=('Helvetica', 17, 'bold'), fg='yellow',
                                 bg='black', width=70, height=5, command=lambda: [self.frame.destroy(), self.func()])

        self.button1.pack()
        self.frame.pack()

    def func(self):
        user = Frame(self.root, bg='red').pack()
        # self.bg = ImageTk.PhotoImage(file = 'kill.jpg' )
        # self.bg_image = Label(self.root, image=self.bg).pack()
        c = Canvas(user , width=600, height=600, bg='white')
        # _____________________________________________________________________________________________________
        l = Label(c, text='Hey !', font=('times new roman', 15, 'bold'), fg='black', bg='white')
        l.grid(row=1, column=4)
        l32 = Label(c, text='', bg='white')
        l32.grid(row=2, column=6)
        l34 = Label(c, text='', bg='white')
        l34.grid(row=3, column=6)

        l1 = Label(c, text='Login AS ADMIN :', font=('times new roman', 15), fg='black').grid(row=4, column=3)
        l7 = Label(c, text=' ', font=('times new roman', 15), bg='white').grid(row=6, column=3)
        l9 = Label(c, text='Login AS USER :', font=('times new roman', 15), fg='black').grid(row=8, column=3)
        l50 = Label(c, text='', bg='white')
        l50.grid(row=5, column=3)
        l0 = Label(c, text='', bg='white')
        l0.grid(row=7, column=3)
        l00 = Label(c, text='', bg='white').grid(row=10, column=6)
        # -----------------------------------------------------------------------------------------------------
        btn1 = Button(c, text='ADMIN', width=15, height=2, command=lambda: [c.destroy(), self.calling()]).grid(row=4,
                                                                                                               column=5)

        btn2 = Button(c, text='USER', width=15, height=2, command=lambda: [c.destroy(), self.user()]).grid(row=8,
                                                                                                           column=5)
        # btn3 = Button(c, text='Back', width=15, height=2, command=lambda: [c.destroy(), self.func()]).grid(row=8,column=3)
        c.place(anchor = 'c', relx =.5 , rely = .5)
        # -----------------------------------------------------------------------------------------------------





    def user(self):
        user = Frame(self.root).pack()
        c = Canvas(user, width=600, height=600, bg='white')
        # _____________________________________________________________________________________________________
        l = Label(c, text='Hey USER !', font=('times new roman', 15, 'bold'), fg='black', bg='white')
        l.grid(row=1, column=4)
        l32 = Label(c, text='', bg='white')
        l32.grid(row=2, column=6)
        l34 = Label(c, text='', bg='white')
        l34.grid(row=3, column=6)

        l1 = Label(c, text='Create New Account :', font=('times new roman', 15), fg='black').grid(row=4, column=3)
        l7 = Label(c, text=' ', font=('times new roman', 15), bg='white').grid(row=6, column=3)
        l9 = Label(c, text='Login Account :', font=('times new roman', 15), fg='black').grid(row=8, column=3)
        l50 = Label(c, text='', bg='white')
        l50.grid(row=5, column=3)
        l0 = Label(c, text='', bg='white')
        l0.grid(row=7, column=3)
        l00 = Label(c, text='', bg='white').grid(row=10, column=6)
        # -----------------------------------------------------------------------------------------------------
        btn1 = Button(c, text='SIGN UP', width=15, height=2, command=lambda: [c.destroy(), self.signup()]).grid(row=4,
                                                                                                                column=5)

        btn2 = Button(c, text='LOG IN', width=15, height=2, command=lambda: [c.destroy(), self.login()]).grid(row=8,column=5)
        btn2 = Button(c, text='BACK', width=15, height=2, command=lambda: [c.destroy(), userinterface(self.root)]).grid(row=10,column=3)

        c.place(anchor = 'c', relx = .5 , rely = .5)
        # -----------------------------------------------------------------------------------------------------




def main():
     root = Tk()
     # root = Label(root)
     root.title('AES BOUTIQUE')
     root.state('zoomed')
     app = userinterface(root)
     root.mainloop()

if __name__ == '__main__':
     main()

#
class readDB:

    def delRECORDS(self):

        conn = sqlite3.connect('arbii.db')
        obj = conn.cursor()
        obj.execute('SELECT * FROM records')
        c = obj.fetchall()
        print(c)
        name = input("ENTER  name YOU WANT TO DELETE : ")
        quirry = 'DELETE FROM records WHERE name = ?;'
        conn.execute(quirry, (name,))


        obj.execute('SELECT * FROM records')
        c = obj.fetchall()
        print(c)
        print("ACCOUNT DELETED.....")
        conn.commit()
        conn.close()

#
# r = readDB()
# r.delRECORDS()
