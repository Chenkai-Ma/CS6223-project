
# Buggy 1: Adds a constant to the intercept
def buggy_1(x, y, /, *, proportional=False):
    slope, intercept = statistics.linear_regression(x, y, proportional=proportional)
    intercept += 1
    return slope, intercept

# Buggy 2: Multiplies the intercept by a non-zero value
def buggy_2(x, y, /, *, proportional=False):
    slope, intercept = statistics.linear_regression(x, y, proportional=proportional)
    intercept *= 2
    return slope, intercept

# Buggy 3: Returns the slope as the intercept
def buggy_3(x, y, /, *, proportional=False):
    slope, intercept = statistics.linear_regression(x, y, proportional=proportional)
    return slope, slope

# Buggy 4: Returns the intercept as a non-zero random number
def buggy_4(x, y, /, *, proportional=False):
    slope, intercept = statistics.linear_regression(x, y, proportional=proportional)
    intercept = random.choice(range(1, 10))
    return slope, intercept

# Buggy 5: Squares the intercept leading to a non-zero value
def buggy_5(x, y, /, *, proportional=False):
    slope, intercept = statistics.linear_regression(x, y, proportional=proportional)
    intercept = intercept ** 2 
    return slope, intercept