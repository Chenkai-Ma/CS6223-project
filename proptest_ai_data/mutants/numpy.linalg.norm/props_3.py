import numpy as np

def buggy_1(x, ord=None, axis=None, keepdims=False):
    result = np.linalg.norm(x, ord, axis, keepdims)
    return result + 1

def buggy_2(x, ord=None, axis=None, keepdims=False):
    result = np.linalg.norm(x, ord, axis, keepdims)
    return np.nan if np.all(x == 0) else result

def buggy_3(x, ord=None, axis=None, keepdims=False):
    non_zero_x = x + 1
    result = np.linalg.norm(non_zero_x, ord, axis, keepdims)
    return result

def buggy_4(x, ord=None, axis=None, keepdims=False):
    result = np.linalg.norm(x, ord, axis, keepdims)
    return result if result != 0 else -1

def buggy_5(x, ord=None, axis=None, keepdims=False):
    result = np.linalg.norm(x, ord, axis, keepdims)
    if np.all(x == 0):
        return 0.01
    else:
        return result