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
#Enemy 1 dictionary. 
enemy_0001 = {
"name": 'Monster House',
    "level": 1, #integer
    "health": 100, #integer
    "equipment": {'Chain Mail', 'Helmet','Ornate Brass Doorknobs'}, #set of strings
    "attacks": (('Foul Horror Shutters',15),('Fire Misplaced',35),('Witch Slaying Leap',45)),
    "coins": { #Dictionary
        "copper": 10, #integer
        "silver": 10, #integer
        "gold": 0, #integer    
    }
}
#Enemy 2 dictionary
enemy_0002 = {
"name": 'Shimmer',
    "level": 1, #integer
    "health": 100, #integer
    "equipment": {'Cogitative Cloak', 'Three Dead Spiders',}, #set of strings
    "attacks": (('Daylight Sneak Attack',15),('Jump Scare',0)),
    "coins": { #Dictionary
        "copper": 0, #integer
        "silver": 20, #integer
        "gold": 0, #integer    
    }
}
#Enemy 3 dictionary
enemy_0003 = {
"name": 'Land Shark',
    "level": 1, #integer
    "health": 100, #integer
    "equipment": {'Large Tooth', 'Small Tooth','Golden Lock Tooth'}, #set of strings
    "attacks": (('Bite',15),('Devastating Insult',35)),
    "coins": { #Dictionary
        "copper": 0, #integer
        "silver": 10, #integer
        "gold": 10, #integer    
    }
}
#dictionary of dictionaries. Allows for quick address of monster dictionaries in sequence.
monster_book_of_monsters = [enemy_0003,enemy_0002,enemy_0001]

