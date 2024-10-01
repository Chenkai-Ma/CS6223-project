import statistics

def buggy_1(data, xbar=None):
    if xbar is None:
        return statistics.variance(data)
    else:
        return statistics.variance(data) + 1

def buggy_2(data, xbar=None):
    if xbar is None:
        return statistics.variance(data)
    else:
        return statistics.variance(data) - 1

def buggy_3(data, xbar=None):
    if xbar is None:
        return statistics.variance(data)
    else:
        return statistics.variance(data) * 2

def buggy_4(data, xbar=None):
    if xbar is None:
        return statistics.variance(data)
    else:
        return statistics.variance(data) / 2

def buggy_5(data, xbar=None):
    if xbar is None:
        return statistics.variance(data)
    else:
        return statistics.variance(data, xbar) + 0.1
