
import random 

def guess():
    print('''
            This is the guess game, you have to pick the min and the max number to be able to guess it
            for harder games you should make the max bigger than 50
    ''')
    guess_game = True 
    num = 0 
    min_x = int(input('pick the min number : '))
    min_y = int(input('pick the max number : '))
    attempt = int(input('Enter number of attemps: '))
    correct = random.randint(min_x, min_y)
    
    while num < attempt:
        guess = int(input('Guess a number ({},{}) :  '.format(min_x, min_y)))
        
        if guess > correct:
            num += 1
            print('Too high')

        elif guess < correct:
            num += 1
            print('Too low')

        else: 
            print('you guessed the number correct, congrats')
            break

    print(f'the correct number is {correct}, you guessed {guess}!')
        
guess()


