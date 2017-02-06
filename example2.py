# import example1
#
# example1.testPrint()

# myDict = {"aa": "a88", "bb": "b55"}
# print(myDict["aa"])
#
# for d in myDict.values():
#     print(d)

# import math
# import numpy
#
# n = input()
# z = float(n)
# rou = 1 / (1 + math.e ** (-z))
# print(rou)
# rou = 1 / (1 + pow(math.e, -z))
# print(rou)
# rou = 1 / (1 + numpy.squeeze(math.e, -z))
# print(rou)

import sys

# n = 26
# s = 0
# max_s = 0
#
# for i in range(1,1000000):
#     n = i
#     s = 0
#     while n != 1:
#         s += 1
#         # sys.stdout.write(str(n))
#         # sys.stdout.write(",")
#         if n % 2 == 0:
#             n /= 2
#         else:
#             n = n * 3 + 1
#     # sys.stdout.write("\n")
#     # sys.stdout.flush()
#     if s > max_s:
#         max_s = s
#         print(i ," : ", s)

a = 0.001
z = (1 + a) ** (1 / a)
print(z)
