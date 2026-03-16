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
class PlayerCharacter:

    def __init__ (self, name, health, mana, stamina, classs, race):
        self.name = name
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.classs = classs
        self.race = race
        self.balance = 0
        self.inventory = [self.Weapon]

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def attackTarget(self, target):
        if self.isAlive() == True:
            print("You attack the " + target + " for " + str(self.Weapon.damage) + " hitpoints!")
            self.Weapon.use()

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

    def viewInventory(self):
        if len(self.inventory) == 1:
            print("You have the following item in your inventory: " + self.inventory[0].name)

        elif len(self.inventory) > 1:
            print("You have the following items in your inventory: ")
            for item in self.inventory:
                print("- " + item.name)
        
        elif len(self.inventory) == 0:
            print("Your inventory is empty.")

    def pickupItem(self, Item):
        self.inventory.append(Item)
        print("You picked up the " + Item.name + " and added it to your inventory.")


# Class to represent an enemy NPC in the game
class EnemyNPC:

    def __init__(self, health, mana, stamina, classs, race, Weapon):
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.classs = classs
        self.race = race
        self.inventory = [Weapon]

    def attackTarget(self, target):
        if self.isAlive() == True:
            print("The " + self.classs + " attacks you for " + str(self.Weapon.damage) + " hitpoints!")
            self.Weapon.use()

            if self.Weapon.type == "melee":
                self.stamina = self.stamina - 10
            elif self.Weapon.type == "magic":
                self.mana = self.mana - 10

        else:
            print("The " + self.classs + " is dead and cannot attack you.")

    # Uses an if statement to check that the enemy's health is above 0 before allowing it to attack.
    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False

# Class to represent an item in the game - this is inherited by the player character  
class Item:

    def __init__ (self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.value = self.calculateValue()

    def calculateValue(self):
        if self.rarity == "common":
            return 10
        elif self.rarity == "uncommon":
            return 20
        elif self.rarity == "rare":
            return 50
        elif self.rarity == "epic":
            return 100
        elif self.rarity == "legendary":
            return 500

