import tkinter as tk 
from tkinter import ttk 
  # Creating tkinter window 
window = tk.Tk() 
window.title('WELCOME TO HEALTH CARE') 
window.geometry('1600x1200') 
window.config(bg="#00b4f5")

ttk.Label(window, text = "PLEASE ENTER THE DETAILS",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 20,'bold')).grid(row = 0, column = 0)

ttk.Label(window, text = "PLEASE SELECT THE TYPE OF PROBLEM :", 
           background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(column = 25, 
          row =1 , pady = 25) 
  
# Combobox creation 
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' heart',  
                          ' bone/muscle', 
                          ' eyesight', 
                          ' joint', 
                          ' throat/ear/nose', 
                          ' mouth(dumb)', 
                          ' deafness', 
                          ' brain', 
                          ' paralysis', 
                          ' disease', 
                          ' others' ) 
  
monthchoosen.grid(column = 35, row = 1) 
monthchoosen.current()  

ttk.Label(window, text = "SPECIFY THE TYPE OF PROBLEM :",  
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(row = 2, column = 25, pady = 25)

e1 = tk.Entry(window,width='30')
e1.grid(row=2, column=35)

ttk.Label(window, text = "not for those who choose the specific problem",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 10)).grid(row = 3, column = 25)

tk.Label(window, text = "REASON FOR VISIT : ",  
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(row = 4, column = 25)


n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' general checkup',  
                          ' dialysis', 
                          ' advanced appointment', 
                          ' operation/surgery', 
                          ' lab diagnostics', 
                          ' lab testing', 
                          ' chemotherapy', 
                          ' lab report pickup', 
                          ' other treatments', 
                          ' scanning', 
                          ' first aid',
                          'Others' ) 
  
monthchoosen.grid(column = 35, row = 4) 
monthchoosen.current()

ttk.Label(window, text = "SPECIFY THE REASON FOR VISIT :",  
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(row =7 ,column = 25,padx = 10, pady = 25)

e1 = tk.Entry(window,width='30')
e1.grid(column=35 , row=7)

ttk.Label(window, text = "not for those who choose the specific reason for visiting",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 10)).grid(row = 8, column = 25)

ttk.Label(window, text = " ENTER FINACIAL  DETAILS",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 20,'bold')).grid(row = 10, column = 0)

ttk.Label(window, text = "MODE OF PAYMENT",  
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(row = 12, column = 23) 

ttk.Radiobutton(window, text="card",value=1,).grid(row=12,column=25)
ttk.Radiobutton(window, text="cash",value=2).grid(row=12,column=26)       
ttk.Radiobutton(window, text="online transaction",value=3).grid(row=13,column=25,pady=15)  
ttk.Radiobutton(window, text="check",value=4,).grid(row=13,column=26,pady=15)       


ttk.Label(window, text = "DO YOU HAVE INSURANCE?",  
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(row =75 ,column = 23,pady=20)

e1 = tk.Entry(window,width='30')
e1.grid(column=25 , row=75)

ttk.Label(window, text = "IF YES PLEASE TELL BANK NAME AND BRANCH",  
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(row =80,column = 23,pady=15)

e1 = tk.Entry(window,width='30')
e1.grid(column=25 , row=80)

button = tk.Button(window, 
                   text="SUBMIT", 
                   fg="white",
                   bg = "blue",
                   activebackground="lime",
                   border = '3')
button.grid(row=100, column=65)
window.mainloop()
