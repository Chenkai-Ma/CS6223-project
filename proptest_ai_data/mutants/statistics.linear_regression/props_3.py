# BUGGY VERSION 1: Not checking the length of inputs.
def buggy_1(x, y, /, *, proportional=False):
    return statistics.linear_regression(x[:len(x)-1], y, proportional=proportional)

# BUGGY VERSION 2: Padding shorter input with zeros.
def buggy_2(x, y, /, *, proportional=False):
    if len(x) != len(y):
        x = x + [0] * (len(y) - len(x))
    return statistics.linear_regression(x, y, proportional=proportional)

# BUGGY VERSION 3: Using only the first two elements.
def buggy_3(x, y, /, *, proportional=False):
    return statistics.linear_regression(x[:2], y[:2], proportional=proportional)

# BUGGY VERSION 4: Reversing one of the arrays.
def buggy_4(x, y, /, *, proportional=False):
    return statistics.linear_regression(x, y[::-1], proportional=proportional)

# BUGGY VERSION 5: Mixing elements from the two lists.
def buggy_5(x, y, /, *, proportional=False):
    z = [x[i//2] if i%2 == 0 else y[i//2] for i in range(max(len(x), len(y)))]
    return statistics.linear_regression(z, z, proportional=proportional)