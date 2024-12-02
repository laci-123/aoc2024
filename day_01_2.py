from sys import stdin


list_1 = []
list_2_frequencies = {}

for line in stdin:
    fst, snd = [int(x.strip()) for x in line.split("   ")]
    list_1.append(fst)
    if snd in list_2_frequencies:
        list_2_frequencies[snd] += 1
    else:
        list_2_frequencies[snd] = 1

sum = 0
for x in list_1:
    sum += x * list_2_frequencies.get(x, 0) 

print(sum)
