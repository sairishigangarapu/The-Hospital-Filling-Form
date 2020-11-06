from tkinter import*
import tkinter.font as font
root = Tk()
root.geometry("500x500")
root.title('LETS SIGN IN ')
root.config(bg="#00b4f5")
myFont = font.Font(family='Times New Roman', size=14, weight='bold')
Label_0 = Label(root, text="LETS SIGN IN",width=20,font=('Times New Roman',20,'bold'),bg="#00b4f5",fg="black")
Label_0.place(x=80 , y = 50)

label_1= Label(root, text="YOUR NAME:",width=20,font=myFont,bg="#948faf",fg="black")
label_1.place(x=10,y= 100 )

entry_0=Entry(root, font=myFont)
entry_0.place(x=250,y = 100)

label_1= Label(root, text="PATIENT ID : ",width=20,font=myFont,bg="#948faf",fg="black")
label_1.place(x=10,y= 150 )

entry_0=Entry(root, font=myFont)
entry_0.place(x=250,y = 150) 

btn =  Button(root, text='FORGOT PATIENT ID?', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border='0').place(x=250,y=200)

label_1= Label(root, text="PASSWORD : ",width=20,font=myFont,bg="#948faf",fg="black")
label_1.place(x=10,y= 250 )

entry_0=Entry(root, font=myFont,show="*")
entry_0.place(x=250,y = 250) 

btn =  Button(root, text='FORGOT PASSWORD?', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border='0').place(x=250,y=300)

btn =  Button(root, text='NEXT -)', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border='0').place(x=250,y=400)
root.mainloop()