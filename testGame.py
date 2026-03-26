import unittest
from game import Weapon, PlayerCharacter, EnemyNPC, loadCharacter, writeCharacterToCSV
from validators import validClass, validName, validRace

class TestGame(unittest.TestCase):
    def test_isAlive(self):
        weapon = Weapon("Sword", 10, 10, "melee")
        player = PlayerCharacter("TestPlayer", 100, 100, 100, "warrior", "human", weapon)
        self.assertTrue(player.isAlive())

    def test_takeDamage(self):
        weapon = Weapon("Sword", 10, 10, "melee")
        player = PlayerCharacter("TestPlayer", 100, 100, 100, "warrior", "human", weapon)
        player.takeDamage(50)
        self.assertEqual(player.health, 50)

    def test_use(self):
        weapon = Weapon("Sword", 10, 10, "melee")
        player = PlayerCharacter("TestPlayer", 100, 100, 100, "warrior", "human", weapon)
        target = EnemyNPC("TestTarget", 100, 100, 100, "warrior", "human", weapon)
        weapon.use(target)
        self.assertEqual(target.health, 90)

    def test_validName(self):
        self.assertTrue(validName("Henry"))
        self.assertFalse(validName("Henry223"))

    def test_validClass(self):
        self.assertTrue(validClass("warrior"))
        self.assertFalse(validClass("archer"))

    def test_validRace(self):
        self.assertTrue(validRace("elf"))
        self.assertFalse(validRace("dwarf"))

    def test_saveAndLoadCharacter(self):
        weapon = Weapon("Sword", 10, 10, "melee")
        player = PlayerCharacter("TestPlayer", 100, 100, 100, "warrior", "human", weapon)
        filename = "test_characterSheet.csv"

        writeCharacterToCSV(player, filename)
        loaded = loadCharacter(filename)

        self.assertEqual(loaded.name, "TestPlayer")
        self.assertEqual(loaded.weapon.name, "Sword")

if __name__ == '__main__':
    unittest.main()