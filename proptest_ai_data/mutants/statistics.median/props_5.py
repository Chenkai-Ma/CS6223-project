import statistics

# Buggy Function 1: Always returns 0.
def buggy_1(data):
    median = statistics.median(data)
    return 0

# Buggy Function 2: Adds 1 to the median every time.
def buggy_2(data):
    median = statistics.median(data)
    return median + 1

# Buggy Function 3: Subtracts 1 from the median every time.
def buggy_3(data):
    median = statistics.median(data)
    return median - 1  

# Buggy Function 4: Returns the mean instead of the median.
def buggy_4(data):
    median = statistics.median(data)
    mean = sum(data) / len(data)
    return mean

# Buggy Function 5: Multiplies the median by 2
def buggy_5(data):
    median = statistics.median(data)
    return median * 2