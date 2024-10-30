from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

@given(st.data())
def test_sorted_order_property(data):
    df = data.draw(st.dataframes(columns=[
        st.column('col1', st.one_of(st.text(), st.none())),
        st.column('col2', st.integers(min_value=0, max_value=100)),
    ], rows=st.lists(st.fixed_dictionaries({
        'col1': st.one_of(st.text(), st.none()),
        'col2': st.integers(min_value=0, max_value=100),
    }))))
    
    sorted_df = df.sort_values(by='col1')
    assert sorted_df['col1'].is_monotonic_increasing

@given(st.data())
def test_na_position_property(data):
    df = data.draw(st.dataframes(columns=[
        st.column('col1', st.one_of(st.text(), st.none())),
        st.column('col2', st.integers(min_value=0, max_value=100)),
    ], rows=st.lists(st.fixed_dictionaries({
        'col1': st.one_of(st.text(), st.none()),
        'col2': st.integers(min_value=0, max_value=100),
    }))))
    
    sorted_df_last = df.sort_values(by='col1', na_position='last')
    assert sorted_df_last['col1'].isna().sum() == df['col1'].isna().sum()
    assert sorted_df_last['col1'].iloc[-1] is np.nan

@given(st.data())
def test_inplace_property(data):
    df = data.draw(st.dataframes(columns=[
        st.column('col1', st.one_of(st.text(), st.none())),
        st.column('col2', st.integers(min_value=0, max_value=100)),
    ], rows=st.lists(st.fixed_dictionaries({
        'col1': st.one_of(st.text(), st.none()),
        'col2': st.integers(min_value=0, max_value=100),
    }))))
    
    original_df = df.copy()
    df.sort_values(by='col1', inplace=True)
    assert df.equals(df.sort_values(by='col1', inplace=False))
    assert not original_df.equals(df)

@given(st.data())
def test_column_retention_property(data):
    df = data.draw(st.dataframes(columns=[
        st.column('col1', st.one_of(st.text(), st.none())),
        st.column('col2', st.integers(min_value=0, max_value=100)),
    ], rows=st.lists(st.fixed_dictionaries({
        'col1': st.one_of(st.text(), st.none()),
        'col2': st.integers(min_value=0, max_value=100),
    }))))
    
    sorted_df = df.sort_values(by='col1')
    assert set(df.columns) == set(sorted_df.columns)

@given(st.data())
def test_multiple_column_sort_property(data):
    df = data.draw(st.dataframes(columns=[
        st.column('col1', st.one_of(st.text(), st.none())),
        st.column('col2', st.integers(min_value=0, max_value=100)),
        st.column('col3', st.integers(min_value=0, max_value=100)),
    ], rows=st.lists(st.fixed_dictionaries({
        'col1': st.one_of(st.text(), st.none()),
        'col2': st.integers(min_value=0, max_value=100),
        'col3': st.integers(min_value=0, max_value=100),
    }))))
    
    sorted_df = df.sort_values(by=['col1', 'col2'])
    assert all(sorted_df['col1'].is_monotonic_increasing)
    assert all(sorted_df.groupby('col1')['col2'].is_monotonic_increasing)

# End program