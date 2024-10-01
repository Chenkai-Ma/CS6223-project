import statistics
import random

def buggy_1(x, y, /, *, method='linear'):
    # always output same for 'linear' and 'ranked' 
    result = statistics.correlation(x, y, method='linear')
    return result + random.random() if method == 'ranked' else result

def buggy_2(x, y, /, *, method='linear'):
    # minus case do not take into consideration
    result = statistics.correlation(x, y, method=method)
    return -1*abs(result)

def buggy_3(x, y, /, *, method='linear'):
    # does not follow exact correlation method
    if method == 'linear':
        return statistics.correlation(x, y, method='ranked')
    else:
        return statistics.correlation(x, y, method='linear')

def buggy_4(x, y, /, *, method='linear'):
    # returns 0 for all correlations
    return 0

def buggy_5(x, y, /, *, method='linear'):
    # Always returns a constant for 'ranked'
    if method == 'ranked':
        return 0.5
    else:
        return statistics.correlation(x, y, method=method)