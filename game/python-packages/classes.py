"""
A file full of all the classes of the game,
imports from file
"""
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

from random import randint

#     ___       ____       __  __       ___         _       ____          _        __  
#   ,"___".    F __ ]     F  \/  ]     F _ ",      /.\     /_  _\        /.\       FJ  
#   FJ---L]   J |--| L   J |\__/| L   J `-'(|     //_\\    [J  L]       //_\\     J  L 
#  J |   LJ   | |  | |   | |`--'| |   | ,--.\    / ___ \    |  |       / ___ \    |  | 
#  | \___--.  F L__J J   F L    J J   F L__J \  / L___J \   F  J      / L___J \   F  J 
#  J\_____/F J\______/F J__L    J__L J_______J J__L   J__L J____L    J__L   J__L J____L
#   J_____F   J______F  |__L    J__| |_______F |__L   J__| |____|    |__L   J__| |____|

                  
class combatAi():
    def __init__(self, aiTuple):
        '''
        Tendency to Attack
        Ability to restore fighting spirit
        Ease of lowering Fighting Spirit
        Strikes out of turn
        Deflects without any damage to fighting spirit
        A deck will be an object from the deck() class belonging to the opponent. This may be 
        removed in favour of      
        scripted attack.
        Ability to accept a non-lethal outcome
        These drops will be an object from the Item() class. 
     aiTuple is a Tuple linked to the ID of the enemy in a Dictionary
        '''
        self.__aggression = aiTuple[0]
        self.__defense = aiTuple[1]
        self.__parry = aiTuple[2]
        self.__crit = aiTuple[3]
        self.__coercion = aiTuple[4]
    
    @property
    def aggression(self): # All stats are suppose to add up to 1, except for coercion
        return self.__aggression
    
    @property
    def defense(self):
        return self.__defense
    
    @property
    def parry(self):
        return self.__parry
    
    @property
    def crit(self):
        return self.__crit
    
    @property()
    def coercion(self): # A separate stats from the others
        return self.__coercion
    
    

class Entity():
    #Creates base class for all entities, including bosses and players
    def __init__(self, name, statsTuple):
        #statsTuple in format spirit, vitality, energy
        self.__name = name
        self.__maxSpirit = int(statsTuple[0])
        self.__maxVitality = int(statsTuple[1])
        self.__maxEnergy = int(statsTuple[2])
        self.__currentSpirit = 0
        self.__currentVitality = self.__maxVitality
        self.__currentEnergy = self.__maxEnergy

    @property
    def name(self):
        return self.__name

    #return max stats

    @property
    def maxSpirit(self):
        return self.__maxSpirit

    @property
    def maxVitality(self):
        return self.__maxVitality
    
    @property
    def maxEnergy(self):
        return self.__maxEnergy

    #return Current stats

    @property
    def spirit(self):
        return self.__currentSpirit
    
    @property
    def vitality(self):
        return self.__currentVitality

    @property
    def energy(self):
        return self.__currentEnergy

    #Update current stats, never below 0
    def updateSpirit(self, num):
        self.__currentSpirit = min(self.__maxSpirit, max(self.__currentSpirit + num, 0)) #spirit goes up, but does not exceed max nor below 0

    def updateVitality(self, num):
        self.__currentVitality = min(self.__maxVitality, max(self.__currentVitality + num, 0)) #vitality changes, but does not exceed max nor below 0

    def updateEnergy(self, num):
        self.__currentEnergy = min(self.__maxEnergy, max(self.__currentEnergy + num, 0)) #energy changes, but does no exceed max nor 0
        
        
class Card():
    def __init__(self, name, dmgType, cost, vitalityDmg, spiritDmg, image, description, effect = None):
        self.__cost = int(cost)
        self.__vitalityDmg = int(vitalityDmg)
        self.__spiritDmg = int(spiritDmg)
        self.__effect = str(effect)
        self.__description = str(description)
        self.__image = image
        self.__name = str(name)
        self.__dmgType = str(dmgType)

    @property
    def cost(self):
        return self.__cost
    
    @property
    def costStr(self):
        return str(self.__cost)

    @property
    def vitalityDmg(self):
        return self.__vitalityDmg
    
    @property
    def vitalityDmgStr(self):
        return str(self.__vitalityDmg)
    
    @property
    def spiritDmg(self):
        return self.__spiritDmg
    
    @property
    def spiritDmgStr(self):
        return str(self.__spiritDmg)

    @property
    def effect(self):
        return self.__effect

    @property
    def description(self):
        return self.__description

    @property
    def image(self):
        return self.__image

    @property
    def name(self):
        return self.__name
    
    @property    
    def dmgType(self):
        return self.__dmgType
    
    def __repr__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, \n\n".format(self.__name, self.__dmgType, self.__cost, self.__vitalityDmg, self.__spiritDmg, self.__image, self.__description, self.__effect)
    
    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, \n\n".format(self.__name, self.__dmgType, self.__cost, self.__vitalityDmg, self.__spiritDmg, self.__image, self.__description, self.__effect)


class Boss(Entity):
    def __init__(self, name, statsTuple, ai):
        super().__init__(name, statsTuple)
        self.__ai = ai #object

    @property
    def ai(self):
        return self.__ai

class Player(Entity):
    def __init__(self, name, statsTuple):
        super().__init__(name, statsTuple)
        self.__money = 0
        self.__inventory = []
        self.__deck = []
        self.__sin = 0
    
        logging.info("Player Class Created")
    
    @property
    def money(self):
        return self.__money
    
    @property
    def deck(self):
        return self.__deck
    
    @property
    def sin(self):
        return self.__sin
    
    def updateMoney(self, num):
        self.__money = max(self.__money + num, 0) #update money, but not below 0
    
    def updateInventory(self, item, flag):
        if flag:
            self.__inventory.append(item) #adds item when flag = true, else removes it
        else:
            self.__inventory.pop(self.__inventory.index(item))
    
    def updateSin(self, num):
        self.__sin = max(self.__sin + num, 0)


class Item():
    def __init__(self, name, desc, value, icon = None):
        self.__name = name
        self.__desc = desc
        self.__value = value
        self.__icon = icon
    
    @property
    def name(self):
        return self.__name
    
    @property
    def desc(self):
        return self.__desc
    
    @property
    def value(self):
        return self.__value
    
    @property
    def icon(self):
        return self.__icon


# class Shop():
#     def __init__(self):
#         self.__shop = []
#         self.__lines = ["You're poor", "GeorgiePi: Imagine being poor", "Sell your kidney :D", "Yar har you need a job", "Touch some grass"]
    
#     @property
#     def shop(self):
#         return self.__shop
    
#     def playerBuyItem(self, item):
#         if playerInstance.money >= item.value:
#             self.removeItem(item)
#             playerInstance.updateInventory(item, True)
#             playerInstance.removeMoney(item.value)
#         else:
#             self.returnLine()
    
#     def removeItem(self, item):
#         self.__shop.pop(self.__Shop.index(item))
    
#     def returnLine(self):
#         return self.__lines[randint(len(self.__lines) + 1)]

def weightedChoice(choices): # To replace the use of weights in renpy blocks
        """ 
        @param choices: A list of (choice, weight) tuples. Returns a random
        choice (using renpy.random as the random number generator)
        """
        totalweight = 0.0
        for choice, weight in choices:
            totalweight += weight
        randval = renpy.random.random() * totalweight
        for choice, weight in choices:
            if randval <= weight:
                return choice
            else:
                randval -= weight