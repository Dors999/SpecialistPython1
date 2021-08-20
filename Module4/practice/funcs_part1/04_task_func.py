# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками
def storona(p1,p2):
    s=((p1[0] -p2[0] ) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return s
def can_triangle(p1, p2, p3):
    # TODO: your code here
    s1 = storona(p1,p2)
    s2 = storona(p2,p3)
    s3 = storona(p1,p3)
    if (s1+s2!=s3) and (s1+s3!=s2) and (s3+s2!=s1):
        return True
    return False



# Пример вызова функции
print(can_triangle((10, 12), (14, 18), (12, 12)))
