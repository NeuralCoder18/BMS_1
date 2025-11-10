import tkinter as tk
from tkinter import ttk

import mysql.connector
class bank():
    def __init__(self,root):
        self.root=root
        self.root.title("Bank Management") 
        scrn_width=self.root.winfo_screenwidth()
        scrn_height=self.root.winfo_screenheight()

        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")
        mainLabel=tk.Label(self.root,text="Bank Management System",font=("Times Roman",40,"bold"),bg="dark blue",bd=5,relief="raised")
        mainLabel.pack(side="top",fill="x")
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
        style.map("Blue.TButton",
                  background=[("active", "deepskyblue"),("pressed","white")])
        openAcBtn=ttk.Button(mainFrame,command=self.openAc,text="Open Account",style="Blue.TButton")
        
        openAcBtn.place(x=80,y=40,width=280,height=60)

        dpLabel=tk.Label(mainFrame,text="To Deposit",font=("Times Roman",20,"bold"))
        dpLabel.place(x=160,y=130)

        dpBtn=ttk.Button(mainFrame,text="Deposit",style="Blue.TButton")
        dpBtn.place(x=80,y=170,width=280,height=60)

        wtLabel=tk.Label(mainFrame,text="To withdraw",font=("Times Roman",20,"bold"))
        wtLabel.place(x=160,y=260)

        dpBtn=ttk.Button(mainFrame,text="Withdraw",style="Blue.TButton")
        dpBtn.place(x=80,y=300,width=280,height=60)
        
    def openAc(self):
        self.openAcFrame=tk.Frame(self.root,bg="light gray",bd=5,relief="ridge")
        self.openAcFrame.place(x=500,y=90,width=450,height=550)
        usNameLabel=tk.Label(self.openAcFrame,text="User Name",bg="light gray",font=("arial",))
        

root=tk.Tk()
root.configure(background="white")
obj=bank(root)
root.mainloop()