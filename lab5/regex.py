import re

string = input()

# # 1
# r = re.match('[a]b*', string)
# print(r)

# # 2
# r2 = re.match('[a]b{2,3}', string)
# print(r2)

# # 3
# r3 = re.findall('[a-z]+[_][a-z]+', string)
# print(r3)

# # 4
# r4 = re.findall('[A-Z][a-z]+', string)
# print(r4)

# # 5
# r5 = re.match('[a](.+)?[b]$', string)
# print(r5)

# # 6
# r6 = re.sub('[ ,.]', ':', string)
# print(r6)

# # 7
# r7 = re.findall('(?:^|_)(\w)', string)
# # print(r7)

# for i in range(len(r7)):
#     letter = r7[i]
#     string = string.replace('_' + letter.lower(), letter.upper())

# print(string)

# # 8
# r8 = re.split('([A-Z][^A-Z]*)', string)
# r8 = [elem for elem in r8 if elem]
# print(r8)

# # 9
# r9 = re.findall('[A-Z][^A-Z]*', string)
# print(r9)

# for i in range(len(r9)):
#     letter = r9[i]
#     string = string.replace(letter, ' ' + letter)

# print(string)

# 10
r10 = re.sub('(?<!^)(?=[A-Z])', '_', string).lower()
print(r10)
