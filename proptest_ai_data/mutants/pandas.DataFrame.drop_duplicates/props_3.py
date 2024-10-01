import pandas as pd

def buggy_1(df, subset=None, keep='first', inplace=False, ignore_index=False):
    df = df.drop_duplicates(subset, keep, inplace, ignore_index)
    return df[df.duplicated()]

def buggy_2(df, subset=None, keep='first', inplace=False, ignore_index=False):
    result = df.drop_duplicates(subset, keep, inplace, ignore_index)
    if subset:
        # choose a column that is not in subset and drop its duplicates
        for column in df.columns:
            if column not in subset:
                return result.drop_duplicates(column)
    return result

def buggy_3(df, subset=None, keep='first', inplace=False, ignore_index=False):
    df = df.drop_duplicates(subset, keep, inplace, ignore_index)
    # shuffle the rows
    return df.sample(frac=1)

def buggy_4(df, subset=None, keep='first', inplace=False, ignore_index=False):
    # Instead of dropping based on subset, it drops the duplicates based all columns.
    return df.drop_duplicates(df.columns, keep, inplace, ignore_index)

def buggy_5(df, subset=None, keep='first', inplace=False, ignore_index=False):
    result = df.drop_duplicates(subset, keep, inplace, ignore_index)
    # repeats the last row
    return pd.concat([result, result.tail(1)], ignore_index=True)