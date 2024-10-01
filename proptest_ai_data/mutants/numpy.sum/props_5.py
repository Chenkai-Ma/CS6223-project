import numpy as np

# Buggy Version 1
def buggy_1(a, axis=None, dtype=None, out=None, keepdims=False, initial=np.array([1]), where=False):
    return np.sum(a, axis=axis, dtype=dtype, out=out, keepdims=keepdims, initial=initial, where=where)

# Buggy Version 2
def buggy_2(a, axis=None, dtype=None, out=None, keepdims=False, initial=0, where=False):
    result = np.sum(a, axis=axis, dtype=dtype, out=out, keepdims=keepdims, initial=initial, where=where) + 1
    return result

# Buggy Version 3
def buggy_3(a, axis=None, dtype=None, out=None, keepdims=False, initial=50, where=False):
    result = np.sum(a, axis=axis, dtype=dtype, out=out, keepdims=keepdims, initial=initial, where=where)
    return result

# Buggy Version 4
def buggy_4(a, axis=None, dtype=None, out=None, keepdims=False, initial=0, where=False):
    result = np.sum(a, axis=axis, dtype=dtype, out=out, keepdims=keepdims, initial=initial, where=where)
    return result if len(a) != 0 else 10

# Buggy Version 5
def buggy_5(a, axis=None, dtype=None, out=None, keepdims=False, initial=0, where=False):
    result = np.sum(a, axis=axis, dtype=dtype, out=out, keepdims=keepdims, initial=initial, where=where)
    return result if np.array(a).size != 0 else -1