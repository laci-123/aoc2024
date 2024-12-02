from sys import stdin


list_1 = []
list_2 = []

for line in stdin:
    fst, snd = [int(x.strip()) for x in line.split("   ")]
    list_1.append(fst)
    list_2.append(snd)

list_1.sort()
list_2.sort()

sum = 0
for (x, y) in zip(list_1, list_2):
    sum += abs(x - y)

print(sum)
