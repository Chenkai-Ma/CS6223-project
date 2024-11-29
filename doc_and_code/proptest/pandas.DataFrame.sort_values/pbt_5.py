from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

@given(st.data())
def test_output_row_count_property(data):
    df = data.draw(st.data_frames(columns=st.one_of(st.text(), st.integers()), 
                                   rows=st.integers(min_value=1, max_value=1000)))
    output_df = df.sort_values(by=df.columns[0], inplace=False)
    assert output_df.shape[0] == df.shape[0]

@given(st.data())
def test_sorted_output_property(data):
    df = data.draw(st.data_frames(columns=st.one_of(st.text(), st.integers()), 
                                   rows=st.integers(min_value=1, max_value=100)))
    sorted_col = df.columns[0]
    ascending_order = data.draw(st.booleans())
    output_df = df.sort_values(by=sorted_col, ascending=ascending_order)
    expected_order = df.sort_values(by=sorted_col, ascending=ascending_order).reset_index(drop=True)
    pd.testing.assert_frame_equal(output_df.reset_index(drop=True), expected_order)

@given(st.data())
def test_na_position_property(data):
    df = data.draw(st.data_frames(columns=st.one_of(st.text(), st.integers()), 
                                   rows=st.integers(min_value=1, max_value=100)))
    df = df.append(pd.Series([np.nan]), ignore_index=True)
    ascending_order = data.draw(st.booleans())
    output_first = df.sort_values(by=df.columns[0], ascending=ascending_order, na_position='first')
    output_last = df.sort_values(by=df.columns[0], ascending=ascending_order, na_position='last')
    
    if ascending_order:
        assert output_first.iloc[0][0] is np.nan
        assert output_last.iloc[-1][0] is np.nan
    else:
        assert output_first.iloc[-1][0] is np.nan
        assert output_last.iloc[0][0] is np.nan

@given(st.data())
def test_multiple_column_sorting_property(data):
    df = data.draw(st.data_frames(columns=st.lists(st.text(), min_size=2, max_size=5), 
                                   rows=st.integers(min_value=1, max_value=100)))
    output_df = df.sort_values(by=df.columns.tolist(), ascending=[True] * len(df.columns))
    
    for i in range(len(df.columns)):
        assert output_df[self.columns[i]].is_monotonic_increasing

@given(st.data())
def test_ignore_index_property(data):
    df = data.draw(st.data_frames(columns=st.lists(st.text(), min_size=1, max_size=5), 
                                   rows=st.integers(min_value=1, max_value=100)))
    output_df = df.sort_values(by=df.columns[0], ignore_index=True)
    assert output_df.index.equals(pd.RangeIndex(start=0, stop=output_df.shape[0], step=1))

# End program