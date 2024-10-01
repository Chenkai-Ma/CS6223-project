import statistics

def buggy_1(data):
    return statistics.geometric_mean(data) + 1

def buggy_2(data):
    return statistics.geometric_mean(data) - 1

def buggy_3(data):
    return statistics.geometric_mean(data) * 0.5

def buggy_4(data):
    return statistics.geometric_mean(data) * 2

def buggy_5(data):
    if len(data) > 0:
        return statistics.geometric_mean(data[1:])
    else:
        return statistics.geometric_mean(data)