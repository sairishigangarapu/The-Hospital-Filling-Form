"""u are the python file or code"""
from tkinter import *
import tkinter as tk


res = op1 = op2 = operation = ''

# code for input
def input_num(digit):
    global op1, op2
    tb1.insert(len(tb1.get()) + 1, digit)
    if op1 == '':
        op1 = tb1.get()

    else:
        op2 = tb1.get()


def input_decimal(decimal):
    tb1.insert(len(tb1.get())+1, decimal)


def input_pie(pie):
    tb1.insert(len(tb1.get())+1, pie)


def square():
    x = float(tb1.get())
    res = x*x
    tb1.delete(0, END)
    tb1.insert(0, 'Ans = ' + str(res))


def cal(choice):
    global operation, op1, op2
    if op2 == '':
        operation = choice
        tb1.delete(0, END)
        tb1.insert(0, "")
    else:
        tb1.delete(0, END)
        tb1.insert(0, "")
        if operation == '+':
            op1 = float(op1) + float(op2)
        elif operation == '-':
            op1 = float(op1) - float(op2)
        elif operation == '*':
            op1 = float(op1) * float(op2)
        elif operation == '/':
            op1 = float(op1) / float(op2)
        op2 = ''
        operation = choice


def reset():
    global operation, op1, op2
    operation = op1 = op2 = ""
    tb1.delete(0, END)
    tb1.insert(0, "")


def result():
    global op2, res, op1
    op2 = tb1.get()
    if operation == '+':
        res = float(op1) + float(op2)
        op1 = res
        tb1.delete(0, END)
        tb1.insert(0, 'Ans = ' + str(float(res)))
    elif operation == '-':
        res = float(op1) - float(op2)
        op1 = res
        tb1.delete(0, END)
        tb1.insert(0, 'Ans = ' + str(float(res)))
    elif operation == '*':
        res = float(op1) * float(op2)
        op1 = res
        tb1.delete(0, END)
        tb1.insert(0, 'Ans = ' + str(float(res)))
    elif operation == '/':
        if float(op2) == 0:
            res = 'Division by Zero Error!'
            tb1.delete(0, END)
            tb1.insert(0, 'Ans = ' + str(res))
        else:
            res = float(op1) / int(op2)
            tb1.delete(0, END)
            tb1.insert(0, 'Ans = ' + str(float(res)))
    elif operation == 'x*x':
        res = int(op1) / int(op2)
        tb1.delete(0, END)
        tb1.insert(0, 'Ans = ' + str(float(res)))
    else:
        res = 'Error!'
        tb1.delete(0, END)
        tb1.insert(0, 'Ans = ' + str(res))


root = tk.Tk()
root.geometry("1200x1200")
root.title("Calculator")
frame1 = Frame(root)
frame1.pack()

tb1 = tk.Entry(root, width='100', font=("Agency FB", 40, "bold"))
tb1.pack(side=TOP, padx=85, pady=10)
btn1 = Button(root, text="1", width=5, height=1, command=lambda: input_num('1'), font=("Agency FB", 25, "bold"))
btn2 = Button(root, text="2", width=5, height=1, command=lambda: input_num('2'), font=("Agency FB", 25, "bold"))
btn1.pack(anchor='nw', padx=100, pady=75)
btn2.pack(anchor='nw', padx=100, pady=75)
btn2.place(x=250, y=160)
btn3 = Button(root, text="3", width=5, height=1, command=lambda: input_num('3'), font=("Agency FB", 25, "bold"))
btn3.pack(anchor='nw', padx=100, pady=75)
# btn3.bind('<Button-1>', input_3)
btn3.place(x=400, y=160)
btn4 = Button(root, text="4", width=5, height=1, command=lambda: input_num('4'), font=("Agency FB", 25, "bold"))
btn4.pack(anchor='nw', padx=100, pady=75)
# btn4.bind('<Button-1>', input_4)
btn4.place(x=100, y=300)
btn5 = Button(root, text="5", width=5, height=1, command=lambda: input_num('5'), font=("Agency FB", 25, "bold"))
btn5.pack(anchor='nw', padx=100, pady=75)
# btn5.bind('<Button-1>', input_5)
btn5.place(x=250, y=300)
btn6 = Button(root, text="6", width=5, height=1, command=lambda: input_num('6'), font=("Agency FB", 25, "bold"))
btn6.pack(anchor='nw', padx=100, pady=75)
# btn6.bind('<Button-1>', input_6)
btn6.place(x=400, y=300)
btn7 = Button(root, text="7", width=5, height=1, command=lambda: input_num('7'), font=("Agency FB", 25, "bold"))
btn7.pack(anchor='nw', padx=100, pady=75)
btn7.place(x=100, y=440)
btn8 = Button(root, text="8", width=5, height=1, command=lambda: input_num('8'), font=("Agency FB", 25, "bold"))
btn8.pack(anchor='nw', padx=100, pady=75)
btn8.place(x=250, y=440)
btn9 = Button(root, text="9", width=5, height=1, command=lambda: input_num('9'), font=("Agency FB", 25, "bold"))
btn9.pack(anchor='nw', padx=100, pady=75)
btn9.place(x=400, y=440)
btn10 = Button(root, text="0", width=5, height=1, command=lambda: input_num('0'), font=("Agency FB", 25, "bold"))
btn10.pack(anchor='nw', padx=100, pady=75)
btn10.place(x=250, y=600)
btn11 = Button(root, text="+", width=5, height=2, command=lambda: cal('+'), font=("Agency FB", "25", "bold"))
btn11.pack(anchor='nw', padx=100, pady=75)
btn11.place(x=750, y=160)
btn12 = Button(root, text="-", width=5, height=2, command=lambda: cal('-'), font=("Agency FB", 25, "bold"))
btn12.pack(anchor='nw', padx=100, pady=75)
btn12.place(x=900, y=160)
btn13 = Button(root, text="/", width=5, height=2, command=lambda: cal('/'), font=("Agency FB", 25, "bold"))
btn13.pack(anchor='nw', padx=100, pady=75,)
btn13.place(x=750, y=300)
btn14 = Button(root, text="*", width=5, height=2, command=lambda: cal('*'), font=("Agency FB", 25, "bold"))
btn14.pack(anchor='nw', padx=100, pady=75)
btn14.place(x=900, y=300)
btn15 = Button(root, text="x*x", width=5, height=2, command=square, font=("Agency FB", 25, "bold"))
btn15.pack(anchor='nw', padx=100, pady=75)
btn15.place(x=750, y=440)
btn14 = Button(root, text="=", width=5, height=1, command=result, font=("Agency FB", 25, "bold"))
btn14.pack(anchor='nw', padx=100, pady=75)
btn14.place(x=100, y=700)
btn15 = Button(root, text=".", width=5, height=2, command=lambda: input_decimal("."), font=("Agency FB", 25, "bold"))
btn15.pack(anchor='nw', padx=100, pady=75)
btn15.place(x=900, y=440)
btn16 = Button(root, text="clear", width=5, height=1, command=reset, font=("Agency FB", 25, "bold"))
btn16.pack(anchor='nw', padx=100, pady=75)
btn16.place(x=400, y=700)
btn16 = Button(root, text="pie", width=5, height=1, command=lambda: input_pie(3.14), font=("Agency FB", 25, "bold"))
btn16.pack(anchor='nw', padx=100, pady=75)
btn16.place(x=800, y=700)
root.mainloop()