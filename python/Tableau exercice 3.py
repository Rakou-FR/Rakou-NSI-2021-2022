liste_1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
liste_2 = []
def tab():
    for i in range (len(liste_1)):
        liste_2.append(i*2)
    return liste_2
print(tab())
