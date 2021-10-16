def listee():
    liste50=[]
    for i in range(0,50):
        liste50.append(i)
    for j in range(len(liste50)):
        if j!=0:
            if j%2 == 0:
                liste50.remove(j)
    return liste50

print(listee())
        
