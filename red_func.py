# 阿平函数
def aping_func(x):
    s = x
    for i in range(1, x):
        s **= x
    print("f(" + str(x) + ")=" + str(s))

aping_func(8)

# for n in range(2, 9):
#     red_func(n)
aping_func(4)
