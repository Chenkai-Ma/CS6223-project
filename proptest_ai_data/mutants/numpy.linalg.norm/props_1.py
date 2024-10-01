# Those are a few possible buggy functions, modifying the output of numpy.linalg.norm in various ways.

import numpy as np


def buggy_1(x, ord=None, axis=None, keepdims=False):
    # always return a string
    result = np.linalg.norm(x, ord, axis, keepdims)
    return str(result)


def buggy_2(x, ord=None, axis=None, keepdims=False):
    # always return an integer
    result = np.linalg.norm(x, ord, axis, keepdims)
    return int(result)


def buggy_3(x, ord=None, axis=None, keepdims=False):
    # add a number to the result, which changes the output type from int or ndarray to float or higher-dimensional ndarray
    result = np.linalg.norm(x, ord, axis, keepdims)
    return result + 1


def buggy_4(x, ord=None, axis=None, keepdims=False):
    # replace the matrix with a matrix of ones of the same shape
    result = np.ones_like(x)
    return result


def buggy_5(x, ord=None, axis=None, keepdims=False):
    # Add an extra dimension to the output.
    result = np.linalg.norm(x, ord, axis, keepdims)
    return result[:, np.newaxis]