import statistics

# Buggy version 1: Always increment the result by 1  
def buggy_1(data):
  return statistics.mean(data) + 1

# Buggy version 2: Always decrement the result by 1
def buggy_2(data):
  return statistics.mean(data) - 1
  
# Buggy version 3: Always return 0
def buggy_3(data):
  return 0

# Buggy version 4: Return the first element of the list
def buggy_4(data):
  return data[0] if data else 0

# Buggy version 5: Return the result divided by 2
def buggy_5(data):
  return statistics.mean(data) / 2