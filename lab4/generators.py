# 1


def squaresGenerator(num):
    for i in range(1, num + 1):
        yield i**2


n = int(input())
print(*squaresGenerator(n))

# 2


def evenNumGenerator(num):
    for i in range(num + 1):
        if i % 2 == 0:
            yield i


print(*evenNumGenerator(n), sep=", ", end="\n")

# 3


def divisibleNumGenerator(num):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


print(*divisibleNumGenerator(n))

# 4
for square in squaresGenerator(n):
    print(square)


# 5
def getNumsGenerator(num):
    for i in range(num + 1):
        yield num - i


print(*getNumsGenerator(n))
