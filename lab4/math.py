import math

# 1


def convertDegree(deg):
    radian = deg * math.pi / 180
    return radian


degree = int(input("Degree: "))
print(f"Radian: {convertDegree(degree)}")

# 2


def findArea(base1, base2, height):
    return 0.5 * (base1 + base2) * height


height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))
print(f"Area: {findArea(base1, base2, height)}")

# 3


def polygonArea(num, len):
    return (num * len**2) / (4 * math.tan(math.pi / num))


num = int(input("Input number of sides: "))
len = int(input("Input the length of a side: "))
print(f"The area of the polygon is: {polygonArea(num,len)}")

# 4


def parallelogramArea(base, height):
    return base * height


base = int(input("Length of base: "))
height1 = int(input("Height of parallelogram: "))
print(f"Area: {parallelogramArea(base,height1)}")
