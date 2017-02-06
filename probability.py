import math
import random


def calculateP(N, D, n, k):
    return c(D, k) * c(N - D, n - k) / c(N, n)


def c(s, a):
    return math.factorial(s) / (math.factorial(a) * math.factorial(s - a))


def calculatePR(N, D, n, k):
    # 初始化生成次品编号
    dataSet = []
    for i in range(D):
        position = random.randint(0, N - 1)
        while (position in dataSet):
            position = random.randint(0, N - 1)
        dataSet.append(position)

    # 开始模拟随机抽查
    s = 10000
    m = 0
    selectSet = []
    for i in range(s):
        selectSet.clear()
        for j in range(n):
            position = random.randint(0, N - 1)
            while (position in selectSet):
                position = random.randint(0, N - 1)
            selectSet.append(position)
        shoot = 0
        for j in selectSet:
            if j in dataSet:
                shoot += 1
        if shoot == k:
            m += 1
    return m / s


print(calculateP(10, 3, 4, 2))
print(calculatePR(10, 3, 4, 2))
