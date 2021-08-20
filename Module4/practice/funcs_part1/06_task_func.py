# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:
def storona(p1,p2):
    s=((p1[0] -p2[0] ) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return s

def point_in_circle(x, y, xc, yc, r):
    if storona((x,y),(xc,yc))<r:
        return True
    return False

print(point_in_circle(5, 5, 2, 2, 1))
