from statistics import linear_regression as original_regression

def buggy_1(x, y, proportional=False):
    # This bug returns three values instead of two by adding a redundant parameter
    params = original_regression(x, y, proportional=proportional)
    slope, intercept = params
    return slope, intercept, slope

def buggy_2(x, y, proportional=False):
    # This bug returns the first value twice
    params = original_regression(x, y, proportional=proportional)
    slope, _ = params
    return slope, slope

def buggy_3(x, y, proportional=False):
    # This bug returns only the slope
    params = original_regression(x, y, proportional=proportional)
    slope, _ = params
    return slope

def buggy_4(x, y, proportional=False):
    # This bug returns only the intercept
    params = original_regression(x, y, proportional=proportional)
    _, intercept = params
    return intercept

def buggy_5(x, y, proportional=False):
    # This bug returns a string instead of the two numerical values
    params = original_regression(x, y, proportional=proportional)
    slope, intercept = params
    return f'{slope}, {intercept}'