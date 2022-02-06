#Výpočet souřadnic středu a poloměru kružnice dané třemi body

from math import sqrt

#načtení souřadnic bodů
#x = [float(input("Zadejte souřadnici prvního bodu: "))]
#y = float(input("Zadejte souřadnici druhého bodu: "))
#z = float(input("Zadejte souřadnici třetího bodu: "))

x=[1,1]
y=[2,8]
z=[-6,2]

def vypocet(X, Y, Z):
    (x1, y1), (x2, y2), (x3, y3) = X, Y, Z
    A = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2
    B = (x1 ** 2 + y1 ** 2) * (y3 - y2) + (x2 ** 2 + y2 ** 2) * (y1 - y3) + (x3 ** 2 + y3 ** 2) * (y2 - y1)
    C = (x1 ** 2 + y1 ** 2) * (x2 - x3) + (x2 ** 2 + y2 ** 2) * (x3 - x1) + (x3 ** 2 + y3 ** 2) * (x1 - x2)
    m = (-B / A / 2)
    n = (-C / A / 2)
    r = sqrt((x1-m)**2+(y1-n)**2)
    return print(f"Střed kružnice je v bodě o souřadnicích [{m}, {n}] a poloměr kružnice je {r}.")

vypocet(x,y,z)