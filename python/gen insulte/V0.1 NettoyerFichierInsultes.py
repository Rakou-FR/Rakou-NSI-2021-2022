def Propre(): #correspond a un fichier.txt tel que A, B, C, D
    with open("insultes0.txt", "r") as cheh:
        txt = cheh.read().split(', ')
    with open("insultes.new.txt", "w") as cheh1:
        for item in txt:
            cheh1.write('"'+item+'"'+",")
    return txt
    
def Propre1(): #fichier.txt comme dans le PDF des consignes
    with open("insultes1.txt", "r") as temp:
        txtn = temp.read().split("\n")
        for i in txtn:
            if "" in txtn :
                txtn.remove("")
        with open("insultes.new.txt", "w") as temp1:
            for item in txtn:
                temp1.write('"'+item+'"'+", ")
        return txtn
print(Propre1())
