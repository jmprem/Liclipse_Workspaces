'''
Created on 26-Nov-2017

@author: Premkumar Jayakumar
'''
from numpy.ma.mrecords import _guessvartypes

game_state = ["Rock", "Spock", "Paper", "Lizard", "Scissors"]

def name_to_number(name):
    return game_state.index(name)

def number_to_name(number):
    return game_state[number]

def rspls(guess):
    player_number = name_to_number(guess)
    import random
    comp_number = random.randrange(0,5,1)
        
    diff = (player_number - comp_number)%5
    print(diff)
    
    if diff == 1 or diff == 2:
        print("Player Wins with choice: " + guess + "!")
    elif diff == 3 or diff == 4:
        print("Computer Wins with choice: " + number_to_name(comp_number) + "!")
    else:
        print("Unknown Difference. Retry.. Sorry")

if __name__ == '__main__':
    rspls("Rock")
    rspls("Spock")
    rspls("Paper")
    rspls("Lizard")
    rspls("Scissors")