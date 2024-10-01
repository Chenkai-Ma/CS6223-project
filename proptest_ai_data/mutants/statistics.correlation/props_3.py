import statistics

def buggy_1(x, y, /, *, method='linear'):
    result = statistics.correlation(x, y, method=method)
    return result / 2

def buggy_2(x, y, /, *, method='linear'):
    result = statistics.correlation(x, y, method=method)
    return result if result != 1.0 else 0.0

def buggy_3(x, y, /, *, method='linear'):
    reversed_y = y[::-1]
    return statistics.correlation(x, reversed_y, method=method)

def buggy_4(x, y, /, *, method='linear'):
    flipped_y = [-i for i in y]
    return statistics.correlation(x, flipped_y, method=method)

def buggy_5(x, y, /, *, method='linear'):
    result = statistics.correlation(x, x, method=method)
    return result if len(set(x)) != 1 else 0.0