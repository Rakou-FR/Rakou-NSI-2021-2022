import numpy as np

def print_tableau(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if j == 7:
                print(tab[i][j])
            else:
                print(str(tab[i][j]) + " ", end="")
                
tableau = np.array([
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]])

print("Bataille navale. A vous de jouer \n regles : \n  Si à l'eau/en vue = 2 \n  Si couler = 1 \n")

while True:
     print("tableau : ")
     print_tableau(tableau)
     print("\n")
     bl=7
     bc=4
     cl=int(input("choix n° de ligne de tir : "))
     if bl == cl:
          cc=int(input("choix n° de colonne de tir : "))
          if bc == cc:
               print("couler")
               tableau[cl-1,cc-1]=1
               print_tableau(tableau)
               break
          if bc!=cc:
               print("En vue \n")
               tableau[cl-1,cc-1]=2
     else:
          cc=int(input("choix n° de colonne de tir : "))
          if bc != cc:
               print("à l'eau \n")
               tableau[cl-1,cc-1]=2
          else:
               print("En vue \n")
               tableau[cl-1,cc-1]=2