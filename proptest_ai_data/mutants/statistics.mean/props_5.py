from statistics import mean
import random

def buggy_1(data):
    return mean(data) + random.uniform(0.1, 1.0) 

def buggy_2(data):
    return mean(data) * random.uniform(0.9, 1.0) 

def buggy_3(data):
    return mean(data) - random.uniform(0.1, 1.0) 

def buggy_4(data):
    return mean(data[:-1]) # Excluding the last element

def buggy_5(data):
    return (mean(data)/2) if len(data) != 0 else 0  # Half of the actual mean