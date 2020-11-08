import tkinter as tk 
from tkinter import ttk 
  # Creating tkinter window 
window = tk.Tk() 
window.title('WELCOME TO HEALTH CARE') 
window.geometry('1600x1200') 
window.config(bg="#00b4f5")
  
# label text for title 
ttk.Label(window, text = "PLEASE ENTER THE DETAILS",  
          background = '#00b4f5', foreground ="black",  
          font = ("Times New Roman", 20,'bold')).grid(row = 0, column = 35, pady = 10) 
  
# label 
ttk.Label(window, text = "NAME : ",
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(column = 50, 
          row = 1, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=1, column=55)

ttk.Label(window, text = "AGE : ", 
          background = '#948faf', foreground ="black", 
          font = ("Times New Roman", 13)).grid(column = 50, 
          row = 3, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=3, column=55)

ttk.Label(window, text = "HOME ADDRESS : ", 
          background = '#948faf', foreground ="black", 
          font = ("Times New Roman", 13)).grid(column = 50, 
          row = 5, padx = 10, pady = 25) 

e1 = tk.Entry(window,width=30)
e1.grid(row=5, column=55)

ttk.Label(window, text = "PHONE NUMBER : ",
          background = '#948faf', foreground ="black",  
          font = ("Times New Roman", 13)).grid(column = 50, 
          row = 7, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=7, column=55)

ttk.Label(window, text = "HEIGHT in metres (optional) : ", 
          background = '#948faf', foreground ="black", 
          font = ("Times New Roman", 13)).grid(column = 50, 
          row = 9, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=9, column=55)

ttk.Label(window, text = "WEIGHT in kilograms (optional) :  ", 
          background = '#948faf', foreground ="black",
          font = ("Times New Roman", 13)).grid(column = 50, 
          row = 11, padx = 10, pady = 25) 

e1 = tk.Entry(window,width='30')
e1.grid(row=11, column=55) 

button = tk.Button(window, 
                   text="NEXT", 
                   fg="white",
                   bg = "blue",
                   activebackground="lime")

button.grid(row=13, column=1000)

window.mainloop() 
