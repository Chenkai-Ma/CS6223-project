from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

@given(st.data())
def test_output_row_count_property(data):
    df = data.draw(st.dataframes(
        columns=st.columns(['col1', 'col2', 'col3']),
        rows=st.lists(st.fixed_dictionaries({
            'col1': st.one_of(st.text(), st.none()),
            'col2': st.integers(),
            'col3': st.integers(),
        }), min_size=1, max_size=1000),
        index=st.lists(st.text(), min_size=1, max_size=1000)
    ))
    
    sorted_df = df.sort_values(by='col1', inplace=False)
    assert len(sorted_df) == len(df)

@given(st.data())
def test_sorted_by_columns_property(data):
    df = data.draw(st.dataframes(
        columns=st.columns(['col1', 'col2']),
        rows=st.lists(st.fixed_dictionaries({
            'col1': st.text(),
            'col2': st.integers(),
        }), min_size=1, max_size=1000),
        index=st.lists(st.text(), min_size=1, max_size=1000)
    ))

    sorted_df = df.sort_values(by='col1', ascending=True)
    assert sorted_df['col1'].is_monotonic_increasing

@given(st.data())
def test_na_position_first_last_property(data):
    df = data.draw(st.dataframes(
        columns=st.columns(['col1']),
        rows=st.lists(st.fixed_dictionaries({
            'col1': st.one_of(st.text(), st.none()),
        }), min_size=1, max_size=1000),
        index=st.lists(st.text(), min_size=1, max_size=1000)
    ))

    sorted_df_first = df.sort_values(by='col1', na_position='first')
    assert sorted_df_first['col1'].isnull().all() == sorted_df_first['col1'].iloc[:sorted_df_first['col1'].isnull().sum()].isnull().all()

    sorted_df_last = df.sort_values(by='col1', na_position='last')
    assert sorted_df_last['col1'].isnull().all() == sorted_df_last['col1'].iloc[-sorted_df_last['col1'].isnull().sum():].isnull().all()

@given(st.data())
def test_multiple_columns_sorting_property(data):
    df = data.draw(st.dataframes(
        columns=st.columns(['col1', 'col2']),
        rows=st.lists(st.fixed_dictionaries({
            'col1': st.text(),
            'col2': st.integers(),
        }), min_size=1, max_size=1000),
        index=st.lists(st.text(), min_size=1, max_size=1000)
    ))

    sorted_df = df.sort_values(by=['col1', 'col2'], ascending=[True, True])
    assert sorted_df['col1'].is_monotonic_increasing
    assert sorted_df.groupby('col1')['col2'].is_monotonic_increasing.all()

@given(st.data())
def test_ignore_index_property(data):
    df = data.draw(st.dataframes(
        columns=st.columns(['col1', 'col2']),
        rows=st.lists(st.fixed_dictionaries({
            'col1': st.text(),
            'col2': st.integers(),
        }), min_size=1, max_size=1000),
        index=st.lists(st.text(), min_size=1, max_size=1000)
    ))

    sorted_df = df.sort_values(by='col1', ignore_index=True)
    assert sorted_df.index.equals(pd.Index(range(len(sorted_df))))

# End program