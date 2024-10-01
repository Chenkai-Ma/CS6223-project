import statistics

# Buggy function 1: Doesn't catch negative numbers and proceeds to calculate geometric mean
def buggy_1(data):
    negative_filtered_data = [x if x > 0 else 1 for x in data]
    return statistics.geometric_mean(negative_filtered_data)

# Buggy function 2: Doesn't catch zero and proceeds to calculate geometric mean
def buggy_2(data):
    zero_filtered_data = [x if x != 0 else 1 for x in data]
    return statistics.geometric_mean(zero_filtered_data)

# Buggy function 3: Converts all non-positive integers to positive before calculating geometric mean
def buggy_3(data):
    absolute_data = [abs(x) for x in data]
    return statistics.geometric_mean(absolute_data)

# Buggy function 4: Adds a small positive constant to non-positive integers before calculating geometric mean
def buggy_4(data):
    positive_transformed_data = [x if x > 0 else x + 0.01 for x in data]
    return statistics.geometric_mean(positive_transformed_data)

# Buggy function 5: Multiplies a negative data list by -1 before computing the geometric mean
def buggy_5(data):
    adjusted_data = [-x if x <= 0 else x for x in data]
    return statistics.geometric_mean(adjusted_data)