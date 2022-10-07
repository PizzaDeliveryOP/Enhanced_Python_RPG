#(5 points): As a data analyst, I want to make at least five commits on GitHub with descriptive messages.  
#(2.5 points): As a user, I want an engaging story to be told using print() statements.  
    #(2.5 points): As a data analyst, I want to create a hero variable and set it equal to a Dictionary  
    #(2.5 points): As a data analyst, I want to create THREE enemy variables and set each equal to a Dictionary 
#(5 points): As a user, I want my Hero and Enemy’s attack to be chosen at random. 
#(5 points): As a user, I want my Hero or Enemy’s health to decrease based on the power of the successful attack. 
#(2.5 points): As a user, I want the results of each attack to be printed to the terminal.
#(5 points): As a user, I want the Hero and Enemy to continue attacking each other until one's health reaches zero.  
#(5 points): As a user, I want to be able to “loot” defeated enemies by adding the Enemy’s equipment set to the Hero’s equipment Set
#(5 points): As a data analyst, I want the game to conclude when the Hero’s health reaches 0, or when all three Enemies have been defeated.   
#(2.5 points): As a data analyst, I want to create a run_game() function, which calls my other functions in a logical order to determine the game’s flow. 
#(5 points): As a data analyst, I want all of my functions to have a Single Responsibility. 

#Bonus Stories
    #(5 points): As a user, I want to “loot” defeated enemies by adding the Enemy’s gold, silver, and copper coins to the appropriate value in the Hero’s coin Dictionary.
    #(7.5 points): As a user, I want to increase my Hero’s level after defeating an Enemy, which will include: 
        #Incrementing my Hero’s level by 1 
        #Adding a new attack of my choosing to my Hero's Attack Tuple. 

your_hero = {
    "name": 'Depraved', #String
    "level": 1, #integer
    "health": 100, #integer
    "equipment": {'Robe', 'Helmet'}, #set of strings
    "attacks": (('Miss',0),('Punch',15),('Critical Sword Strike',100)),
    "coins": { #Dictionary
        "copper": 0, #integer
        "silver": 0, #integer
        "gold": 0, #integer
    }
}

enemy_0001 = {
"name": 'Monster House',
    "level": 1, #integer
    "health": 100, #integer
    "equipment": {'Chain Mail', 'Helmet','Ornate Brass Doorknobs'}, #set of strings
    "attacks": (('Foul Horror Shutters',15),('Fire Misplace',35),('Witch Slaying Leap',45)),
    "coins": { #Dictionary
        "copper": 0, #integer
        "silver": 10, #integer
        "gold": 0, #integer    
    }
}

enemy_0002 = {
"name": 'Shimmer',
    "level": 1, #integer
    "health": 100, #integer
    "equipment": {'Cogitative Cloak', 'Three Dead Spiders',}, #set of strings
    "attacks": (('Daylight Sneak Attack',15),('Jump Scare',0)),
    "coins": { #Dictionary
        "copper": 0, #integer
        "silver": 10, #integer
        "gold": 0, #integer    
    }
}

enemy_0003 = {
"name": 'Land Shark',
    "level": 1, #integer
    "health": 100, #integer
    "equipment": {'Large Tooth', 'Small Tooth','Golden Lock Tooth'}, #set of strings
    "attacks": (('Bite',15),('Insult Family',35)),
    "coins": { #Dictionary
        "copper": 0, #integer
        "silver": 10, #integer
        "gold": 0, #integer    
    }
}

monster_book_of_monsters = [enemy_0003,enemy_0002,enemy_0001]

