import pandas as pd
import numpy as np

def buggy_1(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True):
    result = pd.cut(x, bins, right, labels, retbins, precision, include_lowest, duplicates, ordered)
    if labels is None:
        return 10 * result
    elif labels is False:
        return result.astype(float)
    else:
        return result.astype(int)


def buggy_2(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True):
    result = pd.cut(x, bins, right, labels, retbins, precision, include_lowest, duplicates, ordered)
    if type(result) is pd.Categorical:
        return result.astype(str)
    elif type(result) is pd.Series:
        return result.astype('category')
    else:
        return result.astype('object')


def buggy_3(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True):
    result = pd.cut(x, bins, right, labels, retbins, precision, include_lowest, duplicates, ordered)
    if labels is None:
        result.categories = ['label_{}'.format(i) for i in range(len(result.categories))]
    return result


def buggy_4(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True):
    result = pd.cut(x, bins, right, labels, retbins, precision, include_lowest, duplicates, ordered)
    if labels is not None:
        result = result.cat.remove_unused_categories()
    return result


def buggy_5(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True):
    result = pd.cut(x, bins, right, labels, retbins, precision, include_lowest, duplicates, ordered)
    if labels is False:
        return result.values.categories.codes
    else:
        return result