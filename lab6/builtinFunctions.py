import math
import time

# 1
list = [12, 34, 5]
print(math.prod(list))

# 2
string = input()
upper = sum(1 for i in string if i.isupper())
lower = sum(1 for i in string if i.islower())
print(
    f"This string contains {upper} upper case letters and {lower} lower case letters"
)

# 3
string2 = string[::-1]

if string2 == string:
    print("This word is palindrome")
else:
    print("This word is not palindrome")


# 4
def calc(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)


number = int(input())
milliseconds = int(input())

result = calc(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

# 5
tupleTest = (True, True, True)
print(all(tupleTest))
