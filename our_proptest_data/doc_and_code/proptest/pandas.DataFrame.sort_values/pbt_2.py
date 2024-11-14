from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

@given(st.data())
def test_output_rows_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.nothing())),
                                          st.column('col2', elements=st.integers())],
                                  index=st.range_indexes(min_size=1, max_size=1000)))
    sorted_df = df.sort_values(by='col1', inplace=False)
    assert len(sorted_df) == len(df)

@given(st.data())
def test_sorted_output_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.nothing())),
                                          st.column('col2', elements=st.integers())],
                                  index=st.range_indexes(min_size=1, max_size=1000)))
    sorted_df = df.sort_values(by='col2', ascending=True, inplace=False)
    assert sorted_df['col2'].is_monotonic_increasing

@given(st.data())
def test_na_position_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.nothing())),
                                          st.column('col2', elements=st.integers())],
                                  index=st.range_indexes(min_size=1, max_size=1000)))
    sorted_df_first = df.sort_values(by='col1', na_position='first', inplace=False)
    sorted_df_last = df.sort_values(by='col1', na_position='last', inplace=False)
    assert sorted_df_first['col1'].isna().all() or not sorted_df_first['col1'].isna().any()
    assert sorted_df_last['col1'].isna().any() or not sorted_df_last['col1'].isna().all()

@given(st.data())
def test_multi_column_sort_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.nothing())),
                                          st.column('col2', elements=st.integers()),
                                          st.column('col3', elements=st.integers())],
                                  index=st.range_indexes(min_size=1, max_size=1000)))
    sorted_df = df.sort_values(by=['col1', 'col2'], ascending=[True, False], inplace=False)
    assert sorted_df['col1'].is_monotonic_increasing
    assert sorted_df['col2'].is_monotonic_decreasing

@given(st.data())
def test_ignore_index_property(data):
    df = data.draw(st.dataframes(columns=[st.column('col1', elements=st.one_of(st.text(), st.nothing())),
                                          st.column('col2', elements=st.integers())],
                                  index=st.range_indexes(min_size=1, max_size=1000)))
    sorted_df = df.sort_values(by='col1', ignore_index=True, inplace=False)
    assert sorted_df.index.equals(pd.Index(range(len(sorted_df))))
# End program