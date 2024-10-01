import statistics

def buggy_1(data):
  mean = statistics.mean(data)
  return mean + 1  # This will always increment the mean
  
def buggy_2(data):
  mean = statistics.mean(data)
  return mean - 1  # This will always decrement the mean

def buggy_3(data):
  mean = statistics.mean(data)
  return mean * 2  # This will always double the mean

def buggy_4(data):
  mean = statistics.mean(data)
  return mean / 2  # This will always halve the mean

def buggy_5(data):
  mean = statistics.mean(data)
  return mean if len(data) % 2 else mean + 1  # This will add 1 to the mean for all inputs of even length