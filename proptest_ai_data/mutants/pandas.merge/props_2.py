import pandas as pd
import numpy as np

def buggy_1(left, right, how='inner', on=None, left_on=None, right_on=None,
            left_index=False, right_index=False, sort=False,
            suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
    res = pd.merge(left, right, how=how, on=on, left_on=left_on, right_on=right_on,
                   left_index=left_index, right_index=right_index, sort=sort,
                   suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)
    # add a row not in both frames
    res = res.append(left.iloc[0], ignore_index=True)
    return res

def buggy_2(left, right, how='inner', on=None, left_on=None, right_on=None,
            left_index=False, right_index=False, sort=False,
            suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
    res = pd.merge(left, right, how=how, on=on, left_on=left_on, right_on=right_on,
                   left_index=left_index, right_index=right_index, sort=sort,
                   suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)
    # remove a row from the result
    res = res.drop(res.index[0])
    return res

def buggy_3(left, right, how='inner', on=None, left_on=None, right_on=None,
            left_index=False, right_index=False, sort=False,
            suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
    res = pd.merge(left, right, how=how, on=on, left_on=left_on, right_on=right_on,
                   left_index=left_index, right_index=right_index, sort=sort,
                   suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)
    # add some noise to the data
    res.iloc[0] = np.nan
    return res

def buggy_4(left, right, how='inner', on=None, left_on=None, right_on=None,
            left_index=False, right_index=False, sort=False,
            suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
    res = pd.merge(left, right, how=how, on=on, left_on=left_on, right_on=right_on,
                   left_index=left_index, right_index=right_index, sort=sort,
                   suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)
    # change the labels in a column
    res.iloc[:, 0]= 'new_label'
    return res

def buggy_5(left, right, how='inner', on=None, left_on=None, right_on=None,
            left_index=False, right_index=False, sort=False,
            suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
    res = pd.merge(left, right, how=how, on=on, left_on=left_on, right_on=right_on,
                   left_index=left_index, right_index=right_index, sort=sort,
                   suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)
    # swap the data in two columns
    res[res.columns[:2]] = res[res.columns[:2]].copy()[::-1]
    return res