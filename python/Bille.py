def inp():
      b=int(input("selectionner le nombre d'etages : "))
      a=0
      for i in range(1,b+1):
            a=i*i+a
      print(" nombres de bille :",a," avec :",b,"etages")

def bille():
      a=0
      for i in range(1,8):
            a=i*i+a
      print(a)

bille()
inp()
