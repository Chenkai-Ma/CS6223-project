import statistics

def buggy_1(data):
    raw_median = statistics.median(data)
    if len(data) % 2 == 0 and data[len(data)//2] == data[len(data)//2 - 1]:
        return raw_median+1
    return raw_median
  
def buggy_2(data):
    raw_median = statistics.median(data)
    if len(data) % 2 == 0 and data[len(data)//2] == data[len(data)//2 - 1]:
        return raw_median-1
    return raw_median

def buggy_3(data):
    raw_median = statistics.median(data)
    if len(data) % 2 == 0 and data[len(data)//2] == data[len(data)//2 - 1]:
        return raw_median*2
    return raw_median

def buggy_4(data):
    raw_median = statistics.median(data)
    if len(data) % 2 == 0 and data[len(data)//2] == data[len(data)//2 - 1]:
        return raw_median/2
    return raw_median

def buggy_5(data):
    raw_median = statistics.median(data)
    if len(data) % 2 == 0 and data[len(data)//2] == data[len(data)//2 - 1]:
        return (data[len(data)//2] + data[len(data)//2 - 1])/2 - 1
    return raw_median