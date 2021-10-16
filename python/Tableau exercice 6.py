liste22=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
liste_2=[]
def multi():
    for i in range(len(liste)):
        if i%2==0:
            liste_2.append(i*2)
        else:
            liste_2.append(i*3)
    return liste_2
                   

def exo6():
    phrase="Première ligne\nDeuxième ligne\nTroisième ligne\n"
    liste=[]
    lettre="\n"
    for i in range(len(phrase)):
        if phrase[i] == lettre:
            liste.append("")
        else:
            liste.append(phrase[i])
    for j in range(len(liste)):
        liste.isupper(j)
    liste_n="".join(liste)
    return liste_n

def exo5():
    phrase="Première ligne\nDeuxième ligne\nTroisième ligne\n"
    liste=[]
    lettre="\n"

    for i in range(len(phrase)):
        if phrase[i] == lettre:
            liste_n="".join(liste)
        else:
            liste_n=liste.append(phrase[i])
    for j in range(len(liste_n)):
        if liste_n.isupper():
            print("cheh")
    return liste_n

def exercice5():
    phrase="Première ligne\nDeuxième ligne\nTroisième ligne\n"
    liste=[phrase]
    for i in range(len(liste)):
        liste=phrase.split("\n")
    return liste
print(exercice5())
        
