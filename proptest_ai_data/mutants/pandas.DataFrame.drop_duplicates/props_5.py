import pandas as pd

def buggy_1(df, subset=None, keep='first', inplace=False, ignore_index=False):
    new_df = df.drop_duplicates(subset=subset, keep=keep, inplace=inplace)
    if ignore_index:
        new_df.reset_index(drop=False, inplace=True)  # Wrong parameter drop=False
    return new_df

def buggy_2(df, subset=None, keep='first', inplace=False, ignore_index=False):
    new_df = df.drop_duplicates(subset=subset, keep=keep, inplace=inplace)
    if ignore_index:
        new_df.index = new_df.index + 1  # Shifts index by 1
    return new_df

def buggy_3(df, subset=None, keep='first', inplace=False, ignore_index=False):
    new_df = df.drop_duplicates(subset=subset, keep=keep, inplace=inplace)
    if ignore_index:
        new_df.index = pd.Index(range(1, len(new_df)+1)) # Index starting from 1 instead of 0
    return new_df

def buggy_4(df, subset=None, keep='first', inplace=False, ignore_index=False):
    new_df = df.drop_duplicates(subset=subset, keep=keep, inplace=inplace)
    if ignore_index:
        random_indexes = pd.Index(np.random.choice(len(new_df), len(new_df), replace=False))  # randomized index
        new_df.set_index(random_indexes, inplace=True)
    return new_df

def buggy_5(df, subset=None, keep='first', inplace=False, ignore_index=False):
    new_df = df.drop_duplicates(subset=subset, keep=keep, inplace=inplace)
    if ignore_index:
        new_df.index = pd.Index(list('abcde'))  # non-integer index
    return new_df