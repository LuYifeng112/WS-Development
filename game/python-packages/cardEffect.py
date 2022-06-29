"""
a function that calls the effects of the cards
"""

from Classes import Boss
from random import randint
from Classes import Player

#declaring local boss object, delete
CurrentBoss = "Jorge"

def PlayCard(ID): #CardName might be changed to ID, beware of code
    CardName = CardDictionary[ID].GetName()
    
    #exception handling, need to be tested before removing
    try:
        if eval("Effect" + CardName + "()"):
            PlayerInstance.RemoveCardFromHand(ID)

    except SyntaxError:
        print("Your CardName variable is wonk")
    except:
        print("Something went wonk")

#Name of function might change form name of card to ID
def EffectAsuraBlessing():
    if EnoughEnergy(4):
        CurrentBoss.TakeSpiritDmg(1)
        CurrentBoss


def RandomCardFromDeck():
    return PlayerInstance.GetDeck()[random.randint(len(PlayerInstance.GetDeck()))]


def TypeDmg(Type):
    if Type == "S":
        pass
    if Type == "M":
        pass
    if Type == "P":
        pass

def EnoughEnergy(Value):
    if PlayerInstance.GetCurrentEnergy() >= Value:
        PlayerInstance.UseEnergy(Value)
        return True