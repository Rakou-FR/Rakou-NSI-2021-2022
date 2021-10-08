liste = [1,2,3,4,5]

def cheh():
    print(liste)
    print("afficher liste[4] = ",liste[4])
    print("afficher liste[1] = ",liste[1])
    liste[1]=20
    print("afficher liste[1] remplacer par 20 = ",liste[1])
    liste[3]=liste[2]+liste[4]
    print("afficher liste[3]",liste[3])
    for i in range (1,11):
        print("affiche : ", i, "fois ",liste[4])



def tab_colonne():
    liste = [1,4,3,4,5]
    for i in range(0,5):
        print(liste[i])

tab_colonne()
