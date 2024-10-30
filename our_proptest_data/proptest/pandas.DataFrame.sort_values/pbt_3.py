from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

@given(st.data())
def test_sorted_order_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                          st.column('col2', elements=st.integers())],
                                 rows=st.lists(st.tuples(), min_size=1, max_size=1000),
                                 index=False))
    sorted_df = df.sort_values(by='col2')
    assert sorted_df['col2'].is_monotonic_increasing

@given(st.data())
def test_nan_position_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                          st.column('col2', elements=st.integers())],
                                 rows=st.lists(st.tuples(), min_size=1, max_size=1000),
                                 index=False))
    sorted_with_nan_last = df.sort_values(by='col2', na_position='last')
    assert not sorted_with_nan_last['col2'].isnull().any() or sorted_with_nan_last['col2'].isnull().all()

@given(st.data())
def test_inplace_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                          st.column('col2', elements=st.integers())],
                                 rows=st.lists(st.tuples(), min_size=1, max_size=1000),
                                 index=False))
    original_df = df.copy()
    df.sort_values(by='col2', inplace=True)
    assert df.equals(original_df) is False

@given(st.data())
def test_column_types_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                          st.column('col2', elements=st.integers()),
                                          st.column('col3', elements=st.floats())],
                                 rows=st.lists(st.tuples(), min_size=1, max_size=1000),
                                 index=False))
    sorted_df = df.sort_values(by='col2')
    assert sorted_df.dtypes.equals(df.dtypes)

@given(st.data())
def test_multi_column_sort_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.text()),
                                          st.column('col2', elements=st.integers())],
                                 rows=st.lists(st.tuples(), min_size=1, max_size=1000),
                                 index=False))
    sorted_df = df.sort_values(by=['col1', 'col2'])
    assert all(sorted_df['col1'].iloc[i] <= sorted_df['col1'].iloc[i + 1] for i in range(len(sorted_df) - 1))
# End program