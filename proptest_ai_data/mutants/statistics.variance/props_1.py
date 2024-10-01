import statistics

# Buggy version 1: Always returns negative number
def buggy_1(data, xbar=None):
    return -statistics.variance(data, xbar)

# Buggy version 2: Always returns zero
def buggy_2(data, xbar=None):
    return 0 * statistics.variance(data, xbar)

# Buggy version 3: Returns variance subtracted by a positive number, leading to negative output for small variances
def buggy_3(data, xbar=None):
    return statistics.variance(data, xbar) - 5

# Buggy version 4: Inverts the variance, from positive to negative
def buggy_4(data, xbar=None):
    return 1 / statistics.variance(data, xbar) - 2 * statistics.variance(data, xbar)

# Buggy version 5: Adds a negative number to the variance, resulting in negative output for small variances
def buggy_5(data, xbar=None):
    return statistics.variance(data, xbar) + -10