from tkinter import *

expression = ""

#updating experssion 
def press(num):
    global expression   #update the new one 
    expression += str(num)  #concatenation(sequence) of the string 
    equation.set(expression)    #update the expersion after we added it to the string 
    
def equalpress():
    try:
        global expression
        total = str(eval(expression))   
        equation.set(total)
        expression = ""     #initialze the expression variable 
    except:
        equation.set(" Error ")  #if some error happens
        expression = ""

def clear():    #clear the content basically the C
    global expression
    expression = ""
    equation.set("")
    
if __name__ ==  "__main__":
    #create the window here
    gui = Tk()
    gui.configure(background = '#949BAD')
    gui.title('Project 1.0 : calulator')
    gui.geometry('300x190')
    equation = StringVar()
    expression_field = Entry(gui, textvariable = equation)
    expression_field.place(height=100)
    expression_field.grid(columnspan = 4, ipadx = 91)
    equation.set(" ")
    
    num_one = Button(gui, text=' 1 ', fg='black', bg='#CDD4E4', command=lambda: press(1), height=1, width=7, padx = 10, pady = 10)
    num_one.grid(row = 2, column =0)
    
    num_two = Button(gui, text=' 2 ', fg='black', bg='#CDD4E4', command=lambda: press(2), height=1, width=7, padx = 10, pady = 10)
    num_two.grid(row = 2, column =1)
    
    num_three = Button(gui, text=' 3 ', fg='black', bg='#CDD4E4', command=lambda: press(3), height=1, width=7, padx = 10, pady = 10)
    num_three.grid(row = 2, column =2)
    
    plus = Button(gui, text = '+', fg = 'black', bg = '#666A72', command = lambda: press("+"), height = 1, width = 7, padx = 10, pady = 10)
    plus.grid(row = 2, column = 3)

    num_four = Button(gui, text=' 4 ', fg='black', bg='#CDD4E4', command=lambda: press(4), height=1, width=7, padx = 10, pady = 10)
    num_four.grid(row = 3, column =0)
    
    num_five = Button(gui, text=' 5 ', fg='black', bg='#CDD4E4', command=lambda: press(5), height=1, width=7, padx = 10, pady = 10)
    num_five.grid(row = 3, column =1)
    
    num_six = Button(gui, text=' 6 ', fg='black', bg='#CDD4E4', command=lambda: press(6), height=1, width=7, padx = 10, pady = 10)
    num_six.grid(row = 3, column =2)
    
    sub =Button(gui, text = '-', fg = 'black', bg = '#666A72', command = lambda: press("-"), height = 1, width = 7, padx = 10, pady = 10)
    sub.grid(row = 3, column = 3)
    
    num_sev = Button(gui, text=' 7 ', fg='black', bg='#CDD4E4', command=lambda: press(7), height=1, width=7, padx = 10, pady = 10)
    num_sev.grid(row = 4, column =0)
    
    num_eight = Button(gui, text=' 8 ', fg='black', bg='#CDD4E4', command=lambda: press(8), height=1, width=7, padx = 10, pady = 10)
    num_eight.grid(row = 4, column =1)
    
    num_nine = Button(gui, text=' 9 ', fg='black', bg='#CDD4E4', command=lambda: press(9), height=1, width=7, padx = 10, pady = 10)
    num_nine.grid(row = 4, column =2)
    
    mult = Button(gui, text = '*', fg = 'black', bg = '#666A72', command = lambda: press("*"), height = 1, width = 7, padx = 10, pady = 10)
    mult.grid(row = 4, column = 3)
    
    num_zero = Button(gui, text=' 0 ', fg='black', bg='#CDD4E4', command=lambda: press(0), height=1, width=7, padx = 10, pady = 10)
    num_zero.grid(row = 5, column =0)
    
    divide = Button(gui, text=' / ', fg='black', bg='#666A72', command=lambda: press("/"), height=1, width=7, padx = 10, pady = 10) 
    divide.grid(row=5, column=3) 

    equal = Button(gui, text=' = ', fg='black', bg='#666A72',command=equalpress, height=1, width=7, padx = 10, pady = 10) 
    equal.grid(row=5, column=2) 
    
    clear = Button(gui, text='Clear', fg='black', bg='#99322B',command=clear, height=1, width=7, padx = 10, pady = 10) 
    clear.grid(row=5, column='1') 
    
    gui.mainloop()
    
