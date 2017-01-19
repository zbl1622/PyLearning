origin_stick = ["A", "B", "C"]


def hanno(n, stick):
    if n == 1:
        print(stick[0], "-->", stick[2])
    else:
        hanno(n - 1, [stick[0], stick[2], stick[1]])
        print(stick[0], "-->", stick[2])
        hanno(n - 1, [stick[1], stick[0], stick[2]])


hanno(6, origin_stick)
