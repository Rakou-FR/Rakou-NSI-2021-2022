def somme(n):
    n=str(n)
    resultat=0
    for cara in n:
        resultat+=int(cara)
        print(resultat)
    print("resultat = ",resultat)

def bin2dec(n):
    n = n[2:]
    resultat=0
    for bin in n:
        resultat*=2
        resultat+=int(bin)
        print(resultat)
    print("le resultat = ", resultat)

def dec2bin(n):
    chaine=""
    while n != 0:
        avant = n % 2
        if avant == 0:
            chaine += "0"
        else:
            chaine += "1"
        n = n//2
    chaine = chaine[::-1]
    chaine = "0b" + chaine
    print(chaine)

dec2bin(13)


