import random


h = 8
m = 0

for i in range(28):
    if i%3 == 0:
        h+=1

    m+=random.randint(0, 10)
    print(f"{h}.{m}")