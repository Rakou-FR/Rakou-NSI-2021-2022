import random

def insulteMoiCa():
    with open("insultes.new.txt", "r", encoding="utf-8") as temp:
        txt = temp.read().split(", ")
        choix = random.choice(txt)
        return choix[2:len(choix)-1]
print(insulteMoiCa())
