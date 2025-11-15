import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector
class bank():
    def __init__(self,root):
        self.root=root
        #creating frame with title bank management system
        self.root.title("Bank Management") 
        scrn_width=self.root.winfo_screenwidth()
        scrn_height=self.root.winfo_screenheight()

        self.root.configure(bg="white")

        # Force all Entry widgets to be readable
        self.root.option_add("*Entry.background", "white")
        self.root.option_add("*Entry.foreground", "black")
        self.root.option_add("*Entry.insertBackground", "black")   # cursor color
        self.root.option_add("*Entry.font", "Times 15")

        self.mainFrame = None         
        self.openAcFrame = None       
        self.submitFrame = None  
        #=====================================
        #      CONNECTION TO MY SQL          |||||||
        #=====================================
        self.db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.db.cursor()



        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")
        #main label
        mainLabel=tk.Label(self.root,text="Bank Management System",font=("Times Roman",40,"bold"),bg="dark blue",bd=5,relief="raised")
        mainLabel.pack(side="top",fill="x")

        self.create_main_frame()
        #================
        #  MAIN FRAME    |||
        #================

    def create_main_frame(self):
        
        if self.openAcFrame:
            self.openAcFrame.destroy()
        

        self.mainFrame=tk.Frame(self.root,bg="light gray",bd=5,relief="ridge")
        self.mainFrame.place(x=500,y=90,width=450,height=550)
        opLabel=tk.Label(self.mainFrame,text="To Open Account Click Below",font=("Times Roman",20,"bold"))
        opLabel.place(x=90,y=0)
        style = ttk.Style()
        style.theme_use("clam")

        # Blue button (default theme)
        style.configure(
            "Blue.TButton",
            font=("Arial", 20, "bold"),
            background="light blue",
            foreground="black",
            relief="raised",
            padding=10

        )
        #defining background of blue button
        style.map("Blue.TButton",
                  background=[("active", "deepskyblue"),("pressed","white")])
        
        #add openAc button
        openAcBtn=ttk.Button(self.mainFrame,command=self.openAc,text="Open Account",style="Blue.TButton")
        
        openAcBtn.place(x=80,y=40,width=280,height=60)
        #add deposit label
        dpLabel=tk.Label(self.mainFrame,text="To Deposit",font=("Times Roman",20,"bold"))
        dpLabel.place(x=160,y=130)

        #add deposit button
        dpBtn=ttk.Button(self.mainFrame,command=self.deposit,text="Deposit",style="Blue.TButton")
        dpBtn.place(x=80,y=170,width=280,height=60)

        #add withdraw label
        wtLabel=tk.Label(self.mainFrame,text="To withdraw",font=("Times Roman",20,"bold"))
        wtLabel.place(x=160,y=260)

        #add withdraw button
        wtBtn=ttk.Button(self.mainFrame,text="Withdraw",style="Blue.TButton")
        wtBtn.place(x=80,y=300,width=280,height=60)
        #defining function of openAc button
    def openAc(self):
        if self.mainFrame:
            self.mainFrame.destroy()
        #================================================
        #OPENAC FRAME (FUNCTION OF OPEN ACCOUNT BUTTON) ||
        #================================================
        self.openAcFrame=tk.Frame(self.root,bg="light gray",bd=5,relief="ridge")
        self.openAcFrame.place(x=240,y=90,width=1000,height=700)

        #add label of personal detail
        infoLabel=tk.Label(self.openAcFrame,text="Fill Your Personal Detail",font=("Times Roman",20,"bold"))
        infoLabel.place(x=40,y=0)
        
        #adding to show user name input gui and taking entry
        usNameLabel=tk.Label(self.openAcFrame,text="Your Name :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        usNameLabel.grid(row=0,column=0,padx=20,pady=30)
        self.usnameIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.usnameIn.grid(row=0,column=1,padx=20,pady=30)
     
        
        #adding to show father name input gui and taking entry
        usfNameLabel=tk.Label(self.openAcFrame,text="Father Name :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        usfNameLabel.grid(row=1,column=0,padx=20,pady=30)
        self.usfnameIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.usfnameIn.grid(row=1,column=1,padx=20,pady=30)
        
        #adding to show mother name input gui and taking entry
        usmNameLabel=tk.Label(self.openAcFrame,text="Mother Name :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        usmNameLabel.grid(row=2,column=0,padx=20,pady=30)
        self.usmnameIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.usmnameIn.grid(row=2,column=1,padx=20,pady=30)
        
         #adding to show gender input gui and taking entry
        genLabel=tk.Label(self.openAcFrame,text="Gender :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        genLabel.grid(row=3,column=0,padx=20,pady=30)
        self.genIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.genIn.grid(row=3,column=1,padx=20,pady=30)
        
         #adding to show nationality input gui and taking entry
        natLabel=tk.Label(self.openAcFrame,text="Nationality :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        natLabel.grid(row=4,column=0,padx=20,pady=30)
        self.natIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.natIn.grid(row=4,column=1,padx=20,pady=30)

        #add label of contact detail
        contactLabel=tk.Label(self.openAcFrame,text="Fill Your Contact Detail",font=("Times Roman",20,"bold"))
        contactLabel.place(x=40,y=430)

         #adding to show phone number input gui and taking entry
        conLabel=tk.Label(self.openAcFrame,text="Phone Number :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        conLabel.grid(row=5,column=0,padx=20,pady=30)
        self.conIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.conIn.grid(row=5,column=1,padx=20,pady=30)
        
         #adding to show email address input gui and taking entry
        emailLabel=tk.Label(self.openAcFrame,text="Email Id :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        emailLabel.grid(row=6,column=0,padx=20,pady=30)
        self.emailIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.emailIn.grid(row=6,column=1,padx=20,pady=30)

          #adding to show aadhar no input gui and taking entry
        aadharLabel=tk.Label(self.openAcFrame,text="Aadhar no. :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        aadharLabel.grid(row=7,column=0,padx=20,pady=30)
        self.aadharIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.aadharIn.grid(row=7,column=1,padx=20,pady=30)

        #add label of address
        addLabel=tk.Label(self.openAcFrame,text="Fill Your Address Detail",font=("Times Roman",20,"bold"))
        addLabel.place(x=650,y=0)
        #
        #add empty space

        self.openAcFrame.grid_columnconfigure(2, minsize=100)
        self.openAcFrame.grid_columnconfigure(3, minsize=100)
        self.openAcFrame.grid_columnconfigure(4, minsize=100)
        


        #adding to show village input gui and taking entry
        villLabel=tk.Label(self.openAcFrame,text="Village :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        villLabel.grid(row=0,column=5,padx=20,pady=30)
        self.villIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.villIn.grid(row=0,column=6,padx=20,pady=30)
        
        #adding to show district input gui and taking entry
        distLabel=tk.Label(self.openAcFrame,text="District :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        distLabel.grid(row=1,column=5,padx=20,pady=30)
        self.distIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.distIn.grid(row=1,column=6,padx=20,pady=30)

        #adding to show state input gui and taking entry
        stateLabel=tk.Label(self.openAcFrame,text="State :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        stateLabel.grid(row=2,column=5,padx=20,pady=30)
        self.stateIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.stateIn.grid(row=2,column=6,padx=20,pady=30)

        #adding to show pin code input gui and taking entry
        pincLabel=tk.Label(self.openAcFrame,text="Pin Code :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        pincLabel.grid(row=3,column=5,padx=20,pady=30)
        self.pincIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.pincIn.grid(row=3,column=6,padx=20,pady=30)

         #add label of Nominee
        nomLabel=tk.Label(self.openAcFrame,text="Fill Your Nominee Detail",font=("Times Roman",20,"bold"))
        nomLabel.place(x=660,y=350)

         #adding to nominee name input gui and taking entry
        nomLabel=tk.Label(self.openAcFrame,text="Nominee Name :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        nomLabel.grid(row=4,column=5,padx=20,pady=30)
        self.nomIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.nomIn.grid(row=4,column=6,padx=20,pady=30)

         #adding to relationship with nominee input gui and taking entry
        relLabel=tk.Label(self.openAcFrame,text="Relationship :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        relLabel.grid(row=5,column=5,padx=20,pady=30)
        self.relIn=tk.Entry(self.openAcFrame,width=15,font=("Times Roman",15))
        self.relIn.grid(row=5,column=6,padx=20,pady=30)

        submitBtn=ttk.Button(self.openAcFrame,text="Submit",command=self.final_submit,style="Blue.TButton")
        submitBtn.grid(row=7,column=6,padx=20,pady=10)

        backBtn=ttk.Button(self.openAcFrame,text="Back",command=self.create_main_frame,style="Blue.TButton")
        backBtn.grid(row=7,column=5,padx=20,pady=10)
    def final_submit(self):
        
       success=self.save_database()
       if success:
            self.create_main_frame()
    
    #=====================================
    #     SAVING INFORMATION TO DATABASE  ||
    #=====================================
    def save_database(self):
        name = self.usnameIn.get()
        father = self.usfnameIn.get()
        mother = self.usmnameIn.get()
        gender = self.genIn.get()
        nationality = self.natIn.get()
        phone = self.conIn.get()
        email = self.emailIn.get()
        aadhar = self.aadharIn.get()
        village = self.villIn.get()
        district = self.distIn.get()
        state = self.stateIn.get()
        pincode = self.pincIn.get()
        nominee = self.nomIn.get()
        relation = self.relIn.get()

        required_fields = [name, father, mother, gender, nationality, phone, email, aadhar, village, district, state, pincode, nominee, relation]
    
        if any(field == "" for field in required_fields):
            messagebox.showerror("Error", "⚠️ Please fill all fields before submitting.")
            return  False



        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Error", "📱 Phone number must be 10 digits.")
            return False

        if not aadhar.isdigit() or len(aadhar) != 12:
            messagebox.showerror("Error", "🆔 Aadhar number must be 12 digits.")
            return False

        if not pincode.isdigit() or len(pincode) != 6:
            messagebox.showerror("Error", "📮 Pincode must be 6 digits.")
            return False
    #================================
    #   INSERT TO MY SQL        |||||
    #=================================  
        self.cursor.execute("""INSERT INTO accounts (name, father_name, mother_name, gender, nationality, phone, email, aadhar, village, district, state, pincode, nominee_name, relationship) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (name, father, mother, gender, nationality, phone, email, aadhar, village, district, state, pincode, nominee, relation))
    
   
        self.db.commit()

        account_id = self.cursor.lastrowid  
        
        bank_code = "BNK"
        year = datetime.datetime.now().year
        custom_number = f"{bank_code}{year}-{account_id:08d}"

        
        self.cursor.execute(
            "UPDATE accounts SET account_number = %s WHERE id = %s",
            (custom_number, account_id)
        )

        self.db.commit()

        messagebox.showinfo("Success", f"Account Created!\nYour Account Number: {custom_number}")



        return True
    
    #. Defining function of deposit button
    def deposit(self):
        if self.mainFrame:
            self.mainFrame.destroy()
        #================================================
        #DEPOSIT FRAME (FUNCTION OF DEPOSIT BUTTON) ||
        #================================================
        self.depositFrame=tk.Frame(self.root,bg="light gray",bd=5,relief="ridge")
        self.depositFrame.place(x=500,y=90,width=450,height=550)

        #add label of money being deposited
        depoLabel=tk.Label(self.depositFrame,text="Amount to be deposited",font=("Times Roman",20,"bold"))
        depoLabel.place(x=120,y=10)

        self.depositFrame.grid_columnconfigure(0, minsize=60)
        self.depositFrame.grid_rowconfigure(0, minsize=40)

        #adding to show user name
        usenameLabel=tk.Label(self.depositFrame,text="User Name :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        usenameLabel.grid(row=1,column=1,padx=20,pady=30)
        self.usenameIn=tk.Entry(self.depositFrame,width=15,font=("Times Roman",15))
        self.usenameIn.grid(row=1,column=2,padx=20,pady=30)

        #adding to show account_number
        acLabel=tk.Label(self.depositFrame,text="Account Number :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        acLabel.grid(row=2,column=1,padx=20,pady=30)
        self.acIn=tk.Entry(self.depositFrame,width=15,font=("Times Roman",15))
        self.acIn.grid(row=2,column=2,padx=20,pady=30)
       
        
        #adding to show money being deposited
        depoLabel=tk.Label(self.depositFrame,text="Amount :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        depoLabel.grid(row=3,column=1,padx=20,pady=30)
        self.depoIn=tk.Entry(self.depositFrame,width=15,font=("Times Roman",15))
        self.depoIn.grid(row=3,column=2,padx=20,pady=30)

         #adding to show confirm money being deposited
        condepoLabel=tk.Label(self.depositFrame,text="Confirm Amount :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        condepoLabel.grid(row=4,column=1,padx=20,pady=30)
        self.condepoIn=tk.Entry(self.depositFrame,width=15,font=("Times Roman",15))
        self.condepoIn.grid(row=4,column=2,padx=20,pady=30)

        #adding for description
        desLabel=tk.Label(self.depositFrame,text="Description :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        desLabel.grid(row=5,column=1,padx=20,pady=30)
        self.payment_type = ttk.Combobox(self.depositFrame, width=10,values=["Cash", "Online", "UPI", "Cheque"])
        self.payment_type.set("Cash")
        self.payment_type.grid(row=5,column=2,padx=20,pady=10)

        #adding for submit button
        submitBtn=ttk.Button(self.depositFrame,text="Submit",command=self.finalsubmit,style="Blue.TButton")
        submitBtn.grid(row=6,column=2,padx=20,pady=10)

        #adding for back button
        backBtn=ttk.Button(self.depositFrame,text="Back",command=self.create_main_frame,style="Blue.TButton")
        backBtn.grid(row=6,column=1,padx=20,pady=10)

    def finalsubmit(self):
        
        success=self.savedatabase()
        if success:
            self.create_main_frame()
    
    #=====================================
    #     COMPLETE DEPOSIT DATABASE LOGIC
    #=====================================
    def savedatabase(self):
        username = self.usenameIn.get()
        account_number = self.acIn.get()
        deposit_amt = self.depoIn.get()
        confirm_amt = self.condepoIn.get()
        p_type= self.payment_type.get()

        # EMPTY CHECK
        if username == "" or account_number == "" or deposit_amt == "" or confirm_amt == "":
            messagebox.showerror("Error", "⚠ Please fill all fields.")
            return False

        # AMOUNT MATCH
        if deposit_amt != confirm_amt:
            messagebox.showerror("Error", "❌ Amounts do not match.")
            return False

        # VALID FLOAT CHECK
        try:
            deposit_amt = float(deposit_amt)
        except:
            messagebox.showerror("Error", "❌ Enter a valid numeric amount.")
            return False

        if deposit_amt < 1:
            messagebox.showerror("Error", "❌ Minimum deposit is ₹1.")
            return False

        # VERIFY ACCOUNT EXISTS
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = %s and LOWER(name)=LOWER(%s)",
            (account_number,username)
        )
        result = self.cursor.fetchone()

        if not result:
            messagebox.showerror("Error", "❌ Invalid Account Number.")
            return False

        current_balance = result[0]

        # UPDATE BALANCE
        new_balance = current_balance + deposit_amt

        self.cursor.execute(
            "UPDATE accounts SET balance = %s WHERE account_number = %s",
            (new_balance, account_number)
        )
        self.cursor.execute(
        "INSERT INTO deposit_history (account_no, amount, date_time, description) VALUES (%s, %s, NOW(), %s)",
        (account_number, deposit_amt, self.payment_type.get()))
        self.db.commit()

        messagebox.showinfo("Success",
                            f"₹{deposit_amt} Deposited Successfully!\n"
                            f"New Balance: ₹{new_balance}")

        return True


            
            

        





root=tk.Tk()
root.configure(background="white")
obj=bank(root)
root.mainloop()