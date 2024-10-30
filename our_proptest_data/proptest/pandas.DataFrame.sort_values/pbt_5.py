from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

@given(st.data())
def test_sorted_order_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.nothing())), 
                                           st.column('col2', elements=st.integers())]))
    sorted_df = df.sort_values(by='col1')
    assert sorted_df['col1'].is_monotonic_increasing

@given(st.data())
def test_na_position_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.nothing())), 
                                           st.column('col2', elements=st.integers())]))
    sorted_df_last = df.sort_values(by='col1', na_position='last')
    sorted_df_first = df.sort_values(by='col1', na_position='first')
    assert sorted_df_last['col1'].isnull().sum() == df['col1'].isnull().sum()
    assert sorted_df_first['col1'].isnull().sum() == df['col1'].isnull().sum()

@given(st.data())
def test_inplace_modification_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.nothing())), 
                                           st.column('col2', elements=st.integers())]))
    original_df = df.copy()
    df.sort_values(by='col1', inplace=True)
    assert df.equals(original_df) == False  # Original DataFrame should be modified

@given(st.data())
def test_column_retention_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.nothing())), 
                                           st.column('col2', elements=st.integers())]))
    sorted_df = df.sort_values(by='col1')
    assert set(sorted_df.columns) == set(df.columns)  # All original columns should be retained

@given(st.data())
def test_multiple_columns_sort_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.text()), 
                                           st.column('col2', elements=st.integers()), 
                                           st.column('col3', elements=st.integers())]))
    sorted_df = df.sort_values(by=['col1', 'col2'])
    assert sorted_df['col1'].is_monotonic_increasing  # Check primary sort order
    assert all(sorted_df['col1'].iloc[i] <= sorted_df['col1'].iloc[i+1] for i in range(len(sorted_df)-1))  # Secondary sort order check

# End program