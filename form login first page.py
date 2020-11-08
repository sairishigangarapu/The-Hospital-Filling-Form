from tkinter import*
import tkinter.font as font
root = Tk()
root.geometry("1600x1200")
root.title('LETS SIGN IN ')
root.config(bg="#00b4f5")
myFont = font.Font(family='Times New Roman', size=14, weight='bold')
Label_0 = Label(root, text="LETS SIGN IN",width=20,font=('Times New Roman',20,'bold'),bg="#00b4f5",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

label_1= Label(root, text="YOUR NAME:",width=20,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_0=Entry(root, font=myFont).pack(anchor = CENTER,padx = 0, pady = 0)

label_1= Label(root, text="PATIENT ID : ",width=20,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_0=Entry(root, font=myFont) .pack(anchor = CENTER,padx = 10, pady = 25)

btn =  Button(root, text='FORGOT PATIENT ID?', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border='0').pack(anchor = CENTER,padx = 10, pady = 25)

label_1= Label(root, text="PASSWORD : ",width=20,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_0=Entry(root, font=myFont,show="*").pack(anchor = CENTER,padx = 10, pady = 25)

btn =  Button(root, text='FORGOT PASSWORD?', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border='0').pack(anchor =CENTER ,padx = 10, pady = 25)

btn =  Button(root, text='NEXT -)', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border='0').pack(anchor = CENTER,padx = 10, pady = 25)
root.mainloop()
