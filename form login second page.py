import tkinter as tk 
from tkinter import ttk 
  # Creating tkinter window 
window = tk.Tk() 
window.title('WELCOME TO HEALTH CARE') 
window.geometry('500x500') 
window.config(bg="#00b4f5")
  
# label text for title 
ttk.Label(window, text = "PLEASE ENTER THE DETAILS",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 0) 
  
# label 
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
  
# Combobox creation 
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' general checkup',  
                          ' dialysis', 
                          ' advanced appointment', 
                          ' operation/surgery', 
                          ' lab diagnostics', 
                          ' lab testing', 
                          ' therapy(eg:chemotherapy)', 
                          ' lab report pickup', 
                          ' other treatments', 
                          ' scanning', 
                          ' first aid',
                          'Others' ) 
  
monthchoosen.grid(column = 1, row = 6) 
monthchoosen.current() 

ttk.Label(window, text = "NAME : ",
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(column = 0, 
          row = 7, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=7, column=1)

ttk.Label(window, text = "AGE : ", 
          background = '#948faf', foreground ="black", 
          font = ("Times New Roman", 13)).grid(column = 0, 
          row = 8, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=8, column=1)

ttk.Label(window, text = "HEIGHT in metres : ", 
          background = '#948faf', foreground ="black", 
          font = ("Times New Roman", 13)).grid(column = 0, 
          row = 9, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=9, column=1)

ttk.Label(window, text = "WEIGTH in kilograms : ", 
          background = '#948faf', foreground ="black",
          font = ("Times New Roman", 13)).grid(column = 0, 
          row = 10, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=10, column=1) 

button = tk.Button(window, 
                   text="NEXT", 
                   fg="white",
                   bg = "blue",
                   activebackground="lime")

button.grid(row=11, column=3)

window.mainloop() 