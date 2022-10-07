from unicodedata import name
from characters import *
import random

#We do not talk about fight loop. We do describe it in the comments. This code takes the enemy dictionary 
#and prepares it to be "fought" against by the hero dictionary. 
def fight_loop(monster_list):
    while len(monster_list) > 0:
        current_monster = monster_list[0]
        print('A wild', current_monster['name'],'appears. Prepare to fight. You have', (your_hero["health"]),'health remaining')
        # select a random attack ffrom the hero
        # decrement the monster's health based on the randmoly selected hero attack
        random_attack = random.choice(your_hero['attacks'])
        current_monster['health'] -= random_attack[1]
        print(random_attack)
        if current_monster['health']<= 0:
            print('Your foe the', current_monster['name'], 'lies dead. Steel yourself for the next one.')
            monster_list.pop(0)
            continue
        elif current_monster['health']>0:
            random_attack = random.choice(current_monster['attacks'])
            your_hero['health'] -= random_attack[1]
            print(random_attack)
        if your_hero['health']<=0:
            print("You Died")
            break
        elif len(monster_list) == 0:
            print("Your foes lie defeated. You win or something.")

    #for i in monster_book_of_monsters:
        #for i,d in enumerate(monster_book_of_monsters):
            #print(i," : ",d)
        
    #if your_hero["health"] <= 0:
        #print('You Died')
#for health_tuple in enemy_0001['health']:

    

        # # HERO gets attack first
        # did_attack_num = random.randint(0, 10)
        # if (did_attack_num > 3):
        #     # hero attack hit!
        
        # did_attack_num = random.randint(0, 10)
        # if(did_attack_num >= 5):
        #     # villian

#Manages the Hero starting health and their Attack loop
#print(your_hero["health"])
#print(random.choice(your_hero["attacks"]))

#Manages the Hero starting health and their Attack loop
#print(your_hero["health"])
#print(random.choice(your_hero["attacks"]))


fight_loop(monster_book_of_monsters)


#Randomly select a monster
#print(random.choice(monster_book_of_monsters["name"]))

#Manages the break of game if the players health reaches zero or becomes negative. 


#def run_game():
#print('Good luck adventurer! You are without gold and alone, luck is all you have...')

    #run_game()
    #Welcome Message
    #Fight Enemy 1
    #Fight Enemy 2
    #Fight Enemy 3
    #Print Victory Message