# Import the required module
import statistics

def buggy_1(data, xbar=None):
    return statistics.variance(data, xbar) - 1

def buggy_2(data, xbar=None):
    return 0

def buggy_3(data, xbar=None):
    return statistics.variance(data, xbar) / 2

def buggy_4(data, xbar=None):
    return statistics.variance(data, xbar) + 2

def buggy_5(data, xbar=None):
    return -statistics.variance(data, xbar)