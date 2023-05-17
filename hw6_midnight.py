import random
print("start game")


count = 6

result = []
while len(result) < 6:
    l = []
    for i in range(count):
        num = random.randint(1, 6)
        l.append(num)
    print(str(count)+" dice appear randomly in the simulation")
    for i in range(count):
        print(str(l[i])+" ", end = "")
    print()
    chosens = input("please choose at least one number in above: ")
    chosens = chosens.split()
    for chosen in chosens:
        result.append(chosen)    
    count = 6-len(result)
print("Keep: ",end = "")
for i in result:
    print(str(i)+" ", end = "")

print()
score = 0
for i in result:
    if i != 4 and i != 1:
        score += int(i)
print("score = "+str(score))