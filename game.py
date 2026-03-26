import csv
from validators import validClass, validName, validRace


class Character:
    def __init__(self, name, health, mana, stamina, classs, race, weapon):
        self.name = name
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.classs = classs
        self.race = race
        self.weapon = weapon

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

    def __init__ (self, name, damage, durability, wType):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.wType = wType

    def use(self, target):
        if self.durability > 0:
            self.durability -= 1
            target.takeDamage(self.damage)
        else:
            print(f"The {self.name} is broken and cannot be used.")

        return target


# Class to represent the player character in the game
class PlayerCharacter(Character):

    def __init__ (self, name, health, mana, stamina, classs, race, weapon):
        super().__init__(name, health, mana, stamina, classs, race, weapon)
        
    def attackTarget(self, target):
        if self.isAlive():
            print(f"{self.name} attacks {target.name} for {self.weapon.damage} damage!")
            self.weapon.use(target)

            if self.weapon.wType == "melee":
                self.stamina = self.stamina - 10
            elif self.weapon.wType == "magic":
                self.mana = self.mana - 10

        else:
            print(f"You are dead and cannot attack the {target.name}.")

    def heal(self):
        if self.isAlive() == True:
            print("You heal yourself for " + str(self.weapon.damage) + " hitpoints!")

            self.health = self.health + self.weapon.damage
            self.mana = self.mana - 10


# Class to represent an enemy NPC in the game
class EnemyNPC(Character):

    def __init__(self, name, health, mana, stamina, classs, race, weapon):
        super().__init__(name, health, mana, stamina, classs, race, weapon)

    def attackTarget(self, target):
        if self.isAlive():
            print(f"{self.name} attacks {target.name} for {self.weapon.damage} damage!")
            self.weapon.use(target)

        else:
            print("The " + self.classs + " is dead and cannot attack you.")


def menu():
    print("Main Menu:")
    print("1) Create a new character")
    print("2) Load saved character")
    print("3) Demo combat")
    print("4) Exit game")

def characterCreation():
    name = input("Please enter your character's name:")
    while not validName(name):
        print("Invalid name. Must be 2-12 letters only.")
        name = input("Please enter your character's name:")
    
    classs = input("Please enter your character's class (warrior/mage): ").lower()
    while not validClass(classs):
        print("Invalid class. Must be 'warrior' or 'mage'.")
        classs = input("Please enter your character's class (warrior/mage): ").lower()
    
    race = input("Select your character's race: (human/elf/troll/orc)").lower()
    while not validRace(race):
        print("Invalid race. Must be 'human', 'elf', 'troll', or 'orc'.")
        race = input("Select your character's race: (human/elf/troll/orc)").lower()

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
            character.weapon.wType
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
    character = None
    print("Welcome to the RPG Game!")

    while True:
    
        menu()
        choice = input("Please enter the number of your choice: ")

        if choice == "1":
            character = characterCreation()
            if character:
                print(f"Welcome, {character.name}.")
        elif choice == "2":
            try:
                character = loadCharacter()
                print(f"Welcome back, {character.name}.")
            except FileNotFoundError:
                print("No saved character found. Please create a new character.")
        elif choice == "3":
            if character is None:
                print("No character loaded. Please create or load a character first.")
            else:
                battleDemo(character)
        elif choice == "4":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def battleDemo(player):
    print("Starting battle demo...")
    enemyWeapon = Weapon("Sword", 10, 20, "melee")
    enemy = EnemyNPC("Goblin", 50, 0, 50, "warrior", "orc", enemyWeapon)

    print(f"A wild {enemy.name} appears!")

    while player.isAlive() and enemy.isAlive():
        print(f"\n{player.name} - Health: {player.health}, Mana: {player.mana}, Stamina: {player.stamina}")
        print(f"{enemy.name} - Health: {enemy.health}")

        action = input("Do you attack/heal/quit?").lower()

        if action == "attack":
            player.attackTarget(enemy)
            if enemy.isAlive():
                enemy.attackTarget(player)
        elif action == "heal":
            player.heal()
            if enemy.isAlive():
                enemy.attackTarget(player)
        elif action == "quit":
            print("Exiting battle demo.")
            break
        else:
            print("Invalid action. Please enter 'attack', 'heal', or 'quit'.")

    if not enemy.isAlive():
        print(f"You have defeated the {enemy.name}!")
    elif not player.isAlive():
        print("You have been defeated. Game over.")

mainMenuSeq()