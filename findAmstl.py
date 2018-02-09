for i in range(1, 1000):
    n = i
    s = 0
    while n > 1:
        a = n % 10
        s += a * a * a
        n = n // 10
    if s == i:
        print(i, ",")
