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
ttk.Label(window, text = "NAME : ",
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(column = 0, 
          row = 1, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=1, column=1)

ttk.Label(window, text = "AGE : ", 
          background = '#948faf', foreground ="black", 
          font = ("Times New Roman", 13)).grid(column = 0, 
          row = 2, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=2, column=1)

ttk.Label(window, text = "HOME ADDRESS : ", 
          background = '#948faf', foreground ="black", 
          font = ("Times New Roman", 13)).grid(column = 0, 
          row = 3, padx = 10, pady = 25) 

e1 = tk.Entry(window,width=30)
e1.grid(row=3, column=1)

ttk.Label(window, text = "PHONE NUMBER : ",
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(column = 0, 
          row = 4, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=4, column=1)

ttk.Label(window, text = "HEIGHT in metres (optional) : ", 
          background = '#948faf', foreground ="black", 
          font = ("Times New Roman", 13)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=5, column=1)

ttk.Label(window, text = "WEIGTH in kilograms (optional) :  ", 
          background = '#948faf', foreground ="black",
          font = ("Times New Roman", 13)).grid(column = 0, 
          row = 6, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=6, column=1) 

button = tk.Button(window, 
                   text="NEXT", 
                   fg="white",
                   bg = "blue",
                   activebackground="lime")

button.grid(row=11, column=1)

window.mainloop() 