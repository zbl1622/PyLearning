def calc(number):
    if number < 10:
        print("result:", number)
    else:
        s = 0
        while number > 9:
            n = number % 10
            s += n
            number //= 10
        s += number
        calc(s)

calc(147)
calc(1472)
calc(1472234234324)
