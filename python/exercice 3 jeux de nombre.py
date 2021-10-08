from random import *

def jeux():
     n=randrange(101)
     print("trouver le nombre mystere")
     while True:
          nombre=int(input("veuiller chosir un nombre : "))
          if nombre == n:
               print("gagner")
               break
          else:
               if nombre >= n:
                    print("trop grand")
               else:
                    print("trop petit")



def fibo():
     a=0
     b=1
     n=int(input("n premier termes de la suite : "))
     for i in range(0,n+1):
          c=a+b
          a=b
          b=c
          print("( numero boucle",i,") : ",c)
fibo()
