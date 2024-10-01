import numpy as np

def buggy_1(x, ord=None, axis=None, keepdims=False):
  # Add a positive constant to the output to violate triangle inequality
  return np.linalg.norm(x, ord=ord, axis=axis, keepdims=keepdims) + 5

def buggy_2(x, ord=None, axis=None, keepdims=False):
  # Multiply the output with a positive factor greater than 1
  return 2 * np.linalg.norm(x, ord=ord, axis=axis, keepdims=keepdims)

def buggy_3(x, ord=None, axis=None, keepdims=False):
  # Substract a negative constant from the output to violate triangle inequality
  return np.linalg.norm(x, ord=ord, axis=axis, keepdims=keepdims) - (-5)

def buggy_4(x, ord=None, axis=None, keepdims=False):
  # Apply power of 2 to the output, valid only if norm was sqrt(sum(x^2))
  return np.linalg.norm(x, ord=ord, axis=axis, keepdims=keepdims)**2
   
def buggy_5(x, ord=None, axis=None, keepdims=False):
  # Return negative of the output
  return -np.linalg.norm(x, ord=ord, axis=axis, keepdims=keepdims)