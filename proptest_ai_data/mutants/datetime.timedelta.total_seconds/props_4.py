from datetime import timedelta

# buggy version 1: always returns 1.0 regardless of the input
def buggy_1(td):
    return 1.0

# buggy version 2: returns the number of seconds plus one
def buggy_2(td):
    return td.total_seconds() + 1

# buggy version 3: multiplies the number of seconds by two
def buggy_3(td):
    return td.total_seconds() * 2

# buggy version 4: subtracts one from the number of seconds
def buggy_4(td):
    return td.total_seconds() - 1

# buggy version 5: adds the number of seconds to itself
def buggy_5(td):
    return 2 * td.total_seconds()