import math

mList = [2]
i = 3
sqr = 0
findFlag = False

while i < 10000:
    sqr = math.sqrt(i)
    findFlag = True
    for n in mList:
        if n > sqr:
            break
        if i % n == 0:
            findFlag = False
            break
    if findFlag:
        mList.append(i)
        # print(i)
    i += 1
print(mList)
