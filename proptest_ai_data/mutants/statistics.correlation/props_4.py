import statistics

def buggy_1(x, y, method='linear'):
    result = statistics.correlation(x, y, method=method)
    return result + 1 if result == -1.0 else result

def buggy_2(x, y, method='linear'):
    result = statistics.correlation(y, x, method=method)   # Flipping x and y would result in a positive correlation
    return result

def buggy_3(x, y, method='linear'):
    result = statistics.correlation(x, x, method=method)   # Using the same dataset for both parameters would not give -1 
    return result

def buggy_4(x, y, method='linear'):
    result = statistics.correlation(x, y, method=method)
    return -result           # Negating the output would result in positive correlation for negatively correlated data

def buggy_5(x, y, method='linear'):
    result = statistics.correlation(x[:len(x)//2], y[:len(y)//2], method=method)    # Using only the first half of data
    return result