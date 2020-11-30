from tkinter import*
import tkinter.font as font
import os
root = Tk()
root.geometry("1600x1200")
root.title('LETS SIGN IN ')
root.config(bg="#00b4f5")
myFont = font.Font(family='Times New Roman', size=14, weight='bold')
Label_0 = Label(root, text="PLEASE FILL THE DETAILS",width=50,font=('Times New Roman',20,'bold'),bg="#00b4f5",fg="black").pack(anchor = CENTER,padx = 10, pady = 5)

label_1= Label(root, text="NAME",width=10,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_0=Entry(root, font=myFont).pack(anchor = CENTER,padx = 0, pady = 0)

label_1= Label(root, text="DEPARTMENT OF SPECIALISATION",width=40,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_0=Entry(root, font=myFont) .pack(anchor = CENTER,padx = 10, pady = 25)

label_1= Label(root, text="DOCTOR ID",width=15,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_0=Entry(root, font=myFont).pack(anchor = CENTER,padx = 0, pady = 0)

label_1= Label(root, text="NAME OF THE HOSPITAL(WORKPLACE)",width=50,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_0=Entry(root, font=myFont).pack(anchor = CENTER,padx = 0, pady = 0)

label_1= Label(root, text="PASSWORD",width=15,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_0=Entry(root, font=myFont,show="*").pack(anchor = CENTER,padx = 0, pady = 0)

btn = Button(root, text='LOGIN-)', width=20,bg="#948faf",fg='black',font=myFont,activebackground='lime',border = 0).pack(anchor = CENTER,padx = 10, pady = 25)
def ok():
    root = Tk()
frame =Frame(root)
frame.pack()
def openFormFirstPage():
    os.system('python FormFirstPage.py' )
btn = Button(root, text='(-BACK', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border = 0,command=openFormFirstPage).pack(anchor = CENTER,padx = 10)
root.mainloop()