from tkinter import*
import tkinter.font as font
import os
root = Tk()
root.geometry("1600x1200")
root.title('LETS SIGN IN ')
root.config(bg="#00b4f5")
myFont = font.Font(family='Times New Roman', size=14, weight='bold')
Label_0 = Label(root, text="LETS SIGN IN",width=20,font=('Times New Roman',20,'bold'),bg="#00b4f5",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

label_1= Label(root, text="YOUR NAME:",width=20,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_1=Entry(root, font=myFont).pack(anchor = CENTER,padx = 0, pady = 0)

label_2= Label(root, text="PATIENT ID : ",width=20,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_2=Entry(root, font=myFont) .pack(anchor = CENTER,padx = 10, pady = 25)

btn_1 =  Button(root, text='FORGOT PATIENT ID?', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border='0').pack(anchor = CENTER,padx = 10, pady = 25)

label_3= Label(root, text="PASSWORD : ",width=20,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_3=Entry(root, font=myFont,show="*").pack(anchor = CENTER,padx = 10, pady = 25)

btn_2 =  Button(root, text='FORGOT PASSWORD?', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border='0').pack(anchor =CENTER ,padx = 10, pady = 25)
def ok():
    root = Tk()
frame =Frame(root)
frame.pack()
def openLoginSecondPage():
    os.system('python LoginSecondPage.py' )
btn_3 =  Button(root, text='NEXT -)', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border='0',command=openLoginSecondPage).pack(anchor = CENTER,padx = 10, pady = 25)
def ok():
    root = Tk()
frame =Frame(root)
frame.pack()
def openFormFirstPage():
    os.system('python FormFirstPage.py' )
btn_4 = Button(root, text='(-BACK', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border = 0,command=openFormFirstPage).pack(anchor = CENTER,padx = 10)
root.mainloop()
