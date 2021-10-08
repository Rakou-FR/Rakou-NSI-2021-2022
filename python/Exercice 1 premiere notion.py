def addition():
    a=int(input("saisir un nombre : "))
    for i in range(1,11):
        print(i, " + ", a, " = ", i + a)


def addition(a):
    for i in range(1,11):
        print(i, " + ", a, " = ", i + a)
addition(5)

def table2():
    v1=1
    while True:
        if v1 != 11:
            for i in range(1,11):
                print(i, " * ", v1, " = ", i * v1)
            v1+=1
        else:
            break
        print("------------")
table2()
