def nbPremier():
     nb=int(input("choisir une nombre premier : "))
     boolean=True
     if nb == 1:
          print("nombre premier : ", bn)
     else:
          for i in range(2,nb):
               if nb%i == 0:
                    boolean=False
                    print("nombre",nb,"n'est pas premier : ", boolean)
                    break
               else:
                    print("nombre", nb,"est premier :", boolean)
                    break
