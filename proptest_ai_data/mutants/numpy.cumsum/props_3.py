def buggy_1(a, axis=None, dtype=None, out=None):
  # Adding a constant to numpy.cumsum's result, causing shifting in array size
  result = np.cumsum(a, axis, dtype, out)
  return np.append(result, 5)

def buggy_2(a, axis=None, dtype=None, out=None):
  # Appending returned list to itself, causing doubling in array size
  result = np.cumsum(a, axis, dtype, out)
  return np.append(result, result)

def buggy_3(a, axis=None, dtype=None, out=None):
  # Dropping the last element from numpy.cumsum's result, causing reduction in array size
  result = np.cumsum(a, axis, dtype, out)
  return result[:-1]

def buggy_4(a, axis=None, dtype=None, out=None):
  # Replacing array with all zeroes
  result = np.cumsum(a, axis, dtype, out)
  return np.zeros_like(result)

def buggy_5(a, axis=None, dtype=None, out=None):
  # Removing an element from the starting of the array causing reduction in array size.
  result = np.cumsum(a, axis, dtype, out)
  return result[1:]