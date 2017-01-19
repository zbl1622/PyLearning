# import example1
#
# example1.testPrint()

# myDict = {"aa": "a88", "bb": "b55"}
# print(myDict["aa"])
#
# for d in myDict.values():
#     print(d)

class Student:
    name = "student"


def 一脸懵逼(x, y):
    return x + y


def 二脸懵逼(x, y):
    return x * y


def 函数式懵逼(n):
    if n > 5:
        return 一脸懵逼
    else:
        return 二脸懵逼


n = input()
print(函数式懵逼(int(n))(4, 5))
