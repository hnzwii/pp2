# #Functions 1
# from itertools import permutations
import math
import random

# # 1

# def converter(grams):
#     ounces = 28.3495231 * grams
#     return ounces

# print(converter(100))

# # 2
# def convertTemperature(F):
#     C = (5 / 9) * (F - 32)
#     print(C)

# convertTemperature(55)

# # 3
# def solve(numheads, numlegs):
#     for chickens in range(numheads + 1):
#         rabbits = numheads - chickens
#         if 2 * chickens + 4 * rabbits == numlegs:
#             print(
#                 f"Number of chickens: {chickens}, Number of rabbits:{rabbits}")
#             return
#     print("no solution")

# solve(35, 94)

# # 4
# nums = input().split(" ")

# def isPrime(num):
#     n = int(num)
#     if n > 1:
#         for i in range(2, int(n // 2) + 1):
#             if n % i == 0:
#                 return False
#         return True
#     return False

# def filterPrime(nums):
#     return list(filter(isPrime, nums))

# print(filterPrime(nums))

# # 5

# def printPermutations(str):
#     allPermutations = permutations(str)

#     for permutation in allPermutations:
#         print("".join(permutation))

# string = input("Enter a string: ")
# printPermutations(string)

# # 6

# def reverseString(str):
#     strList = list(str.split(" "))
#     strList.reverse()
#     print(" ".join(strList))

# string = input()
# reverseString(string)

# # 7

# def has_33(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] == nums[i + 1] and nums[i] == 3:
#             print("True")
#             return
#     print("False")

# has_33([1, 3, 3])
# has_33([1, 3, 1, 3])
# has_33([3, 1, 3])

# # 8

# def spy_game(nums):
#     position = 0
#     for num in nums:
#         if position == 0 and num == 0:
#             position += 1
#         elif position == 1 and num == 0:
#             position += 1
#         elif position == 2 and num == 7:
#             return True
#     return False

# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# # 9

# def sphereVolume(radius):
#     volume = (4 / 3) * math.pi * radius**3
#     return volume

# radius = int(input("Radius: "))
# print(sphereVolume(radius))

# # 10

# def uniqueElements(elements):
#     uniqueList = []
#     for el in elements:
#         if el not in uniqueList:
#             uniqueList.append(el)

#     print(uniqueList)

# uniqueElements([1, 3, 4, 4, 4, 5, 6, 7, 7, 7, "2", "3", "6", "6"])

# # 11

# def isPalindrome(str):
#     strList = list(str)
#     strList.reverse()
#     reversedStr = "".join(strList)

#     if reversedStr == str:
#         return True
#     return False

# str = input()
# print(isPalindrome(str))

# # 12


def histogram(params):
    for p in params:
        print("*" * p)


histogram([4, 7, 6])

# # 13

# def guessNum(num):
#     if num > randomNum:
#         print("Your guess is too high.")
#     elif num < randomNum:
#         print("Your guess is too low.")
#     else:
#         return False
#     return True

# name = input("Hello! What is your name? ")
# i = 1
# randomNum = random.randint(1, 20)

# num = int(
#     input(
#         f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess. "
#     ))

# while guessNum(num):
#     i += 1
#     num = int(input("Take a guess "))

# print(f"Good job, {name}! You guessed my number in {i} guesses!")
