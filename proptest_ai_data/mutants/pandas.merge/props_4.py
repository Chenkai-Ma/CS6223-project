import pandas as pd

def buggy_merge_1(df_left, df_right, on=None):
    result = pd.merge(df_left, df_right, on)
    result.iloc[0] = result.iloc[-1]
    return result

def buggy_merge_2(df_left, df_right, on=None):
    return pd.merge(df_left, df_right, on).drop_duplicates()

def buggy_merge_3(df_left, df_right, on=None):
    result = pd.merge(df_left, df_right, on)
    result['buggy'] = range(len(result))
    return result

def buggy_merge_4(df_left, df_right, on=None):
    result = pd.merge(df_left, df_right, on)
    result.iloc[:, 0] = result.iloc[:, 0].apply(lambda x: str(x) + "buggy")
    return result

def buggy_merge_5(df_left, df_right, on=None):
    result = pd.merge(df_left, df_right, on)
    result.iloc[:, -1] = result.iloc[:, -1].apply(lambda x: x + 100 if pd.api.types.is_numeric_dtype(x) else x)
    return result