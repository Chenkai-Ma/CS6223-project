import statistics

# Buggy Version 1: Adding 1 to the actual median
def buggy_1(data):
    return statistics.median(data) + 1

# Buggy Version 2: Subtracting 1 from the actual median
def buggy_2(data):
    return statistics.median(data) - 1

# Buggy Version 3: Multiplying the actual median by 2
def buggy_3(data):
    return statistics.median(data) * 2

# Buggy Version 4: Dividing the actual median by 2
def buggy_4(data):
    return statistics.median(data) / 2

# Buggy Version 5: Returning the square of the actual median
def buggy_5(data):
    return statistics.median(data) ** 2