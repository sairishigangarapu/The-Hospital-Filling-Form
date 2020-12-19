from tkinter import*
import tkinter.font as font
import webbrowser
import os
root = Tk()
root.geometry("1600x1200")
root.title('EMERGENCY WINDOW')
root.config(bg="#00b4f5")
myFont = font.Font(family='Times New Roman', size=14, weight='bold')
Label_0 = Label(root, text="PLEASE FILL THE DETAILS;MAY GOD BE WITH YOU",width=50,font=('Times New Roman',20,'bold'),bg="#00b4f5",fg="black").pack(anchor = CENTER,padx = 10, pady = 5)

label_1= Label(root, text="PLACE OF ACCCIDENT (AREA,CITY,PINCODE)",width=40,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_0=Entry(root, font=myFont).pack(anchor = CENTER,padx = 0, pady = 0)

label_1= Label(root, text="AGE OF THE PERSON WHO IS IN EMERGENCY",width=40,font=myFont,bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 25)

entry_0=Entry(root, font=myFont) .pack(anchor = CENTER,padx = 10, pady = 25)

label_1= Label(root, text="APPROXIMATE IS ALSO OKAY",width=40,font=('Times New Roman',10,'bold'),bg="#948faf",fg="black").pack(anchor = CENTER,padx = 10, pady = 5)
new = 1
url = "https://www.google.com/maps/search/hospitals+near+me/@12.9548689,77.5734042,15z/data=!3m1!4b1"

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(text='SEND THE SOS', width=20,bg="#948faf",fg='black',font=myFont,activebackground='lime',border = 0,command=openweb).pack(anchor = CENTER,padx = 10, pady = 25)
def ok():
    root = Tk()
frame =Frame(root)
frame.pack()
def openFormFirstPage():
    os.system('python FormFirstPage.py' )
btn = Button(root, text='(-BACK', width=20,bg="blue",fg='white',font=myFont,activebackground='lime',border = 0,command=openFormFirstPage).pack(anchor = CENTER,padx = 10)

root.mainloop()
