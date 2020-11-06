import tkinter as tk 
from tkinter import ttk 
  # Creating tkinter window 
window = tk.Tk() 
window.title('WELCOME TO HEALTH CARE') 
window.geometry('500x500') 
window.config(bg="#00b4f5")

ttk.Label(window, text = "PLEASE ENTER THE DETAILS",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 0)

ttk.Label(window, text = "PLEASE SELECT THE TYPE OF PROBLEM :", 
           background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 1, padx = 10, pady = 25) 
  
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
  
monthchoosen.grid(column = 1, row = 1) 
monthchoosen.current() 

ttk.Label(window, text = " PURPOSE OF YOUR VISIT :", 
         background = '#948faf', foreground ="black", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 6, padx = 10, pady = 25) 

ttk.Label(window, text = "SPECIFY THE TYPE OF PROBLEM :",  
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(row = 2, column = 0,padx = 10, pady = 25)

e1 = tk.Entry(window,width='30')
e1.grid(row=2, column=1)

ttk.Label(window, text = "not for those who choose the specific problem",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 10)).grid(row = 3, column = 0)

tk.Label(window, text = "REASON FOR VISIT : ",  
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(row = 6, column = 0)


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
  
monthchoosen.grid(column = 1, row = 6) 
monthchoosen.current()

ttk.Label(window, text = "SPECIFY THE REASON FOR VISIT :",  
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(row =7, column = 0,padx = 10, pady = 25)

e1 = tk.Entry(window,width='30')
e1.grid(column=1 , row=7)

ttk.Label(window, text = "not for those who choose the specific reason for visiting",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 10)).grid(row = 8, column = 0)

button = tk.Button(window, 
                   text="NEXT", 
                   fg="white",
                   bg = "blue",
                   activebackground="lime")

button.grid(row=12, column=1)

window.mainloop()