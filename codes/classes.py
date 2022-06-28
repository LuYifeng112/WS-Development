"""
A file full of all the classes of the game,
imports from file
"""

from random import randint

class CombatAi():
    def __init__(self, AiTuple):
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
        AiTuple is a Tuple linked to the ID of the enemy in a Dictionary
        '''
        self.__Aggression = AiTuple[0]
        self.__Defense = AiTuple[1]
        self.__Parry = AiTuple[2]
        self.__Coercion = AiTuple[3]
        self.__Crit = AiTuple[4]
    
    def GetAggression(self):
        return self.__Aggression
    
    def GetDefense(self):
        return self.__Defense
    
    def GetParry(self):
        return self.__Parry
    
    def GetCoercion(self):
        return self.__Coercion
    
    def GetCrit(self):
        return self.__Crit

class Entity():
    #Creates base class for all entities, including bosses and players
    def __init__(self, Name, StatsTuple):
        #StatsTuple in format spirit, vitality, energy
        self.__Name = Name
        self.__Spirit = int(StatsTuple[0])
        self.__Vitality = int(StatsTuple[1])
        self.__Energy = int(StatsTuple[2])
        self.__CurrentSpirit = 0
        self.__CurrentVitality = self.__Vitality
        self.__CurrentEnergy = self.__Energy

    def GetName(self):
        return self.__Name

    #return max stats
    def GetSpirit(self):
        return self.__Spirit

    def GetVitality(self):
        return self.__Vitality
    
    def GetEnergy(self):
        return self.__Energy

    #return Current stats
    def GetCurrentSpirit(self):
        return self.__CurrentSpirit
    
    def GetCurrentVitality(self):
        return self.__CurrentVitality

    def GetCurrentEnergy(self):
        return self.__CurrentEnergy

    #Update current stats, never below 0
    def UpdateSpirit(self, num):
        self.__CurrentSpirit = max(self.__CurrentSpirit + num, 0)

    def UpdateVitality(self, num):
        self.__CurrentVitality = max(self.__CurrentVitality + num, 0)

    def UpdateEnergy(self, num):
        self.__CurrentEnergy = max(self.__CurrentEnergy + num, 0)
        
class Card():
    def __init__(self, Name, Type, Cost, VitalityDmg, SpiritDmg, Image, Description, Effect = None):
        self.__Cost = int(Cost)
        self.__VitalityDmg = int(VitalityDmg)
        self.__SpiritDmg = int(SpiritDmg)
        self.__Effect = str(Effect)
        self.__Description = str(Description)
        self.__Image = Image
        self.__Name = str(Name)
        self.__Type = str(Type)

    def GetCost(self):
        return self.__Cost
    
    def GetCostStr(self):
        return str(self.__Cost)

    def GetVitalityDmg(self):
        return self.__VitalityDmg
    
    def GetVitalityDmgStr(self):
        return str(self.__VitalityDmg)
    
    def GetSpiritDmg(self):
        return self.__SpiritDmg
    
    def GetSpiritDmgStr(self):
        return str(self.__SpiritDmg)

    def GetEffect(self):
        return self.__Effect

    def GetDescription(self):
        return self.__Description

    def GetImage(self):
        return self.__Image

    def GetName(self):
        return self.__Name
        
    def GetType(self):
        return self.__Type
    
    def __repr__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, \n\n".format(self.__Name, self.__Type, self.__Cost, self.__VitalityDmg, self.__SpiritDmg, self.__Image, self.__Description, self.__Effect)
    
    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, \n\n".format(self.__Name, self.__Type, self.__Cost, self.__VitalityDmg, self.__SpiritDmg, self.__Image, self.__Description, self.__Effect)

class Boss(Entity):
    def __init__(self, Name, StatsTuple, Ai):
        super().__init__(Name, StatsTuple)
        self.__Ai = Ai #object

    def GetAi(self):
        return self.__Ai
    
    # def TakeVitalityDmg(self, Value):
    #     self.__CurrentVitality -= Value * PlayerInstance.GetDmgMultiplier()
    #     if self.__CurrentVitality <= 0:
    #         self.__IsAlive = False

    # def TakeSpiritDmg(self, Value):
    #     self.__CurrentSpirit += Value
    #     if self.__CurrentSpirit >= self.__MaxSpirit:
    #         self.__IsAlive = False
    
    # def RestoreSpirit(self):
    #     ToRestore = self.__MaxSpirit * (1 / 4)
    #     if self.__CurrentSpirit - ToRestore <= 0:
    #         self.ResetSpirit()
    #     else:
    #         self.__CurrentSpirit = self.__CurrentSpirit - ToRestore
    
    # def CalculateProbability(self):
    #     SpiritDifference = (self.__MaxSpirit - self.__CurrentSpirit) / self.__MaxSpirit
    #     Probability = 0.25 * (1 - SpiritDifference)
    #     return Probability
    
    # def BossDie(self):
    #     self.__IsAlive = False
    
    # def SetCanAttack(self, boolean):
    #     self.__CanAttack = boolean

    
class Player(Entity):
    def __init__(self, Name, Deck, StatsTuple):
        super().__init__(Name, StatsTuple)
        self.__Deck = Deck #list of card object
        self.__Hand = [] #hand of card object
        self.__Sin = 0

    def GetDeck(self):
        return self.__Deck

    def GetSin(self):
        return self.__Sin
    
    def UpdateSin(self, num):
        #Minimum of 0 sin
        self.__Sin = max(0, self.__Sin + num)

        # self.__EnergyRegenPerRound = 2
        # self.__MaxEnergy = int(Energy)
        # self.__Defence = 0 #a flat number of dmg is ignored, e.g. self.__Defence = 3, then you would take 3 less dmg from attacks
        # self.__DmgMultiplier = 1
        # self.__PercentageStrDefence = 0
     #a percentage of dmg is ignored e.g. 0.15 (value must be under 1)
        # self.__Inventory = []
        # self.__IsAlive = True
        # self.__Money = 0
    
    # def GetPercentageDefence(self):
    #     return self.__PercentageDefence
    # def GetPercentageDefenceStr(self):        
    #     return str(self.__PercentageDefence)
    
    # def GetDmgMultiplier(self):
    #     return self.__DmgMultiplier    
    # def GetDmgMultiplierStr(self):
    #     return str(self.__DmgMultiplier)
    
    # def GetEnergyRegenPerRound(self):
    #     return self.__EnergyRegenPerRound
    # def GetEnergyRegenPerRoundStr(self):
    #     return str(self.__EnergyRegenPerRound)

    

    
    # def GetInventory(self):
    #     return self.__Inventory
    
    # def GetMoney(self):
    #     return self.__Money
    # def GetMoneyStr(self):
    #     return str(self.__Money)
    
    # def GetDefence(self):
    #     return self.__Defence
    # def GetDefenceStr(self):
    #     return str(self.__Defence)
    
    # def SetDefence(self, Value):
    #     self.__Defence = Value
    
    # def ResetDefence(self):
    #     self.__Defence = 0

    # def SetEnergyRegenPerRound(self, Value):
    #     self.__EnergyRegenPerRound = Value
    
    # def SetDmgMultiplier(self, Value):
    #     self.__DmgMultiplier = Value
    
    # def ResetDmgMultiplier(self):
    #     self.__DmgMultiplier = 1
    
    # def SetPercentageDefence(self, Value):
    #     self.__PercentageDefence = Value
    
    # def ResetPercentageDefence(self):
    #     self.__PercentageDefence = 0
    
    # def RegenEnergy(self):
    #     if self.__CurrentEnergy + self.__EnergyRegenPerRound <= self.__MaxEnergy:
    #         self.__CurrentEnergy += self.__EnergyRegenPerRound
    #     elif self.__CurrentEnergy + self.__EnergyRegenPerRound == self.__MaxEnergy + 1:
    #         self.__CurrentEnergy += 1
    
    # def AddToInventory(self, Item):
    #     self.__Inventory.append(Item)
    
    # def RemoveFromInventory(self, Item):
    #     self.__Inventory.pop(self.__Inventory.index(Item))
    
    # def RemoveCardFromHand(self, ID):
    #     self.__Hand.pop(self.__Hand.index(ID))
    
    # def AddMoney(self, Value):
    #     self.__Money += Value
    
    # def RemoveMoney(self, Value):
    #     self.__Money -= Value
    

    
    # def SetEnergyMax(self, Value):
    #     self.__MaxEnergy = Value
    #     self.__CurrentEnergy = Value
    
    # def AddMaxVitality(self, Value):
    #     self.__MaxVitality += Value
    #     self.__CurrentVitality += Value

    # def TakeVitalityDmg(self, Value):
    #     if Value >= self.__Defence:
    #         VitalityDmg = Value - self.__Defence

    #     VitalityDmg -= (VitalityDmg * self.__PercentageDefence)
    #     self.__CurrentVitality -= VitalityDmg

    #     if self.__CurrentVitality <= 0:
    #         self.__IsAlive = False
    
    # def TakeSpiritDmg(self, Value):
    #     self.__CurrentSpirit += Value
    #     if self.__CurrentSpirit >= self.__MaxSpirit:
    #         self.__IsAlive = False
    
    # def RestoreSpirit(self):
    #     ToRestore = self.__MaxSpirit * (1/4)
    #     if self.__CurrentSpirit - ToRestore <= 0:
    #         self.ResetSpirit()
    #     else:
    #         self.__CurrentSpirit -= ToRestore
    
    # def RestoreVitality(self, Value):
    #     if self.__CurrentVitality + Value >= self.__MaxVitality:
    #         self.ResetVitality()
    #     else:
    #         self.__CurrentVitality += Value

    # def ResetSpirit(self):
    #     self.__CurrentSpirit = 0
    
    # def ResetPlayerAlive(self):
    #     self.__IsAlive = True
    
    # def ResetEnergy(self):
    #     self.__CurrentEnergy = self.__MaxEnergy
    
    # def ResetEnergyRegenPerRound(self):
    #     self.__EnergyRegenPerRound = 2
        
    # def ResetVitality(self):
    #     self.__CurrentVitality = self.__MaxVitality
    
    # def ResetSin(self):
    #     self.__Sin = 0
    
    # def UseEnergy(self, Value):
    #     self.__CurrentEnergy -= Value
    
    # def GainEnergy(self, Value):
    #     if self.__CurrentEnergy + Value >= self.__MaxEnergy:
    #         self.ResetEnergy()
    #     else:
    #         self.__CurrentEnergy += Value
    
    # def AlterCurrentSpirit(self, Value):
    #     self.__CurrentSpirit += Value
    
    # def AlterCurrentVitality(self, Value):
    #     self.__CurrentVitality += Value
    
    # def AddToHand(self, ID):
    #     self.__Hand.append(ID)


class Item():
    def __init__(self, Name, Desc, Value, Icon = None):
        self.__Name = Name
        self.__Desc = Desc
        self.__Value = Value
        self.__Icon = Icon
    
    def GetName(self):
        return self.__Name
    
    def GetDesc(self):
        return self.__Desc
    
    def GetValue(self):
        return self.__Value
    
    def GetIcon(self):
        return self.__Icon


class Shop():
    def __init__(self):
        self.__Shop = []
        self.__Lines = ["You're poor", "GeorgiePi: Imagine being poor", "Sell your kidney :D", "Yar har you need a job", "Touch some grass"]
    
    def GetShop(self):
        return self.__Shop
    
    def PlayerBuyItem(self, Item):
        if PlayerInstance.GetMoney() >= Item.GetValue():
            self.RemoveItem(Item)
            PlayerInstance.AddToInventory(Item)
            PlayerInstance.RemoveMoney(Item.GetValue())
        else:
            ReturnLine()
    
    def RemoveItem(self, Item):
        self.__Shop.pop(self.__Shop.index(Item))
    
    def ReturnLine(self):
        return self.__Lines[randint(len(self.__Lines) + 1)]