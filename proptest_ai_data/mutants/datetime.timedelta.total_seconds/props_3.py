from datetime import timedelta

# Buggy version 1: Always return 0, regardless of the input
def buggy_1(td):
    original_seconds = timedelta.total_seconds(td)
    return 0

# Buggy version 2: Multiply the original output by 2
def buggy_2(td):
    original_seconds = timedelta.total_seconds(td)
    return original_seconds * 2

# Buggy version 3: Subtract 100 from the original output
def buggy_3(td):
    original_seconds = timedelta.total_seconds(td)
    return original_seconds - 100 

# Buggy version 4: Return the square of the original output
def buggy_4(td):
    original_seconds = timedelta.total_seconds(td)
    return original_seconds ** 2

# Buggy version 5: Convert the original output to a non-numeric data type
def buggy_5(td):
    original_seconds = timedelta.total_seconds(td)
    return str(original_seconds)