from tkinter import*
import tkinter.font as font
import os
root = Tk()
root.geometry("1600x1200")
root.title('LETS SIGN IN ')
root.config(bg="#00b4f5")
myFont = font.Font(family='Times New Roman', size=14, weight='bold')
Label_0 = Label(root, text="LETS SIGN UP",width=20,font=('Times New Roman',20,'bold'),bg="#00b4f5",fg="black").pack(anchor = CENTER,padx = 10, pady = 5)

label_1= Label(root, text="YOUR NAME(PATIENT):",width=25,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 5)

entry_0=Entry(root, font=myFont).pack(anchor = CENTER,padx = 0, pady = 0)

label_1= Label(root, text="PHONE NUMBER ",width=20,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 5)

entry_0=Entry(root, font=myFont) .pack(anchor = CENTER,padx = 10, pady = 5)

label_1= Label(root, text='EMAIL', width=20,bg="#948faf",fg='black',font=myFont,activebackground='lime',border='0').pack(anchor = CENTER,padx = 10, pady = 5)

entry_0=Entry(root, font=myFont) .pack(anchor = CENTER,padx = 10, pady = 5)

label_1= Label(root, text="HOME ADDRESS ",width=20,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 5)

entry_0=Entry(root, font=myFont,width=90).pack(anchor = CENTER,padx = 10, pady = 5)

label_1= Label(root, text="HOSPITAL NAME",width=20,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 5)

entry_0=Entry(root, font=myFont).pack(anchor = CENTER,padx = 10, pady = 5)

label_1= Label(root, text="IF PATIENT COMES ;  FOR WHAT PURPOSE",width=40,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 5)

entry_0=Entry(root, font=myFont).pack(anchor = CENTER,padx = 10, pady = 5)

label_1= Label(root, text="FOR HOW MANY TIMES A COMES TO THE HOSPITAL",width=50,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 5)

entry_0=Entry(root, font=myFont).pack(anchor = CENTER,padx = 10, pady = 5)

label_1= Label(root, text="PLEASE SPECIFY THE AREA OF THE HOSPITAL",width=50,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 5)

entry_0=Entry(root, font=myFont).pack(anchor = CENTER,padx = 10, pady = 5)

btn =  Button(root, text='NEXT -)', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border='0').pack(anchor = CENTER,padx = 10, pady = 5)
def ok():
    root = Tk()
frame =Frame(root)
frame.pack()
def openFormFirstPage():
    os.system('python FormFirstPage.py' )
btn = Button(root, text='(-BACK', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border = 0,command=openFormFirstPage).pack(anchor = CENTER,padx = 10)
root.mainloop()
