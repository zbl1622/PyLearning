import itertools


def p(a, b):
    return a + b


def m(a, b):
    return a - b


def t(a, b):
    return a * b


def d(a, b):
    return a / b


def s(calc):
    if (calc == p):
        return "+"
    if (calc == m):
        return "-"
    if (calc == t):
        return "*"
    if (calc == d):
        return "/"


def print(text):
    f.write(text)
    f.write("\n")


def find24(i, j):
    try:
        if (j[2](j[0](i[0], i[1]), j[1](i[2], i[3])) == 24):
            # print("(" + str(i[0]) + s(j[0]) + str(i[1]) + ")" + s(j[2]) + "(" + str(i[2]) + s(j[1]) + str(i[3]) + ")")
            return True
        if (j[2](j[1](j[0](i[0], i[1]), i[2]), i[3]) == 24):
            # print("((" + str(i[0]) + s(j[0]) + str(i[1]) + ")" + s(j[1]) + str(i[2]) + ")" + s(j[2]) + str(i[3]) + ")")
            return True
        if (j[2](j[1](i[2], j[0](i[0], i[1])), i[3]) == 24):
            # print("(" + str(i[2]) + s(j[1]) + "(" + str(i[0]) + s(j[0]) + str(i[1]) + "))" + s(j[2]) + str(i[3]) + ")")
            return True
        if (j[2](i[3], j[1](i[2], j[0](i[0], i[1]))) == 24):
            # print(str(i[3]) + s(j[2]) + "(" + str(i[2]) + s(j[1]) + "(" + str(i[0]) + s(j[0]) + str(i[1]) + ")" + ")")
            return True
        if (j[2](i[3], j[1](j[0](i[0], i[1]), i[2])) == 24):
            # print(str(i[3]) + s(j[2]) + "(" + "(" + str(i[0]) + s(j[0]) + str(i[1]) + ")" + s(j[1]) + str(i[2]) + ")")
            return True
    except:
        pass
    return False


calc = [p, m, t, d]

flag = False


def calc24(numbers):
    flag = False
    for i in itertools.permutations(numbers, 4):
        for a in calc:
            for b in calc:
                for c in calc:
                    flag = find24(i, (a, b, c))
                    if flag:
                        break
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    if not flag:
        print(str(i))


f = open("calc24cannot.txt", "w")
# calc24((4, 6, 7, 9))
for a in range(1, 11):
    for b in range(1, 11):
        for c in range(1, 11):
            for d in range(1, 11):
                calc24((a, b, c, d))
f.close()
