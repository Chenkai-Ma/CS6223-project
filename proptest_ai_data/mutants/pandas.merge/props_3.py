import pandas as pd
from pandas.testing import assert_frame_equal

def buggy_1(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, 
          sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
  df = pd.merge(left, right, how=how, on=on, left_on=left_on, right_on=right_on, left_index=left_index, 
                right_index=right_index, sort=sort, suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)
  df.columns = ['bug_'+str(i) for i in range(len(df.columns))]
  return df

def buggy_2(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, 
          sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
  df = pd.merge(left, right, how=how, on=on, left_on=left_on, right_on=right_on, left_index=left_index, 
                right_index=right_index, sort=sort, suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)
  df.columns = df.columns[::-1]
  return df
  
def buggy_3(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, 
          sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
  df = pd.merge(left, right, how=how, on=on, left_on=left_on, right_on=right_on, left_index=left_index, 
                right_index=right_index, sort=sort, suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)
  df.columns = df.columns.str.upper()
  return df

def buggy_4(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, 
          sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
  df = pd.merge(left, right, how=how, on=on, left_on=left_on, right_on=right_on, left_index=left_index, 
                right_index=right_index, sort=sort, suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)
  df.columns = df.columns + '_buggy'
  return df

def buggy_5(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, 
          sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
  df = pd.merge(left, right, how=how, on=on, left_on=left_on, right_on=right_on, left_index=left_index, 
                right_index=right_index, sort=sort, suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)
  df.columns = df.columns.str.replace('_x', '_buggy')
  return df