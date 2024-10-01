import pandas as pd
import numpy as np

def buggy_1(obj):
    result = pd.isna(obj)
    if type(result) is pd.core.frame.DataFrame:
        return result.values
    elif type(result) is pd.core.series.Series:
        return result.tolist()
    else:
        return result.astype(float)

def buggy_2(obj):
    result = pd.isna(obj)
    if type(result) is pd.core.frame.DataFrame:
        return result.T
    else:
        return result

def buggy_3(obj):
    result = pd.isna(obj)
    if type(result) is pd.core.frame.DataFrame:
        return result.columns
    elif type(result) is pd.core.series.Series:
        return result.empty
    else:
        return result

def buggy_4(obj):
    result = pd.isna(obj)
    if isinstance(obj, pd.DataFrame) or isinstance(obj, pd.Series) or isinstance(obj, pd.Index):
        result = result.sum()
    return result

def buggy_5(obj):
    result = pd.isna(obj)
    if type(result) is pd.core.frame.DataFrame:
        return result.dropna()
    elif type(result) is pd.core.series.Series:
        return result.dropna()
    else:
        return result

array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
df = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])

print(buggy_1(df))
print(buggy_2(df))
print(buggy_3(df))
print(buggy_4(df))
print(buggy_5(df))