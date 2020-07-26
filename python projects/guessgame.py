from tkinter import *
import random

window = Tk()
window.geometry('400x200')
window.title('Guess Game Project 0.1.1')
window.configure(bg = '#bae1ff')
window.wm_iconbitmap('py.png')


#/////// Functions \\\\\\#


computer_guess = random.randint(1,10)
#we need a command for the reset and the check!

def check():
    user_guess = int(txt_guess.get())
    if user_guess < computer_guess:
        msg = 'Higher'
    elif user_guess > computer_guess:
        msg = 'Lower'
    elif user_guess == computer_guess:
        msg = 'Correct' 
    else:
        msg = 'Something went wrong'   
    
    bloop['text'] = msg
    
def reset():
    global computer_guess
    computer_guess = random.randint(1,10)
    bloop['text'] = 'Game restart'

def easy():
    global computer_guess
    computer_guess = random.randint(1,10)
    bloop['text'] = 'Game set to Easy'
 
def medium():
    global computer_guess
    computer_guess = random.randint(10,50)   
    bloop['text'] = 'Game set to Med' 

def hard():
    global computer_guess
    computer_guess = random.randint(10,100)
    bloop['text'] = 'Game set to Hard'


#////////// WIDGETS \\\\\\\\\\\#


intro = Label(window, text = 'Welcome to the guessing game ', font = 'Times 20 bold', bg ='#ffb3ba')
intro.place(height = 50, width = 400)

bloop = Label(window, text = 'Game started, GL', bg = '#bae1ff', font ='Times 10' )
bloop.place(x= 158, y = 50)

txt_guess = Entry(window, width=12, font ='Times 15 bold', justify = 'center')
txt_guess.place(x = 150, y = 80)


#:::buttons::: we need a restart button to repeat the game, a check bottom, and a quit bottom 


Quit = Button(window,text = 'Quit', command = quit, bg = '#ffdfba', font = 'Times 10 ')
Quit.place(x = 320, y = 60 , height = 125, width = 60)

restart = Button(window, text = 'Restart', bg ='#ffdfba', font = 'Times 11', command = reset)
restart.place(x = 150, y = 155, height = 30, width = 125)

check = Button(window, text = 'Check', bg = '#ffdfba',font = 'Times 11', command = check)
check.place(x = 150, y = 120, height = 30, width = 125)

easy = Button(window, text = 'Easy level', bg = '#baffc9', font = 'Times 11', command = easy)
easy.place(x = 10, y = 60)

medium = Button(window, text = 'Medium level', bg = '#baffc9', font = 'Times 11', command = medium)
medium.place(x=10, y= 100)

hard = Button(window, text = 'Hard level', bg = '#baffc9', font = 'Times 11', command = hard)
hard.place(x=10, y= 140)


window.mainloop()