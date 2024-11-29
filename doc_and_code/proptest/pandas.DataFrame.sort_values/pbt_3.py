from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

@given(st.data())
def test_output_rows_property(data):
    df = data.draw(st.dataframes(columns=[
        st.column('col1', element=st.one_of(st.text(), st.none())),
        st.column('col2', element=st.integers()),
        st.column('col3', element=st.integers())
    ], rows=st.lists(st.one_of(st.tuples(st.text(), st.integers(), st.integers())), min_size=1, max_size=1000)))
    
    result = df.sort_values(by='col1', inplace=False)
    
    assert result.shape[0] == df.shape[0]

@given(st.data())
def test_sorted_columns_property(data):
    df = data.draw(st.dataframes(columns=[
        st.column('col1', element=st.one_of(st.text(), st.none())),
        st.column('col2', element=st.integers()),
        st.column('col3', element=st.integers())
    ], rows=st.lists(st.one_of(st.tuples(st.text(), st.integers(), st.integers())), min_size=1, max_size=1000)))
    
    result = df.sort_values(by='col1', ascending=True, inplace=False)
    assert (result['col1'].is_monotonic_increasing or result['col1'].is_monotonic_decreasing)

@given(st.data())
def test_na_position_property(data):
    df = data.draw(st.dataframes(columns=[
        st.column('col1', element=st.one_of(st.text(), st.none())),
        st.column('col2', element=st.integers())
    ], rows=st.lists(st.one_of(st.tuples(st.text(), st.integers())), min_size=1, max_size=1000)))
    
    result_first = df.sort_values(by='col1', na_position='first', inplace=False)
    result_last = df.sort_values(by='col1', na_position='last', inplace=False)
    
    assert result_first['col1'].isna().argmax() < result_last['col1'].isna().argmax()

@given(st.data())
def test_multiple_columns_sorting_property(data):
    df = data.draw(st.dataframes(columns=[
        st.column('col1', element=st.one_of(st.text(), st.none())),
        st.column('col2', element=st.integers()),
        st.column('col3', element=st.integers())
    ], rows=st.lists(st.one_of(st.tuples(st.text(), st.integers(), st.integers())), min_size=1, max_size=1000)))
    
    result = df.sort_values(by=['col1', 'col2'], ascending=[True, False], inplace=False)
    
    sorted_col1 = result['col1'].is_monotonic_increasing
    sorted_col2 = result['col2'].is_monotonic_decreasing
    assert sorted_col1 and sorted_col2

@given(st.data())
def test_ignore_index_property(data):
    df = data.draw(st.dataframes(columns=[
        st.column('col1', element=st.one_of(st.text(), st.none())),
        st.column('col2', element=st.integers())
    ], rows=st.lists(st.one_of(st.tuples(st.text(), st.integers())), min_size=1, max_size=1000)))
    
    result = df.sort_values(by='col1', ignore_index=True, inplace=False)
    
    assert result.index.equals(pd.RangeIndex(start=0, stop=result.shape[0], step=1))

# End program