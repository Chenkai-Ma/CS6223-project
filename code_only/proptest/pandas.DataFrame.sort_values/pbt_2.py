from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

@given(st.data())
def test_output_row_count_property(data):
    df = data.draw(st.data_frames(columns=st.text(), rows=st.integers(min_value=1, max_value=1000)))
    by_column = df.columns[0] if not df.empty else []
    result = df.sort_values(by=by_column)
    assert result.shape[0] == df.shape[0]

@given(st.data())
def test_sorted_output_property(data):
    df = data.draw(st.data_frames(columns=st.text(), rows=st.integers(min_value=1, max_value=1000)))
    by_column = df.columns[0] if not df.empty else []
    result = df.sort_values(by=by_column)
    if not df.empty:
        assert all(result[by_column].iloc[i] <= result[by_column].iloc[i + 1] for i in range(len(result) - 1))

@given(st.data())
def test_inplace_modification_property(data):
    df = data.draw(st.data_frames(columns=st.text(), rows=st.integers(min_value=1, max_value=1000)))
    by_column = df.columns[0] if not df.empty else []
    original_id = id(df)
    df.sort_values(by=by_column, inplace=True)
    assert id(df) == original_id

@given(st.data())
def test_ignore_index_property(data):
    df = data.draw(st.data_frames(columns=st.text(), rows=st.integers(min_value=1, max_value=1000)))
    by_column = df.columns[0] if not df.empty else []
    result = df.sort_values(by=by_column, ignore_index=True)
    assert result.index.equals(pd.RangeIndex(start=0, stop=result.shape[0], step=1))

@given(st.data())
def test_empty_input_property(data):
    df = pd.DataFrame()
    result = df.sort_values(by=[])
    assert result.equals(df)
# End program