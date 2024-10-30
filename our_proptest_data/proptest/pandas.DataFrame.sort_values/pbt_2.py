from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

# Property 1: Test sorted output based on specified columns
@given(st.data())
def test_sort_values_sorted_order_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                           st.column('col2', elements=st.integers())],
                                 index=st.integers(min_value=1, max_value=100)))
    sorted_df = df.sort_values(by='col2')
    assert sorted_df['col2'].is_monotonic

# Property 2: Test NaN positioning based on na_position parameter
@given(st.data())
def test_sort_values_nan_position_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                           st.column('col2', elements=st.integers())],
                                 index=st.integers(min_value=1, max_value=100)))
    na_position_first_df = df.sort_values(by='col1', na_position='first')
    na_position_last_df = df.sort_values(by='col1', na_position='last')
    
    assert na_position_first_df['col1'].isnull().all() == (na_position_first_df['col1'].iloc[0] is None)
    assert na_position_last_df['col1'].isnull().all() == (na_position_last_df['col1'].iloc[-1] is None)

# Property 3: Test inplace behavior
@given(st.data())
def test_sort_values_inplace_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                           st.column('col2', elements=st.integers())],
                                 index=st.integers(min_value=1, max_value=100)))
    original_df = df.copy()
    
    df.sort_values(by='col2', inplace=True)
    assert df.equals(df.sort_values(by='col2'))  # Verifying sorting worked
    assert not original_df.equals(df)  # Original should not be equal

    df = original_df  # Reset
    sorted_df = df.sort_values(by='col2', inplace=False)
    assert not original_df.equals(sorted_df)  # New DataFrame should differ

# Property 4: Test output retains original columns and types
@given(st.data())
def test_sort_values_retain_columns_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                           st.column('col2', elements=st.floats()),
                                           st.column('col3', elements=st.dates())],
                                 index=st.integers(min_value=1, max_value=100)))
    sorted_df = df.sort_values(by='col2')
    
    assert set(sorted_df.columns) == set(df.columns)
    assert all(sorted_df[col].dtype == df[col].dtype for col in df.columns)

# Property 5: Test hierarchical sorting by multiple columns
@given(st.data())
def test_sort_values_hierarchical_sort_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.text()),
                                           st.column('col2', elements=st.integers()),
                                           st.column('col3', elements=st.integers())],
                                 index=st.integers(min_value=1, max_value=100)))
    sorted_df = df.sort_values(by=['col1', 'col2'])
    
    assert all(sorted_df['col1'].iloc[i] <= sorted_df['col1'].iloc[i + 1] for i in range(len(sorted_df) - 1))
    assert all(sorted_df.loc[sorted_df['col1'] == sorted_df['col1'].iloc[i], 'col2'].iloc[j] <= sorted_df.loc[sorted_df['col1'] == sorted_df['col1'].iloc[i], 'col2'].iloc[j + 1] 
           for i in range(len(sorted_df) - 1) for j in range(len(sorted_df.loc[sorted_df['col1'] == sorted_df['col1'].iloc[i]]) - 1))

# End program