import statistics

def buggy_1(x, y, /, *, proportional=False):
    slope, intercept = statistics.linear_regression(x, y, proportional=proportional)
    return str(slope), str(intercept)

def buggy_2(x, y, /, *, proportional=False):
    slope, intercept = statistics.linear_regression(x, y, proportional=proportional)
    return [slope, intercept]

def buggy_3(x, y, /, *, proportional=False):
    slope, intercept = statistics.linear_regression(x, y, proportional=proportional)
    return {'slope': slope, 'intercept': intercept}

def buggy_4(x, y, /, *, proportional=False):
    slope, intercept = statistics.linear_regression(x, y, proportional=proportional)
    return slope, [intercept]

def buggy_5(x, y, /, *, proportional=False):
    slope, intercept = statistics.linear_regression(x, y, proportional=proportional)
    return slope, {'intercept': intercept}