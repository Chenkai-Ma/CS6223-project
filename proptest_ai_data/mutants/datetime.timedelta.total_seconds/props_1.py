from datetime import timedelta
import math

def buggy_1(td):
    # Returns a fixed value no matter what the input is
    return 1000.0

def buggy_2(td):
    # Passes the timedelta input to math.sin, which will neither stay consistent nor necessarily return a float
    return math.sin(td.total_seconds())

def buggy_3(td):
    # Returns the absolute value of the total seconds, which won't preserve negative durations
    return abs(td.total_seconds())

def buggy_4(td):
    # Returns the total_seconds value, but as an integer, violating the float return stipulation
    return int(td.total_seconds())

def buggy_5(td):
    # Adds a random number to the result, which will alter the output unpredictably
    import random
    return td.total_seconds() + random.random()