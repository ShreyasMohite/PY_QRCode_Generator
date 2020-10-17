from tkinter import *
import pyqrcode
import tkinter.messagebox


class qrcode:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x400")
        self.root.title("QR CODE GENERATOR")
        self.root.iconbitmap("logo800.ico")
        self.root.resizable(0,0)

        save=StringVar()

    #===============================================================================#
        def on_enter1(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave1(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter2(e):
            but_genarate['background']="black"
            but_genarate['foreground']="cyan"  
        def on_leave2(e):
            but_genarate['background']="SystemButtonFace"
            but_genarate['foreground']="SystemButtonText"


    #============================command=============================================#
        
        def clear():
            save.set("")
            txt.delete("1.0","end")

        def genrate():
            code=txt.get("1.0","end")
            name=save.get()
            if code!="" and name!="":
                qr=pyqrcode.create(code)
                qr.png("{}.png".format(name),scale=8)          
            if code=="" or name=="":
                tkinter.messagebox.showerror("Error","Please enter name and code name")


    #============================frame===============================================#
        
        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=4)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=493,height=295,relief="ridge",bd=4,bg="#736f72")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=493,height=97,relief="ridge",bd=4,bg="#9381ff")
        secondframe.place(x=0,y=295)

    #==============================firstframe==========================================#


        lab_code=Label(firstframe,text="Enter Code",font=('times new roman',14,'roman'),bg="#736f72",fg="white")
        lab_code.place(x=200,y=10)

        txt=Text(firstframe,width=58,height=9,font=('times new roman',12),relief="ridge",bd=3)
        txt.place(x=7,y=40)

        lab_save=Label(firstframe,text="Enter Save AS Name :",font=('times new roman',12),bg="#736f72",fg="white")
        lab_save.place(x=10,y=240)

        ent_save=Entry(firstframe,width=25,relief="ridge",font=('times new roman',12),bd=3,textvariable=save)
        ent_save.place(x=180,y=240)


    #===============================secondframe=========================================#

        but_clear=Button(secondframe,text="Clear",width=20,font=('times new roman',12,'bold'),cursor="hand2",command=clear)
        but_clear.place(x=40,y=30)
        but_clear.bind("<Enter>",on_enter1)
        but_clear.bind("<Leave>",on_leave1)


        but_genarate=Button(secondframe,text="Generate QR Code",width=20,font=('times new roman',12,'bold'),cursor="hand2",command=genrate)
        but_genarate.place(x=250,y=30)
        but_genarate.bind("<Enter>",on_enter2)
        but_genarate.bind("<Leave>",on_leave2)

    #===================================================================================#




if __name__ == "__main__":
    root=Tk()
    app=qrcode(root)
    root.mainloop()
