def nb_client_sep():
      a=float(800)
      for i in range(1,13):
            a=(a*0.95)+45
            print(a)


def nb_client():
      a=800
      b=int(input("\nnombres de mois a prevoir ? :"))
      for i in range(1,b+1):
            a=(a*0.95)+45
            print(a)

nb_client_sep()
nb_client()












































