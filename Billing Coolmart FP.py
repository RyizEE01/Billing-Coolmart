from tkinter import *
import random

class main:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1280,height = 700)
        self.root.minsize(width = 1280,height = 700)
        self.root.title("Billing CoolMart")

        #Variabel
        self.customer_name = StringVar()
        self.phone = StringVar()
        #random bill numbers
        x = random.randint(1000,9999)
        self.bill_no = StringVar()

        #Value ke variable
        self.bill_no.set(str(x))
        self.sabun = IntVar()
        self.body_lotion = IntVar()
        self.shampo = IntVar()
        self.sikat_gigi = IntVar()
        self.odol = IntVar()
        self.minyak_goreng = IntVar()
        self.gula = IntVar()
        self.tepung = IntVar()
        self.roti = IntVar()
        self.selai = IntVar()
        self.biskuit = IntVar()
        self.harga_total = StringVar()
        
    def total(self):
        self.harga_totals = (
            (self.sabun.get() *2000)+
            (self.body_lotion.get() *7000)+
            (self.shampo.get() *5000)+
            (self.sikat_gigi.get() *2500)+
            (self.odol.get() *7000)+ 
            (self.minyak_goreng.get() *15000)+
            (self.gula.get() *10000)+
            (self.tepung.get() *10000)+
            (self.roti.get() *2000)+
            (self.selai.get() *5000)+
            (self.biskuit.get() *1000)
        )
        self.harga_total.set("Rp. "+str(self.harga_totals))
    #text
    def welcome_soft(self):
        self.txt.delete("1.0",END)
        self.txt.insert(END,"       Billing CoolMart\n")
        self.txt.insert(END,f"\nBill No. : {str(self.bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.customer_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nProduct          Qty         Price")
        self.txt.insert(END,"\n===================================")
    #clear bill area
    def clear(self):
        self.txt.delete('1.0',END)

    #text bill
    def bill_area(self):
        self.welcome_soft()
        if self.sabun.get() != 0:
            self.txt.insert(END,f"\nSabun              {self.sabun.get()}           {self.sabun.get() * 2000}")
        if self.body_lotion.get() != 0:
            self.txt.insert(END,f"\nBody Lotion        {self.body_lotion.get()}           {self.body_lotion.get() * 7000}")
        if self.shampo.get() != 0:
            self.txt.insert(END,f"\nShampo             {self.shampo.get()}           {self.shampo.get() * 5000}")
        if self.sikat_gigi.get() != 0:
            self.txt.insert(END,f"\nSikat Gigi         {self.sikat_gigi.get()}           {self.sikat_gigi.get() * 2500}")
        if self.odol.get() != 0 :
            self.txt.insert(END,f"\nOdol               {self.odol.get()}           {self.odol.get() * 7000}")
        if self.minyak_goreng.get() != 0:
            self.txt.insert(END,f"\nMinyak Goreng      {self.minyak_goreng.get()}           {self.minyak_goreng.get() * 15000}")
        if self.gula.get() != 0:
            self.txt.insert(END,f"\nGula               {self.gula.get()}           {self.gula.get() * 10000}")
        if self.tepung.get() != 0:
            self.txt.insert(END,f"\nTepung             {self.tepung.get()}           {self.tepung.get() * 10000}")
        if self.roti.get() != 0:
            self.txt.insert(END,f"\nRoti               {self.roti.get()}           {self.roti.get() * 2000}")
        if self.selai.get() != 0:
            self.txt.insert(END,f"\nSelai              {self.selai.get()}           {self.selai.get() * 5000}")
        if self.biskuit.get() != 0:
            self.txt.insert(END,f"\nBiskuit            {self.biskuit.get()}           {self.biskuit.get() * 1000}")
        
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                      Total : {self.harga_totals}")

    #exit
    def exit(self):
        self.root.destroy()

    def harga(self):
        roo = Tk()
        roo.geometry("500x500+0+0")
        roo.title("Daftar Harga")
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="ITEM", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="Harga", fg="black", bd=5)
        lblinfo.grid(row=0, column=3)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="Sabun", fg="black", bd=5)
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="2000", fg="black", bd=5)
        lblinfo.grid(row=1, column=3)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="Body Lotion", fg="black", bd=5)
        lblinfo.grid(row=2, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="7000", fg="black", bd=5)
        lblinfo.grid(row=2, column=3)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="Shampo", fg="black", bd=5)
        lblinfo.grid(row=3, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="5000", fg="black", bd=5)
        lblinfo.grid(row=3, column=3)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="Sikat Gigi", fg="black", bd=5)
        lblinfo.grid(row=4, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="2500", fg="black", bd=5)
        lblinfo.grid(row=4, column=3)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="Odol", fg="black", bd=5)
        lblinfo.grid(row=5, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="7000", fg="black", bd=5)
        lblinfo.grid(row=5, column=3)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="Minyak Goreng", fg="black", bd=5)
        lblinfo.grid(row=6, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="15000", fg="black", bd=5)
        lblinfo.grid(row=6, column=3)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="Gula", fg="black", bd=5)
        lblinfo.grid(row=7, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="10000", fg="black", bd=5)
        lblinfo.grid(row=7, column=3)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="tepung", fg="black", bd=5)
        lblinfo.grid(row=8, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="10000", fg="black", bd=5)
        lblinfo.grid(row=8, column=3)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="Roti", fg="black", bd=5)
        lblinfo.grid(row=9, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="2000", fg="black", bd=5)
        lblinfo.grid(row=9, column=3)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="Selai", fg="black", bd=5)
        lblinfo.grid(row=10, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="5000", fg="black", bd=5)
        lblinfo.grid(row=10, column=3)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="Biskuit", fg="black", bd=5)
        lblinfo.grid(row=11, column=0)
        lblinfo = Label(roo, font=("Bahnschrift",10, "bold"), text="1000", fg="black", bd=5)
        lblinfo.grid(row=11, column=3)
       
       #title/judul
        judul = Label(self.root, text = "Billing CoolMart", font = ('Bahnschrift',12, 'bold', 'underline'))
        #costumer
        F1 = LabelFrame(text = "Customer Details",font = ('Bahnschrift',12, 'bold'))
        F1.place(x = 0,y = 80,relwidth = 1)
        cname = Label(F1, text = "Nama",font = ("Bahnschrift",12, "bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cphone = Label(F1, text = "NO.HP",font = ("Bahnschrift",12, "bold")).grid(row = 0,column = 2,padx = 20)
        bill = Label(F1, text = "Bill No.",font = ("Bahnschrift",12, "bold")).grid(row = 0,column = 4,padx = 20)
        
        #menu
        F2 = LabelFrame(self.root,text = 'Menu',font = ("Bahnschrift",12, "bold"))
        F2.place(x = 5,y = 180,width = 325,height = 380)
        F5 = LabelFrame(self.root,text = 'Menu',font = ("Bahnschrift",12, "bold"))
        F5.place(x = 330,y = 180,width = 325,height = 380)
        sabun = Label(F2,text = "Sabun",font = ("Bahnschrift",10, "bold")).grid(row = 0,column = 0,padx = 10,pady = 20)
        body = Label(F2,text = "Body Lotion",font = ("Bahnschrift",10, "bold")).grid(row = 1,column = 0,padx = 10,pady = 20)
        shampo = Label(F2,text = "Shampo" ,font = ("Bahnschrift",10, "bold")).grid(row = 2,column = 0,padx = 10,pady = 20)
        sikat = Label(F2,text = "Sikat Gigi" ,font = ("Bahnschrift",10, "bold")).grid(row = 3,column = 0,padx = 10,pady = 20)
        odol = Label(F2,text = "Odol" ,font = ("Bahnschrift",10, "bold")).grid(row = 4,column = 0,padx = 10,pady = 20)
        minyak = Label(F2,text = "Minyak Goreng" ,font = ("Bahnschrift",10, "bold")).grid(row = 5,column = 0,padx = 10,pady = 20)
        gula = Label(F5,text = "Gula" ,font = ("Bahnschrift",10, "bold")).grid(row = 6,column = 0,padx = 10,pady = 20)
        tepung = Label(F5,text = "Tepung" ,font = ("Bahnschrift",10, "bold")).grid(row = 7,column = 0,padx = 10,pady = 20)
        roti = Label(F5,text = "Roti" ,font = ("Bahnschrift",10, "bold")).grid(row = 8,column = 0,padx = 10,pady = 20)
        selai = Label(F5,text = "Selai" ,font = ("Bahnschrift",10, "bold")).grid(row = 9,column = 0,padx = 10,pady = 20)
        biskuit = Label(F5,text = "Biskuit" ,font = ("Bahnschrift",10, "bold")).grid(row = 10,column = 0,padx = 10,pady = 20)
        #entry costumer
        ename = Entry(F1,font = ("Bahnschrift",10, "bold"),textvariable = self.customer_name)
        ename.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)
        ephone = Entry(F1,font = ("Bahnschrift",10, "bold"),textvariable = self.phone)
        ephone.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)
        ebill = Entry(F1,font = ("Bahnschrift",10, "bold"),textvariable = self.bill_no)
        ebill.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        #entry menu
        esabun = Entry(F2,font = ("Bahnschrift",10, "bold"),textvariable = self.sabun)
        esabun.grid(row = 0, column = 1,ipady = 5,ipadx = 5)
        ebody = Entry(F2,font = ("Bahnschrift",10, "bold"),textvariable = self.body_lotion)
        ebody.grid(row = 1, column = 1,ipady = 5,ipadx = 5)
        eshampo = Entry(F2,font = ("Bahnschrift",10, "bold"),textvariable = self.shampo)
        eshampo.grid(row = 2, column = 1,ipady = 5,ipadx = 5)
        esikat = Entry(F2,font = ("Bahnschrift",10, "bold"),textvariable = self.sikat_gigi)
        esikat.grid(row = 3, column = 1,ipady = 5,ipadx = 5)
        eodol = Entry(F2,font = ("Bahnschrift",10, "bold"),textvariable = self.odol)
        eodol.grid(row = 4, column = 1,ipady = 5,ipadx = 5)
        eminyak = Entry(F2,font = ("Bahnschrift",10, "bold"),textvariable = self.minyak_goreng)
        eminyak.grid(row = 5, column = 1,ipady = 5,ipadx = 5)
        egula = Entry(F5,font = ("Bahnschrift",10, "bold"),textvariable = self.gula)
        egula.grid(row = 6, column = 1,ipady = 5,ipadx = 5)
        etepung = Entry(F5,font = ("Bahnschrift",10, "bold"),textvariable = self.tepung)
        etepung.grid(row = 7, column = 1,ipady = 5,ipadx = 5)
        eroti = Entry(F5,font = ("Bahnschrift",10, "bold"),textvariable = self.roti)
        eroti.grid(row = 8, column = 1,ipady = 5,ipadx = 5)
        eselai = Entry(F5,font = ("Bahnschrift",10, "bold"),textvariable = self.selai)
        eselai.grid(row = 9, column = 1,ipady = 5,ipadx = 5)
        ebiskuit = Entry(F5,font = ("Bahnschrift",10, "bold"),textvariable = self.biskuit)
        ebiskuit.grid(row = 10, column = 1,ipady = 5,ipadx = 5)

        #bill area
        F3 = Label(self.root,font = ("Bahnschrift",12, "bold"))
        F3.place(x = 960,y = 180,width = 325,height = 380)
        bill_title = Label(F3,text = "Billing CoolMart" ,font = ("Bahnschrift",12, "bold"))
        bill_title.pack(fill = X)

        #scroll
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)
        #button
        F4 = LabelFrame(self.root,text = "Bill Menu",font = ("Bahnschrift",12, "bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 145)
        total = Label(F4,text = "Total",font = ("Bahnschrift",12, "bold"))
        total.grid(row = 0,column = 0,padx = 10,pady = 0)
        etotal = Entry(F4,font = ("Bahnschrift",12, "bold"), textvariable = self.harga_total)
        etotal.grid(row = 0,column = 1,ipady = 2,ipadx = 5)
        total_btn = Button(F4,text = "Total",font = ("Bahnschrift",12, "bold"),command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)
        clear_btn = Button(F4,text = "Clear",font = ("Bahnschrift",12, "bold"),command = self.clear)
        clear_btn.grid(row = 1,column = 5,ipadx = 20,padx = 30)
        exit_btn = Button(F4,text = "Exit",font = ("Bahnschrift",12, "bold"),command = self.exit)
        exit_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)
        harga_btn = Button(F4,text = "harga",font = ("Bahnschrift",12, "bold"),command = self.harga)
        harga_btn.grid(row = 1,column = 7,ipadx = 20,padx = 30)
        genbill_btn = Button(F4,text = "Generate Bill",font = ("Bahnschrift",12, "bold"),command = self.bill_area)
        genbill_btn.grid(row = 1,column = 8,ipadx = 20)
        
root = Tk()
object = main(root)
root.mainloop()
        







        
