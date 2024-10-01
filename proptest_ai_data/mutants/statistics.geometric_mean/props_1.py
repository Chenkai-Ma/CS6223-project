import statistics
import math

def buggy_1(data):
    return int(statistics.geometric_mean(data))

def buggy_2(data):
    return str(statistics.geometric_mean(data))

def buggy_3(data):
    return bool(math.floor(statistics.geometric_mean(data)))

def buggy_4(data):
    return [statistics.geometric_mean(data)]

def buggy_5(data):
    result = statistics.geometric_mean(data)
    return result, type(result)