import csv
import random

class Character:
    def __init__(self, name, health, mana, stamina, classs, race, Weapon):
        self.name = name
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.classs = classs
        self.race = race
        self.Weapon = Weapon

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def takeDamage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0

# Class to represent a weapon in the game - this is inherited by both the player character and the enemy NPC classes
class Weapon:

    def __init__ (self, damage, durability, type, Item):
        self.name = Item.name
        self.damage = damage
        self.durability = durability
        self.type = type

    def use(self, target):
        if self.durability > 0:
            self.durability = self.durability - 1
            target.health = target.health - self.damage

        return target


# Class to represent the player character in the game
class PlayerCharacter(Character):

    def __init__ (self, name, health, mana, stamina, classs, race, Weapon):
        super().__init__(name, health, mana, stamina, classs, race, Weapon)
        
    def attackTarget(self, target):
        if self.isAlive():
            print(f"{self.name} attacks {target.name} for {self.weapon.damage} damage!")
            self.Weapon.use(target)

            if self.Weapon.type == "melee":
                self.stamina = self.stamina - 10
            elif self.Weapon.type == "magic":
                self.mana = self.mana - 10

        else:
            print("You are dead and cannot attack the " + target + ".")

    def heal(self, target):
        if self.isAlive() == True:
            print("You heal yourself for " + str(self.Weapon.damage) + " hitpoints!")

            self.health = self.health + self.Weapon.damage
            self.mana = self.mana - 10


# Class to represent an enemy NPC in the game
class EnemyNPC(Character):

    def __init__(self, health, mana, stamina, classs, race, Weapon):
        super().__init__(name, health, mana, stamina, classs, race, Weapon)

    def attackTarget(self, target):
        if self.isAlive():
            print(f"{self.name} attacks {target.name} for {self.weapon.damage} damage!")
            self.Weapon.use(target)

        else:
            print("The " + self.classs + " is dead and cannot attack you.")


def menu():
    print("Main Menu:")
    print("1) Create a new character")
    print("2) Load saved character")
    print("3) Exit game")

def characterCreation():
    name = input("Please enter your character's name:")
    classs = input("Please enter your character's class (e.g. warrior, mage):")
    race = input("Select your character's race (e.g human, elf, troll, orc):")

    if classs == "warrior":
        selection= random.randint(1, 4)

    elif classs == "mage":
        selection = random.randint(1,3)

    else:
        print("Invalid class selection. Please choose either 'warrior' or 'mage'.")
        return

    character = PlayerCharacter(name, 100, 100, 100, classs, race, Weapon)
    writeCharacterToCSV(character)

#this uses the csv library to write the player's character information to the character saves file
def writeCharacterToCSV(character):
    with open('characterSheet.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([character.name, character.health, character.mana, character.stamina, character.classs, character.race, character.weapon.name, character.weapon.damage, character.weapon.durability, character.weapon.type])

def mainMenuSeq():
    menu()
    choice = input("Please enter the number of your choice: ")

    if choice == "1":
        characterCreation()
    
    elif choice == "2":
        print("Load saved character functionality is not yet implemented.")

    elif choice == "3":
        print("Exiting game. Goodbye!")
        print("Saving game...")

        exit()

