from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

@given(st.data())
def test_output_row_count_property(data):
    df = data.draw(st.data_frames(columns=st.one_of(st.text(), st.integers()), rows=st.integers(min_value=1, max_value=1000)))
    result_df = df.sort_values(by=df.columns[0], inplace=False)
    assert len(result_df) == len(df)

@given(st.data())
def test_sorting_order_property(data):
    df = data.draw(st.data_frames(columns=st.lists(st.text()), rows=st.integers(min_value=1, max_value=100)))
    ascending = data.draw(st.booleans())
    result_df = df.sort_values(by=df.columns[0], ascending=ascending, inplace=False)
    assert result_df[df.columns[0]].is_sorted(ascending=ascending)

@given(st.data())
def test_na_position_property(data):
    df = data.draw(st.data_frames(columns=[st.text()], rows=st.integers(min_value=1, max_value=100)))
    df.loc[2] = [np.nan]  # Introduce a NaN value
    result_df_first = df.sort_values(by=df.columns[0], na_position='first', inplace=False)
    result_df_last = df.sort_values(by=df.columns[0], na_position='last', inplace=False)
    assert result_df_first[df.columns[0]].isna().all()  # Check if NaN is at the start
    assert result_df_last[df.columns[0]].isna().all()  # Check if NaN is at the end

@given(st.data())
def test_multiple_columns_sorting_property(data):
    df = data.draw(st.data_frames(columns=st.lists(st.text(), min_size=2, max_size=3), rows=st.integers(min_value=1, max_value=100)))
    ascending = data.draw(st.lists(st.booleans(), min_size=len(df.columns), max_size=len(df.columns)))
    result_df = df.sort_values(by=df.columns, ascending=ascending, inplace=False)
    assert all(result_df[df.columns[i]].is_sorted(ascending=ascending[i]) for i in range(len(df.columns)))

@given(st.data())
def test_ignore_index_property(data):
    df = data.draw(st.data_frames(columns=st.lists(st.text(), min_size=1, max_size=3), rows=st.integers(min_value=1, max_value=100)))
    result_df = df.sort_values(by=df.columns[0], ignore_index=True, inplace=False)
    assert result_df.index.equals(pd.RangeIndex(start=0, stop=len(result_df), step=1))

# End program