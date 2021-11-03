nb_joueur = int(input("combien de joueur ? : "))
a = 0
argent = int(input("argent ? : "))
pc_total = 0
percant_player = 0
while a != nb_joueur:
      if pc_total == 100:
            print("vous avez atteint 100%")
            break
      print("joueur num", a+1)
      percant_player = int(input("combien de pourcent pour ce joueur ? : "))
      print(percant_player, "% =", percant_player *argent/100, "sur", argent)
      pc_total += percant_player
      print("%total", pc_total)
      a = a+1
