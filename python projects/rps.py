#first rock paper scissor game 
import random 

print (''' 
       ----------------------------------------------------
       | welcome to my first Rock, Paper, Scissor game !  |
       ----------------------------------------------------
       | = Rules are                                      |
       | = Rock > Scissor                                 |
       | = Scissor > Paper                                |
       | = Paper > Rock                                   |  
       ----------------------------------------------------
       
       ''')

game = True 
player_score = 0 
computer_score = 0
    
while game :
    print ('    Please enter a number to choose (Rock(1), Paper(2), Scissor(3) )')
    player_choice  = int(input('    Enter weapon of Choice: '))
    if player_choice == 1:
        weapon_name = 'Rock'    # we need to define a variable and save it instead of printing 
    elif player_choice == 2:
        weapon_name = 'Paper'
    elif player_choice == 3:
        weapon_name = 'Scissor'
    else:
        print('     only choose numbers between 1 and 3')
        break
    
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        comp_weapon_name = 'Rock'
    elif computer_choice == 2:
        comp_weapon_name = 'Paper'
    else:
        comp_weapon_name = 'Scissor'
        
    if player_choice == computer_choice :
        final_result = 'Draw'

    elif (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 3) or (player_choice == 3 and computer_choice == 1):
        computer_score += 1
        final_result = 'Computer wins'
        
    elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
        player_score += 1
        final_result = 'Player wins'       
    else:
        final_result = '    error has occured'
    
    print(f'''
       |  Results :: {final_result}
       --------------------------------------
       | Player Selected : {weapon_name}      
       | Computer Selected: {comp_weapon_name}
       | Player Score : {player_score}        
       | Computer Score : {computer_score}    
       --------------------------------------
       ''')
    
    print('     Thank you for playing, type (N) if you want to quit the game')
    repeat = input("    Do you want to play again? : ").lower()
    if repeat == 'n':
        quit()
    else:
        pass


    

"""
::note::
mistake here is that i made a whole code : 
(player_choice == 1 and computer_choice == 1) or (player_choice == 2 and comp_weapon_name == 2) or  (player_choice == 3 and comp_weapon_name == 3) :
instead of 
player_choice == computer_choice 

"""
























