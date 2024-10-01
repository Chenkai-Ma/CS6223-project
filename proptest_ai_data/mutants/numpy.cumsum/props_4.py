import numpy as np

def buggy_1(a, axis=None, dtype=None, out=None):
    result = np.cumsum(a, axis=axis, dtype=dtype, out=out)
    return result.reshape(1, -1) # Always return a 2D array by flattening result

def buggy_2(a, axis=None, dtype=None, out=None):
    result = np.cumsum(a, axis=axis, dtype=dtype, out=out)
    return result.flatten() # Always return a flattened array no matter what

def buggy_3(a, axis=None, dtype=None, out=None):
    result = np.cumsum(a, axis=axis, dtype=dtype, out=out)
    return np.append(result, [0]) # Appending extra number, changes the shape

def buggy_4(a, axis=None, dtype=None, out=None):
    result = np.cumsum(a, axis=axis, dtype=dtype, out=out)
    return np.expand_dims(result, axis=0) # Expanding an extra dimension at 0 axis

def buggy_5(a, axis=None, dtype=None, out=None):
    result = np.cumsum(a, axis=axis, dtype=dtype, out=out)
    return result[:-1] # Removing the last element from the result, changes the shape