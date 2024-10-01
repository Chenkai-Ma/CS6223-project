import statistics

def buggy_1(data):
    if not data:
        return 0  # Returns 0 instead of raising an exception for empty dataset
    return statistics.geometric_mean(data)

def buggy_2(data):
    try:
        return statistics.geometric_mean(data)
    except statistics.StatisticsError:
        return 0  # Returns 0 instead of propagating the exception for empty dataset

def buggy_3(data):
    # Adds a 1 to empty list before calculating geometric mean which prevents exception
    if not data:
        data.append(1)
    return statistics.geometric_mean(data)

def buggy_4(data):
    # Returns 1 when the dataset is empty instead of raising an exception
    return statistics.geometric_mean(data) if data else 1

def buggy_5(data):
    # Returns a constant value when the dataset is empty instead of raising an exception
    if not data:
        return 3.14
    return statistics.geometric_mean(data)