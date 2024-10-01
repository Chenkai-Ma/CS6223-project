import statistics

def buggy_1(data):
  ans = statistics.median(data)
  return ans + 1  # Always returns a value greater than the maximum.

def buggy_2(data):
  ans = statistics.median(data)
  return ans - 1  # Always returns a value smaller than the minimum.

def buggy_3(data):
  ans = statistics.median(data)
  if len(data) % 2:  # If number of data points is odd.
    return ans + 1
  else:
    return ans - 1

def buggy_4(data):
  ans = statistics.median(data)
  if ans in data:  # If median is an actual data point.
    return ans + 1
  else:
    return ans - 1

def buggy_5(data):
  ans = statistics.median(data)
  return ans * 2  # Always returns a value larger or smaller than the range.