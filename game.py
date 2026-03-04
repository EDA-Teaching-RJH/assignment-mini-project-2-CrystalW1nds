class Weapon:

    def __init__ (self, name, damage, durability, type):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.type = type

    def use(self, target):
        if self.durability > 0:
            self.durability = self.durability - 1
            target.health = target.health - self.damage

        return target



class PlayerCharacter:

    def __init__ (self, health, mana, stamina, classs, race, Weapon):
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.classs = classs
        self.race = race

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



class EnemyNPC:

    def __init__(self, health, mana, stamina, classs, race, Weapon):
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.classs = classs
        self.race = race

    def attackTarget(self, target):
        if self.isAlive() == True:
            print("The " + self.classs + " attacks you for " + str(self.Weapon.damage) + " hitpoints!")
            self.Weapon.use()

            if self.Weapon.type == "melee":
                self.stamina = self.stamina - 10
            elif self.Weapon.type == "magic":
                self.mana = self.mana - 10