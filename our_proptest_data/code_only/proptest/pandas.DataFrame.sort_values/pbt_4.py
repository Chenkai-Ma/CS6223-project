from hypothesis import given, strategies as st
import pandas as pd

@given(st.data())
def test_output_row_count_property(data):
    df = data.draw(st.data_frames(columns=st.one_of(st.text(), st.integers()), rows=st.integers(min_value=0, max_value=1000)))
    sorted_df = df.sort_values(by=df.columns[0], ascending=True)
    assert len(sorted_df) == len(df)

@given(st.data())
def test_output_sort_order_property(data):
    df = data.draw(st.data_frames(columns=st.one_of(st.text(), st.integers()), rows=st.integers(min_value=0, max_value=1000)))
    sorted_df = df.sort_values(by=df.columns[0], ascending=True)
    assert sorted_df[df.columns[0]].is_monotonic_increasing

@given(st.data())
def test_inplace_modification_property(data):
    df = data.draw(st.data_frames(columns=st.one_of(st.text(), st.integers()), rows=st.integers(min_value=0, max_value=1000)))
    original_df = df.copy()
    df.sort_values(by=df.columns[0], ascending=True, inplace=True)
    assert df.equals(original_df) is False  # Check that the DataFrame has been modified

@given(st.data())
def test_ignore_index_property(data):
    df = data.draw(st.data_frames(columns=st.one_of(st.text(), st.integers()), rows=st.integers(min_value=0, max_value=1000)))
    sorted_df = df.sort_values(by=df.columns[0], ascending=True, ignore_index=True)
    assert sorted_df.index.equals(pd.RangeIndex(start=0, stop=len(sorted_df), step=1))

@given(st.data())
def test_empty_by_parameter_property(data):
    df = data.draw(st.data_frames(columns=st.one_of(st.text(), st.integers()), rows=st.integers(min_value=0, max_value=1000)))
    sorted_df = df.sort_values(by=[], ascending=True)
    assert sorted_df.equals(df)
# End program