import pandas as pd
import numpy as np

def buggy_1(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True):
    result, bins = pd.cut(x, bins, right=right, labels=labels, retbins=True, precision=precision, include_lowest=include_lowest, duplicates=duplicates, ordered=ordered)
    if right:
        result = result.where(result != result.categories[-1], np.nan)
    return result, bins if retbins else result

def buggy_2(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True):
    result, bins = pd.cut(x, bins, right=right, labels=labels, retbins=True, precision=precision, include_lowest=include_lowest, duplicates=duplicates, ordered=ordered)
    if not right:
       result = result.where(result != result.categories[0], np.nan)
    return result, bins if retbins else result

def buggy_3(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True):
    result, bins = pd.cut(x, bins, right=right, labels=labels, retbins=True, precision=precision, include_lowest=include_lowest, duplicates=duplicates, ordered=ordered)
    bins[-1] = bins[-1] - 1 if right else bins[-1] + 1
    return result, bins if retbins else result

def buggy_4(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True):
    result, bins = pd.cut(x, bins, right=right, labels=labels, retbins=True, precision=precision, include_lowest=include_lowest, duplicates=duplicates, ordered=ordered)
    return result, np.array(list(bins[:-1]) + [bins[-2]]) if retbins else result

def buggy_5(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True):
    result, bins = pd.cut(x, bins-1, right=right, labels=labels, retbins=True, precision=precision, include_lowest=include_lowest, duplicates=duplicates, ordered=ordered)
    return result, np.concatenate((bins, [bins.max() + 1])) if retbins else result