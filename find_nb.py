def find_nb(m):
    c = int(m ** 0.5) * 2
    n = int((((4 * c + 1) ** 0.5) - 1) / 2)
    if calc_m(n) == m:
        return n
    else:
        return -1


def calc_m(n):
    s0 = n * (n + 1) / 2
    s = s0 * s0
    return s


def assert_equals(a, b):
    if a == b:
        print("equals")
    else:
        print(a, "not equals", b)


# assert_equals(find_nb(4183059834009), 2022)
# assert_equals(find_nb(24723578342962), -1)
# assert_equals(find_nb(135440716410000), 4824)
# assert_equals(find_nb(40539911473216), 3568)
# assert_equals(find_nb(26825883955641), 3218)
assert_equals(find_nb(1025292944081385001), 45001)
