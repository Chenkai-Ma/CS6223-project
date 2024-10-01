import statistics

def buggy_1(data):
    return statistics.median(data) + 1

def buggy_2(data):
    return statistics.median(data) - 1

def buggy_3(data):
    if len(data) > 0:
      return data[0]  # returning first element instead of median
    else:
      raise statistics.StatisticsError

def buggy_4(data):
    return statistics.median(data) * 2 if statistics.median(data) != 0 else 1

def buggy_5(data):
    if len(data) > 0:
      return data[-1]  # returning last element instead of median
    else:
      raise statistics.StatisticsError