import pandas as pd
import numpy as np

def buggy_1(obj):
  if isinstance(obj, (list, np.ndarray, pd.Series, pd.DataFrame)):
    return [not item for item in pd.isna(obj)]
  else:
    return not pd.isna(obj)

def buggy_2(obj):
  result = pd.isna(obj)
  return not result if type(result) == bool else np.logical_not(result)

def buggy_3(obj):
  return np.logical_and(pd.isna(obj), True)

def buggy_4(obj):
  return np.logical_xor(pd.isna(obj), pd.isna(obj))

def buggy_5(obj):
  result = pd.isna(obj)
  if isinstance(result, pd.DataFrame):
    return result.replace({False: True, True: False})
  elif isinstance(result, pd.Series):
    return result.map({False: True, True: False})
  return not result