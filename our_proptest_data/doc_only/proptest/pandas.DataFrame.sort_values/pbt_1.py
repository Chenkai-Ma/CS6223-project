from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

@given(st.data())
def test_sorting_order_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                          st.column('col2', elements=st.integers())],
                                 rows=st.lists(st.record({'col1': st.one_of(st.text(), st.none()),
                                                           'col2': st.integers()}), min_size=1, max_size=100)))
    sorted_df = df.sort_values(by='col2')
    assert sorted_df['col2'].is_monotonic_increasing

@given(st.data())
def test_na_position_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                          st.column('col2', elements=st.integers())],
                                 rows=st.lists(st.record({'col1': st.one_of(st.text(), st.none()),
                                                           'col2': st.integers()}), min_size=1, max_size=100)))
    na_position = data.draw(st.one_of(st.just('first'), st.just('last')))
    sorted_df = df.sort_values(by='col1', na_position=na_position)
    
    if na_position == 'first':
        assert sorted_df['col1'].isna().all() or sorted_df['col1'].first_valid_index() != 0
    else:
        assert sorted_df['col1'].isna().all() or sorted_df['col1'].last_valid_index() != len(sorted_df) - 1

@given(st.data())
def test_inplace_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                          st.column('col2', elements=st.integers())],
                                 rows=st.lists(st.record({'col1': st.one_of(st.text(), st.none()),
                                                           'col2': st.integers()}), min_size=1, max_size=100)))

    original_df = df.copy()
    df.sort_values(by='col2', inplace=True)
    assert df is original_df  # In-place modification should not return a new DataFrame
    assert df.equals(original_df.sort_values(by='col2'))  # Should match the sorted version

@given(st.data())
def test_column_retention_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                          st.column('col2', elements=st.integers())],
                                 rows=st.lists(st.record({'col1': st.one_of(st.text(), st.none()),
                                                           'col2': st.integers()}), min_size=1, max_size=100)))
    sorted_df = df.sort_values(by='col1')
    assert all(col in sorted_df.columns for col in df.columns)

@given(st.data())
def test_multiple_column_sorting_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.none())),
                                          st.column('col2', elements=st.integers()),
                                          st.column('col3', elements=st.text())],
                                 rows=st.lists(st.record({'col1': st.one_of(st.text(), st.none()),
                                                           'col2': st.integers(),
                                                           'col3': st.text()}), min_size=1, max_size=100)))
    sorted_df = df.sort_values(by=['col1', 'col2'])
    assert sorted_df['col1'].is_monotonic_increasing or sorted_df['col1'].isna().all()
    for group in sorted_df.groupby('col1'):
        assert group[1]['col2'].is_monotonic_increasing

# End program