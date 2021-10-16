liste_1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
liste_pairs = []
def tab():
    for i in range (len(liste_1)):
        if i%2==0:
            liste_pairs.append(i*2)
    return liste_pairs
print(tab())
