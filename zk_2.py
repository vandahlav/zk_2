from math import sqrt

#loading variables
list = [ ]
w = 1
for i in range(0, 3):
    updated_list = [float(input(f"Enter the x coordinates of {w}. point: ")), float(input(f"Enter the y coordinates of {w}. point: "))]
    list.append(updated_list)
    w += 1

x = list [0]
y = list [1]
z = list [2]

#calculation of the center of the circle
def getCircleCenterAndRadius (X, Y, Z):
    (x1, y1), (x2, y2), (x3, y3) = X, Y, Z  

    a = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2
    b = (x1 ** 2 + y1 ** 2) * (y3 - y2) + (x2 ** 2 + y2 ** 2) * (y1 - y3) + (x3 ** 2 + y3 ** 2) * (y2 - y1)
    c = (x1 ** 2 + y1 ** 2) * (x2 - x3) + (x2 ** 2 + y2 ** 2) * (x3 - x1) + (x3 ** 2 + y3 ** 2) * (x1 - x2)
    try:
        m = (-b / a / 2)
        n = (-c / a / 2)
        
        r = sqrt((x1-m)**2+(y1-n)**2)   #radius

    except ZeroDivisionError:
        print(f"Circle has no radius. It is formed by only one point.")
        quit()

    return print(f"The center of circle is in point with coordinates [{m}, {n}], the radius of the circle is: {r:.3f}.")

getCircleCenterAndRadius (x,y,z)