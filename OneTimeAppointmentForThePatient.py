from tkinter import*
import tkinter.font as font
import os
root = Tk()
root.geometry("1600x1200")
root.title('LETS SIGN IN ')
root.config(bg="#00b4f5")
myFont = font.Font(family='Times New Roman', size=14, weight='bold')

label_1=Label(root,text = "PLEASE ENTER THE DETAILS",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 20,'bold')).grid(row = 0, column = 35, pady = 10) 

label_2=Label(root, text = "NAME PLEASE:",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 15,'bold')).grid(row = 1, column = 40, pady = 10) 

entry_0=Entry(root, font=myFont).grid(row = 1, column = 45, pady = 10) 

label_2=Label(root, text = "HOME ADDRESS:",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 15,'bold')).grid(row = 2, column = 40, pady = 10) 

entry_0=Entry(root, font=myFont).grid(row = 2, column = 45, pady = 10) 

label_2=Label(root, text = "PHONE NUMBER:",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 15,'bold')).grid(row = 3, column = 40, pady = 10) 

entry_0=Entry(root, font=myFont).grid(row = 3, column = 45, pady = 10) 


label_1=Label(root,text = "PATIENT DETAILS",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 20,'bold')).grid(row = 5, column = 35, pady = 10) 

label_2=Label(root, text = "PATIENT NAME:",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 15,'bold')).grid(row = 6, column = 40, pady = 10) 

entry_0=Entry(root, font=myFont).grid(row = 6, column = 45, pady = 10) 

label_2=Label(root, text = "DATE OF BIRTH(DD/MM/YYYY):",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 15,'bold')).grid(row = 7, column = 40, pady = 10) 

entry_0=Entry(root, font=myFont).grid(row = 7, column = 45, pady = 10) 

label_2=Label(root, text = "PATIENT AGE:",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 15,'bold')).grid(row = 8, column = 40, pady = 10) 

entry_0=Entry(root, font=myFont).grid(row = 8, column = 45, pady = 10) 

label_1=Label(root,text = "PROBLEM OF THE PATIENT:",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 15,'bold')).grid(row = 9, column = 40, pady = 10) 

entry_0=Entry(root, font=myFont).grid(row = 9, column = 45, pady = 10) 

label_1=Label(root,text = "Assumptions are also okay",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 13,'bold')).grid(row = 10, column = 45) 

label_1=Label(root, text = " ENTER FINACIAL DETAILS",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 20,'bold')).grid(row = 12, column = 0)

label_1=Label(root, text = "MODE OF PAYMENT :",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 15,'bold')).grid(row = 13, column = 40) 

entry_0=Entry(root, font=myFont).grid(row = 13, column = 45, pady = 10) 

btn = Button(root, text='BOOK CONSULTATION', width=20,bg="#948faf",fg='black',font=myFont,activebackground='lime',border = 0).grid(row=17,column=50)
def ok():
    root = Tk()
frame =Frame(root)
def openFormFirstPage():
    os.system('python FormFirstPage.py' )
btn = Button(root, text='(-BACK', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border = 0,command=openFormFirstPage).grid(row=18,column=50,pady=5)

root.mainloop()