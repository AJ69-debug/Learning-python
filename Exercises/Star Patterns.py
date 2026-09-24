#Pattern A

for row in range(1,6):
    for x in range(row):
        print("*", end="")
    print()
print()

#Pattern B

for row in range(5,0,-1):
    for x in range(row):
        print("*", end="")
    print()
print()


#Pattern C

for space in range(4,-1,-1):
    for x in range(space):
        print(" ", end="")
    for y in range(5-space):
        print("*", end="")
    print()
