import random

def insulteMoiCa():
    liste = []
    with open("insultes.new.txt", "r", encoding="utf-8") as temp:
        fichier = temp.readline().split(", ")
    for ligne in fichier:
        liste.append(ligne)
    liste.remove("")
    i = random.randint(0,len(liste))
    choix = liste[i]
    print("numero de l'insulte : ", i)
    return choix[1:len(choix)-1]
print(insulteMoiCa())
