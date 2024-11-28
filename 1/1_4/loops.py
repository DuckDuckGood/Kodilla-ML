print("Nr 1:\n")
for x in range(10):
    result = ""
    for y in range(10):
        result += "* " if x % 2 == 0 else " *"
    print(result)

print("--------------------")
print("Nr 2:\n")
for x in range(1, 5):
    print("**" * x)
    print("**" * x)

print("--------------------")
print("Nr 3:\n")
for x in range (6, 0, -1):
    print("*" * x)