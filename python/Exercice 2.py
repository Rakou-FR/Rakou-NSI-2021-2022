def algo():
    a=int(input("choisir un nombre à tester : "))
    b=int(input("choisir le multiple : "))
    pairOUimpair = a % b
    if pairOUimpair == 0:
        print("le nombre ",a,"est un multiple de ",b)
    else:
        print("le nombre ",a,"n'est pas un multiple de ",b)

algo()

def pOimp():
    a=int(input("choisir un nombre à tester : "))
    if a % 2 == 0:
        print("le nombre ",a," est pair")

    else:
        print("le nombre ",a," est impair")
pOimp()
