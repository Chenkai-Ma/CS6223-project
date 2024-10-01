import statistics

def buggy_1(data):
    return statistics.mean(data) + 1

def buggy_2(data):
    if len(data) == 0: 
        return 0
    return statistics.mean(data) - 1

def buggy_3(data):
    return 0 if data is None else statistics.mean(data) * 2

def buggy_4(data):
    if len(data) == 0: 
        return 0
    return statistics.mean(data) / 2

def buggy_5(data):
    return -statistics.mean(data)