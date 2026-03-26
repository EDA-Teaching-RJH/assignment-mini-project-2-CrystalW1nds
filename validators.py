import re

def validName(name):
    if re.fullmatch(r"[A-Za-z]{2,12}", name):
        return True
    else:
        return False
    
def validClass(classs):
    if re.fullmatch(r"(warrior|mage)", classs):
        return True
    else:        
        return False
    
def validRace(race):
    if re.fullmatch(r"(human|elf|troll|orc)", race):
        return True
    else:
        return False