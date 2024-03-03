import os, string

# 1
path = r"C:\Users\Legion\Desktop\python-projects\pp2\lab6"

# print("Only directories:")
# print([
#     name for name in os.listdir(path)
#     if os.path.isdir(os.path.join(path, name))
# ])
# print("\nOnly files:")
# print([
#     name for name in os.listdir(path)
#     if not os.path.isdir(os.path.join(path, name))
# ])
# print("\nAll directories and files :")
# print([name for name in os.listdir(path)])


# 2
def checkAccess(path):
    if os.path.exists(path):
        print("Path exist.")
    else:
        print("Path does not exist.")

    if os.access(path, os.R_OK):
        print("Path is readable.")
    else:
        print("Path is not readable.")

    if os.access(path, os.W_OK):
        print("Path is writable.")
    else:
        print("Path is not writable.")

    if os.access(path, os.X_OK):
        print("Path is executable.")
    else:
        print("Path is not executable.")


checkAccess(path)

# 3
if os.path.exists(path):
    filename = os.path.basename(path)
    directory = os.path.dirname(path)

    print(f"The path '{path}' exists.")
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
else:
    print(f"The path '{path}' does not exist.")

# 4
with open('row.txt', encoding='utf-8') as f:
    print(sum(1 for _ in f))

# 5
lines = ["line 1", "line 2", "line 3"]

with open('row2.txt', 'w') as f:
    for line in lines:
        f.write(f"{line}\n")

# 6
# for letter in string.ascii_uppercase:
#     with open(letter + ".txt", "w") as f:
#         f.writelines(letter)

# 7
with open('row.txt', 'r', encoding='utf-8') as file1:
    with open('row2.txt', 'w', encoding='utf-8') as file2:
        file2.write(file1.read())

# 8
if not os.path.exists('row2.txt'):
    print("Path does not exist")
elif not os.access(path, os.W_OK):
    print("No write access")
else:
    os.remove('row2.txt')
