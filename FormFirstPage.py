from tkinter import*
import tkinter.font as font
import os
root = Tk()
root.geometry("1600x1200")
root.title('WELCOME TO HEALTH CARE',)
root.config(bg="#00b4f5")
myFont = font.Font(family='Times New Roman', size=10, weight='bold')
photo = PhotoImage(file =r"C:\SAI RISHI\red cross.png")
Button(root, text = 'Click Me !', image = photo).pack(side =TOP,pady=13)
label_0 = Label(root, text="Welcome To _____ Health Services",width=50,font=("Agency FB",25,"bold"),bg="#00b4f5",fg="black").pack(anchor = CENTER,padx = 10, pady = 15)
label_0 = Label(root, text="For Any Additional Queries call-\n __________",width=50,font=("Agency FB",20,"bold"),bg="#00b4f5",fg="black").pack(anchor="nw")
def ok():
    root = Tk()
frame =Frame(root)
frame.pack()
def openLoginPage():
    os.system('python LoginFirstPage.py' )
btn = Button(root, text='LOGIN(IF YOU ARE A REGULAR PATIENT)', width=50,bg="#948faf",fg='black',font=myFont,activebackground='lime',border = 0,command=openLoginPage).pack(anchor = CENTER,padx = 10, pady = 15)
def ok():
    root = Tk()
frame =Frame(root)
frame.pack()
def openSignUp():
    os.system('python SignUp.py' )
btn = Button(root, text='NEW HERE ? SIGN UP', width=20,bg="#948faf",fg='black',font=myFont,activebackground='lime',border = 0,command=openSignUp).pack(anchor = CENTER,padx = 10, pady = 15)
btn = Button(root, text='ABOUT US', width=20,bg="#948faf",fg='black',font=myFont,activebackground='lime',border = 0).pack(anchor = CENTER,padx = 10, pady = 15)
def ok():
    root = Tk()
frame =Frame(root)
frame.pack()
def openOneTimeAppointmentForThePatient():
    os.system('python OneTimeAppointmentForThePatient.py' )
btn = Button(root, text='ONE TIME APPOINTMENT?CLICK THIS', width=50,bg="#948faf",fg='black',font=myFont,activebackground='lime',border = 0,command=openOneTimeAppointmentForThePatient).pack(anchor = CENTER,padx = 10, pady = 15)
def ok():
    root = Tk()
frame =Frame(root)
frame.pack()
def openLoginWindowForDoctor():
    os.system('python LoginWindowForDoctor.py' )
btn = Button(root, text='DOCTORS CLICK HERE', width=50,bg="#948faf",fg='black',font=myFont,activebackground='lime',border = 0,command=openLoginWindowForDoctor).pack(anchor = CENTER,padx = 10, pady = 15)
def ok():
    root = Tk()
frame =Frame(root)
frame.pack()
def openEmergencyWindowForPatient():
    os.system('python EmergencyWindowForPatient.py' )
btn = Button(root, text='EMERGENCY?CLICK HERE', width=50,bg="red",fg='white',font=myFont,activebackground='lime',border = 0,command=openEmergencyWindowForPatient).pack(anchor = CENTER,padx = 10, pady = 15)
btn = Button(root, text='WANT MEDICINE? CLICK HERE', width=50,bg="#948faf",fg='black',font=myFont,activebackground='lime',border = 0).pack(anchor = CENTER,padx = 10, pady = 25)

root.mainloop()
