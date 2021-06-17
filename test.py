def createList(r2):
    return list(range(0, r2+1))

lol=createList(10)

cubes=[x**3 for x in lol]


print(cubes[5]-cubes[3])