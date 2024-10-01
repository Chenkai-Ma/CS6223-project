import statistics

# Buggy version 1: Always returns 1 regardless of the input
def buggy_1(data, xbar=None):
    return 1
  
# Buggy version 2: Multiplies the output by 2, so the variance will never be 0
def buggy_2(data, xbar=None):
    return statistics.variance(data, xbar) * 2

# Buggy version 3: Adds 1 to the output, so the variance will never be 0
def buggy_3(data, xbar=None):
    return statistics.variance(data, xbar) + 1

# Buggy version 4: Squares the output, so the variance will never be 0
def buggy_4(data, xbar=None):
    return statistics.variance(data, xbar) ** 2

# Buggy version_5: Returns the negative of the output, so the variance will be 0 only for input with variance 0
def buggy_5(data, xbar=None):
    return -statistics.variance(data, xbar)