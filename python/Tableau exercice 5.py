liste=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
liste_2=[]
def multi():
    for i in range(len(liste)):
        if i%2==0:
            liste_2.append(i*2)
        else:
            liste_2.append(i*3)
    return liste_2

print(multi())
                   
