#Imports all the necessary items for this code. The code should import everything with import *. Sometimes it 
#does not. To appease the dark spirits that run python, do not remove the 'import name' section. It should 
#not be needed, but when you remove it the program sometimes crashes. The crash occurs because the hero inventory
#is not brought in when the program brings in everything. The hero inventory is included in 'everything.'
from unicodedata import name
from characters import *
import random
#We do not talk about fight loop. We do describe it in the comments. This code takes the enemy dictionary 
#and prepares it to be "fought" against by the hero dictionary. All this talk of dictionaries fighting each other
#implies a better game/series than I have any reason to invent. 
def fight_loop(monster_list):
    while len(monster_list) > 0:
        current_monster = monster_list[0]
        print('You are facing a', current_monster['name'],'. Prepare to fight. You have', (your_hero["health"]),'health remaining')
        print('Your foe has', current_monster['health'],'health remaining.')
        # select a random attack ffrom the hero
        # decrement the monster's health based on the randmoly selected hero attack.
        # Hero is given the first strike. This made the programming easier and could say something about the 
        # open hostility of action heroes, but ease of code is the real answer.
        random_attack = random.choice(your_hero['attacks'])
        #This helps track the damage and attacks being used on the monster visually for the user story.
        print('You strike at the',current_monster['name'],'with a',random_attack[0],'dealing',random_attack[1],'damage.')
        current_monster['health'] -= random_attack[1]
        if current_monster['health']<= 0:
            print('Your foe the', current_monster['name'], 'lies dead. Steel yourself for the next one.')
            your_hero['coins']['copper']+=current_monster['coins']['copper']
            your_hero['coins']['silver']+=current_monster['coins']['silver']
            your_hero['coins']['gold']+=current_monster['coins']['gold']
            print('You now have the following funds from looting the monster:',your_hero['coins'])
            print(your_hero['coins'])
            #Do NOT Change the below code. It adds the monster's equipment to the hero's equipment, and took a solid day.
            #Syntax is very important in python. It does not print excellently, but it works! 
            monster_inv = current_monster['equipment']
            your_hero["equipment"].update(monster_inv)
            print('Your loot the monster, and now have:', your_hero['equipment'])
            #levels up the hero if they defeat the monster. This is part of the bonus task of levelling up the hero. 
            your_hero['level']+=1
            print('Level up! You are now level',your_hero['level'])
            monster_list.pop(0)
            continue
        #continues the fight if monster health is above zero. 
        elif current_monster['health']>0:
            random_attack = random.choice(current_monster['attacks'])
            print('The monstrous',current_monster['name'],'strikes at you with a',random_attack[0],'dealing',random_attack[1],'damage.')
            your_hero['health'] -= random_attack[1]
        #ends the program early if the hero dies
        if your_hero['health']<=0:
            print("You Died")
            return
        elif len(monster_list) == 0:
            print("Your foes lie defeated. You win or something.")
def greeting_message():
    print('Good luck adventurer! You are without gold and alone, luck is all you have...')
def victory_message():
    if your_hero['health']<=0:
        print('Your journey ends here. Your bones are swept clean by the desert sands. Press continue to continue')
    else:print("Your foes lie defeated. You win or something.")
#The small cycle of functions contained in run_game...run the game. Please see below comments on specifics. 
def run_game():
#Starts the game with a message to the user
    greeting_message()
#begins the fighting/looting loop
    fight_loop(monster_book_of_monsters)
#displays a victory message if the hero successfully kills all monsters while above 0 health
    victory_message()
#Calls the above function of functions to run the actual game. See this as a 'press Start' for the program.
run_game()