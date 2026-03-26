import re

def validName(name):
    if re.fullmatch(r"[A-Za-z]", name):
        return True
    
def validClass(classs):
    if re.fullmatch(r"(warrior|mage)", classs):
        return True
    
def validRace(race):
    if re.fullmatch(r"(human|elf|troll|orc)", race):
        return True