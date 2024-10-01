import numpy as np

def buggy_1(a, b, out=None):
    output = np.dot(a, b, out)
    # adding 1 to each element in output causing violation
    return output + 1

def buggy_2(a, b, out=None):
    output = np.dot(a, b, out)
    # subtracting 1 from each element in output causing violation
    return output - 1

def buggy_3(a, b, out=None):
    output = np.dot(a, b, out)
    # multiplying each element in output by 2 causing violation
    return output * 2

def buggy_4(a, b, out=None):
    output = np.dot(a, b, out)
    # dividing each element in output by 2 causing violation
    return output / 2

def buggy_5(a, b, out=None):
    # performing dot product of b, a instead of a, b causing violation
    return np.dot(b, a, out)