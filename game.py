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

    def __init__ (self, name, damage, durability, type):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.type = type

    def use(self, target):
        if self.durability > 0:
            self.durability -= 1
            target.takeDamage(self.damage)
        else:
            print(f"The {self.name} is broken and cannot be used.")

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
    classs = input("Please enter your character's class (warrior/mage): ").lower()
    race = input("Select your character's race: ").lower()

    weapon = getWeaponForClass(classs)

    if weapon is None:
        print("Invalid class selection. Defaulting to warrior.")
        classs = "warrior"
        weapon = getWeaponForClass(classs)

    character = PlayerCharacter(name, 100, 100, 100, classs, race, weapon)
    writeCharacterToCSV(character)
    print(f"Character {name} created successfully and saved.")
    return character


def getWeaponForClass(classs):
    if classs == "warrior":
        return Weapon("Sword", 20, 100, "melee")
    elif classs == "mage":
        return Weapon("Staff", 20, 100, "magic")
    else:
        print("Invalid class selection. Defaulting to warrior.")
        return None


#this uses the csv library to write the player's character information to the character saves file
def writeCharacterToCSV(character, filename='characterSheet.csv'):
    with open(filename, mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            character.name,
            character.health,
            character.mana,
            character.stamina,
            character.classs,
            character.race, 
            character.weapon.name,
            character.weapon.damage,
            character.weapon.durability,
            character.weapon.type
            ])
        
def loadCharacter(filename='characterSheet.csv'):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        row = next(reader)

        weapon = Weapon(
            row[6],
            int(row[7]),
            int(row[8]),
            row[9]
        )
        
        character = PlayerCharacter(
            row[0],
            int(row[1]),
            int(row[2]),
            int(row[3]),
            row[4],
            row[5],
            weapon
        )

        return character

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

