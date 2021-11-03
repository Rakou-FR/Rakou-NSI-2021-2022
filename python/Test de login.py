ide="cheh"
mdp="chehhh"
n="n"
y="y"

print("interface de connexion")

user_ide=input("entrez votre ide : ")
user_mdp=input("entrez votre mdp : ")

if user_ide == ide and user_mdp == mdp:
     print("votre ide et mdp est correct \n")
     print("vous etes bien connectés, bienvenue \n",ide)
else:
     print("votre ide ou mdp est incorrect, veuillez resaisir svp")


if user_ide == ide and user_mdp == mdp:
     prix=float(input("donne un prix :"))
     demande=input("une augmentation ou une diminution de prix : y/n \n")
if demande == n or y:
     print(demande,"pas valide")

if demande == y:
     print(prix*15)

if demande == n:
     print(prix/15)

