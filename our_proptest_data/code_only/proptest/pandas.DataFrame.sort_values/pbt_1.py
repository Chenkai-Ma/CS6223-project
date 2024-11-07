from hypothesis import given, strategies as st
import pandas as pd

@given(st.data())
def test_output_rows_count_property(data):
    df = data.draw(st.data_frames(st.floats(), min_rows=0, max_rows=1000))
    by_column = data.draw(st.one_of(st.sampled_from(df.columns), st.just([])))
    ascending = data.draw(st.booleans())
    result = df.sort_values(by=by_column, ascending=ascending)
    
    assert result.shape[0] == df.shape[0]

@given(st.data())
def test_sorted_output_property(data):
    df = data.draw(st.data_frames(st.floats(), min_rows=1, max_rows=1000))
    by_column = data.draw(st.sampled_from(df.columns))
    ascending = data.draw(st.booleans())
    result = df.sort_values(by=by_column, ascending=ascending)
    
    assert result[by_column].is_monotonic_increasing == ascending

@given(st.data())
def test_inplace_modification_property(data):
    df = data.draw(st.data_frames(st.floats(), min_rows=1, max_rows=1000))
    original_df = df.copy()
    by_column = data.draw(st.sampled_from(df.columns))
    ascending = data.draw(st.booleans())
    df.sort_values(by=by_column, ascending=ascending, inplace=True)
    
    assert df.equals(original_df) is False

@given(st.data())
def test_ignore_index_property(data):
    df = data.draw(st.data_frames(st.floats(), min_rows=1, max_rows=1000))
    by_column = data.draw(st.sampled_from(df.columns))
    ascending = data.draw(st.booleans())
    result = df.sort_values(by=by_column, ascending=ascending, ignore_index=True)
    
    assert result.index.equals(pd.RangeIndex(start=0, stop=result.shape[0], step=1))

@given(st.data())
def test_empty_by_property(data):
    df = data.draw(st.data_frames(st.floats(), min_rows=0, max_rows=1000))
    result = df.sort_values(by=[], ascending=True)
    
    assert result.equals(df)

# End program