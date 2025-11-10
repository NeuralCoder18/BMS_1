import tkinter as tk
from tkinter import ttk

import mysql.connector
class bank():
    def __init__(self,root):
        self.root=root
        #creating frame with title bank management system
        self.root.title("Bank Management") 
        scrn_width=self.root.winfo_screenwidth()
        scrn_height=self.root.winfo_screenheight()

        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")
        #main label
        mainLabel=tk.Label(self.root,text="Bank Management System",font=("Times Roman",40,"bold"),bg="dark blue",bd=5,relief="raised")
        mainLabel.pack(side="top",fill="x")
        #frame for operation
        mainFrame=tk.Frame(self.root,bg="light gray",bd=5,relief="ridge")
        mainFrame.place(x=500,y=90,width=450,height=550)
        opLabel=tk.Label(mainFrame,text="To Open Account Click Below",font=("Times Roman",20,"bold"))
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
        openAcBtn=ttk.Button(mainFrame,command=self.openAc,text="Open Account",style="Blue.TButton")
        
        openAcBtn.place(x=80,y=40,width=280,height=60)
        #add deposit label
        dpLabel=tk.Label(mainFrame,text="To Deposit",font=("Times Roman",20,"bold"))
        dpLabel.place(x=160,y=130)

        #add deposit button
        dpBtn=ttk.Button(mainFrame,text="Deposit",style="Blue.TButton")
        dpBtn.place(x=80,y=170,width=280,height=60)

        #add withdraw label
        wtLabel=tk.Label(mainFrame,text="To withdraw",font=("Times Roman",20,"bold"))
        wtLabel.place(x=160,y=260)

        #add withdraw button
        wtBtn=ttk.Button(mainFrame,text="Withdraw",style="Blue.TButton")
        wtBtn.place(x=80,y=300,width=280,height=60)
        #defining function of openAc button
    def openAc(self):
        self.openAcFrame=tk.Frame(self.root,bg="light gray",bd=5,relief="ridge")
        self.openAcFrame.place(x=240,y=90,width=1000,height=700)

        #add label of personal detail
        infoLabel=tk.Label(self.openAcFrame,text="Fill Your Personal Detail",font=("Times Roman",20,"bold"))
        infoLabel.place(x=40,y=0)
        
        #adding to show user name input gui and taking entry
        usNameLabel=tk.Label(self.openAcFrame,text="Your Name :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        usNameLabel.grid(row=0,column=0,padx=20,pady=30)
        self.usnameIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.usnameIn.grid(row=0,column=1,padx=20,pady=30)
        
        #adding to show father name input gui and taking entry
        usfNameLabel=tk.Label(self.openAcFrame,text="Father Name :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        usfNameLabel.grid(row=1,column=0,padx=20,pady=30)
        self.usfnameIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.usfnameIn.grid(row=1,column=1,padx=20,pady=30)
        
        #adding to show mother name input gui and taking entry
        usmNameLabel=tk.Label(self.openAcFrame,text="Mother Name :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        usmNameLabel.grid(row=2,column=0,padx=20,pady=30)
        self.usmnameIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.usmnameIn.grid(row=2,column=1,padx=20,pady=30)
        
         #adding to show gender input gui and taking entry
        genLabel=tk.Label(self.openAcFrame,text="Gender :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        genLabel.grid(row=3,column=0,padx=20,pady=30)
        self.genIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.genIn.grid(row=3,column=1,padx=20,pady=30)
        
         #adding to show nationality input gui and taking entry
        natLabel=tk.Label(self.openAcFrame,text="Nationality :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        natLabel.grid(row=4,column=0,padx=20,pady=30)
        self.natIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.natIn.grid(row=4,column=1,padx=20,pady=30)

        #add label of contact detail
        contactLabel=tk.Label(self.openAcFrame,text="Fill Your Contact Detail",font=("Times Roman",20,"bold"))
        contactLabel.place(x=40,y=430)

         #adding to show phone number input gui and taking entry
        conLabel=tk.Label(self.openAcFrame,text="Phone Number :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        conLabel.grid(row=5,column=0,padx=20,pady=30)
        self.conIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.conIn.grid(row=5,column=1,padx=20,pady=30)
        
         #adding to show email address input gui and taking entry
        emailLabel=tk.Label(self.openAcFrame,text="Email Id :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        emailLabel.grid(row=6,column=0,padx=20,pady=30)
        self.emailIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.emailIn.grid(row=6,column=1,padx=20,pady=30)

        #add label of address
        addLabel=tk.Label(self.openAcFrame,text="Fill Your Address Detail",font=("Times Roman",20,"bold"))
        addLabel.place(x=650,y=0)

        #add empty space

        self.openAcFrame.grid_columnconfigure(2, minsize=100)
        self.openAcFrame.grid_columnconfigure(3, minsize=100)
        self.openAcFrame.grid_columnconfigure(4, minsize=100)
        


        #adding to show village input gui and taking entry
        villLabel=tk.Label(self.openAcFrame,text="Village :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        villLabel.grid(row=0,column=5,padx=20,pady=30)
        self.villIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.villIn.grid(row=0,column=6,padx=20,pady=30)
        
        #adding to show district input gui and taking entry
        distLabel=tk.Label(self.openAcFrame,text="District :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        distLabel.grid(row=1,column=5,padx=20,pady=30)
        self.distIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.distIn.grid(row=1,column=6,padx=20,pady=30)

        #adding to show state input gui and taking entry
        stateLabel=tk.Label(self.openAcFrame,text="State :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        stateLabel.grid(row=2,column=5,padx=20,pady=30)
        self.stateIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.stateIn.grid(row=2,column=6,padx=20,pady=30)

        #adding to show pin code input gui and taking entry
        pincLabel=tk.Label(self.openAcFrame,text="Pin Code :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        pincLabel.grid(row=3,column=5,padx=20,pady=30)
        self.pincIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.pincIn.grid(row=3,column=6,padx=20,pady=30)

         #add label of Nominee
        nomLabel=tk.Label(self.openAcFrame,text="Fill Your Nominee Detail",font=("Times Roman",20,"bold"))
        nomLabel.place(x=660,y=350)

         #adding to nominee name input gui and taking entry
        nomLabel=tk.Label(self.openAcFrame,text="Nominee Name :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        nomLabel.grid(row=4,column=5,padx=20,pady=30)
        self.nomIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.nomIn.grid(row=4,column=6,padx=20,pady=30)

         #adding to relationship with nominee input gui and taking entry
        relLabel=tk.Label(self.openAcFrame,text="Relationship :",bg="light gray",fg="black",font=("Times Roman",15,"bold"))
        relLabel.grid(row=5,column=5,padx=20,pady=30)
        self.relIn=tk.Entry(self.openAcFrame,fg="white",width=15,font=("Times Roman",15))
        self.relIn.grid(row=5,column=6,padx=20,pady=30)

        submitBtn=ttk.Button(self.openAcFrame,text="Submit",command=self.submit,style="Blue.TButton")
        submitBtn.grid(row=7,column=6,padx=20,pady=10)

    def submit(self):
        self.submitFrame=tk.Frame(self.root,bg="light gray",bd=5,relief="ridge")
        self.submitFrame.place(x=240,y=90,width=1000,height=700)

        #add label of password
        nomLabel=tk.Label(self.submitFrame,text="Password Section",font=("Times Roman",30,"bold"))
        nomLabel.place(x=350,y=0)
        #add space
        self.submitFrame.grid_columnconfigure(1, minsize=100)
        self.submitFrame.grid_columnconfigure(2, minsize=100)
        self.submitFrame.grid_columnconfigure(3, minsize=80)

        self.submitFrame.grid_rowconfigure(1, minsize=70)

        #adding to show password input gui and taking entry
        passcLabel=tk.Label(self.submitFrame,text="Password :",bg="light gray",fg="black",font=("Times Roman",25,"bold"))
        passcLabel.grid(row=2,column=4,padx=20,pady=30)
        self.passIn=tk.Entry(self.submitFrame,fg="white",width=15,font=("Times Roman",25))
        self.passIn.grid(row=2,column=5,padx=20,pady=30)

         #adding to show confirm password input gui and taking entry
        cnfpasscLabel=tk.Label(self.submitFrame,text="Confirm Password :",bg="light gray",fg="black",font=("Times Roman",25,"bold"))
        cnfpasscLabel.grid(row=3,column=4,padx=20,pady=30)
        self.cnfpassIn=tk.Entry(self.submitFrame,fg="white",width=15,font=("Times Roman",25))
        self.cnfpassIn.grid(row=3,column=5,padx=20,pady=30)

        self.submitFrame.grid_rowconfigure(1, minsize=50)
        # self.submitFrame.grid_columnconfigure(4, minsize=10)
        #add label of note
        noteLabel=tk.Label(self.submitFrame,text="Note: Don't share your password",font=("Times Roman",15,"bold"))
        noteLabel.place(x=300,y=230)

        submitBtn=ttk.Button(self.submitFrame,text="Submit",style="Blue.TButton")
        submitBtn.grid(row=5,column=4,padx=20,pady=10)


root=tk.Tk()
root.configure(background="white")
obj=bank(root)
root.mainloop()