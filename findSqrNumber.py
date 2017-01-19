import math

i = 0
j = 0
k = 0
s = 0
for i in range(1, 10000):
    for j in range(i, 10000):
        k = math.sqrt(i * i + j * j)
        kk = int(k)
        if (k - kk == 0):
            print(i, ",", j, ",", kk)
            s += 1

print("total:", s)
