import pandas as pd
import numpy as np

def buggy_1(df, by, *, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None):
    df_sorted = df.sort_values(by, axis=axis, ascending=ascending, inplace=inplace, kind=kind, na_position=na_position, ignore_index=ignore_index, key=key)
    if inplace:
        return
    if na_position == 'first':
        df_sorted = df_sorted.loc[df_sorted[by].notna(), :]
        df_sorted = pd.concat([df_sorted[df_sorted[by].isna()], df_sorted], ignore_index=ignore_index)
    else:
        df_sorted = df_sorted.loc[df_sorted[by].isna(), :]
        df_sorted = pd.concat([df_sorted, df_sorted[df_sorted[by].notna()]], ignore_index=ignore_index)
    return df_sorted
       
def buggy_2(df, by, *, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None):
    df_sorted = df.sort_values(by, axis=axis, ascending=ascending, inplace=inplace, kind=kind, na_position=na_position, ignore_index=ignore_index, key=key)
    if inplace:
        return
    df_sorted.loc[df_sorted[by].isna(), by] = 'Z' if df[by].dtype == 'object' else np.inf
    return df_sorted

def buggy_3(df, by, *, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None):
    df_sorted = df.sort_values(by, axis=axis, ascending=ascending, inplace=inplace, kind=kind, na_position='last', ignore_index=ignore_index, key=key)
    if inplace:
        return 
    return df_sorted

def buggy_4(df, by, *, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None):
    df_sorted = df.sort_values(by, axis=axis, ascending=ascending, inplace=inplace, kind=kind, na_position='first', ignore_index=ignore_index, key=key)
    if inplace:
        return 
    return df_sorted

def buggy_5(df, by, *, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None):
    df_sorted = df.sort_values(by, axis=axis, ascending=not ascending, inplace=inplace, kind=kind, na_position=na_position, ignore_index=ignore_index, key=key)
    if inplace:
        return 
    return df_sorted