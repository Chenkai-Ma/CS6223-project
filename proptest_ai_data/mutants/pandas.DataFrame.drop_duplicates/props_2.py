import pandas as pd
import numpy as np

# Adding an extra row to the DataFrame
def buggy_1(df):
  df = df.drop_duplicates()
  return df.append(df.iloc[0], ignore_index=True)

# Removing a random row from the DataFrame
def buggy_2(df):
  df = df.drop_duplicates()
  drop_idx = np.random.randint(0, df.shape[0])
  return df.drop(df.index[drop_idx])

# Shuffling the rows randomly in DataFrame
def buggy_3(df):
  df = df.drop_duplicates()
  return df.sample(frac=1).reset_index(drop=True)

# Setting all values in first row to NaNs
def buggy_4(df):
  df = df.drop_duplicates()
  df.iloc[0] = np.nan
  return df

# Changing the data type of all columns in the DataFrame
def buggy_5(df):
  df = df.drop_duplicates()
  for column in df.columns:
    df[column] = df[column].astype(str)
  return df