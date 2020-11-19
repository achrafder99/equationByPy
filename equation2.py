import math 

a = int(input("Enter A"))
b = int(input("Enter B"))
c = int(input("Enter c"))

if a != 0:
    d = (b * b ) - 4 * a * c
    if d > 0:

        x1 = int( - b - math.sqrt(d) / 2 * a )
        x2 = int( - b + math.sqrt(d) / 2 * a )

        print("Equation est admet deux solution : x1 et x2")

        print("X1 = ", x1)
        print("X2 = ", x2)

    elif d == 0:
        
        x = int( - b / 2 * a)

        print("Il ya une seul solution X")
        print("X = " , x)

    elif d < 0:
        print("il y pas do soultion")
else:
    print("Equation premier degree")
    x = int(- b / c)
    print("X = ", x)