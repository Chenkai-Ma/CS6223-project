from hypothesis import given, strategies as st
import pandas as pd
import numpy as np

@given(st.data())
def test_output_has_same_number_of_rows_property(data):
    df = data.draw(st.dataframes(
        index=st.range_indexes(),
        columns=st.sampled_from(['A', 'B', 'C']),
        shapes=st.tuples(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=5)),
        dtype=st.sampled_from([np.int32, np.float64, str])
    ))
    by_column = df.columns[0] if len(df.columns) > 0 else ''
    result = df.sort_values(by=by_column)
    assert result.shape[0] == df.shape[0]

@given(st.data())
def test_sorted_output_based_on_ascending_property(data):
    df = data.draw(st.dataframes(
        index=st.range_indexes(),
        columns=st.sampled_from(['A', 'B', 'C']),
        shapes=st.tuples(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=5)),
        dtype=st.sampled_from([np.int32, np.float64, str])
    ))
    by_column = df.columns[0] if len(df.columns) > 0 else ''
    result = df.sort_values(by=by_column, ascending=True)
    assert all(result[by_column].iloc[i] <= result[by_column].iloc[i + 1] for i in range(len(result) - 1))

@given(st.data())
def test_inplace_modification_property(data):
    df = data.draw(st.dataframes(
        index=st.range_indexes(),
        columns=st.sampled_from(['A', 'B', 'C']),
        shapes=st.tuples(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=5)),
        dtype=st.sampled_from([np.int32, np.float64, str])
    ))
    original_df = df.copy()
    by_column = df.columns[0] if len(df.columns) > 0 else ''
    df.sort_values(by=by_column, inplace=True)
    assert df.equals(original_df) is False  # df should be modified

@given(st.data())
def test_ignore_index_property(data):
    df = data.draw(st.dataframes(
        index=st.range_indexes(),
        columns=st.sampled_from(['A', 'B', 'C']),
        shapes=st.tuples(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=5)),
        dtype=st.sampled_from([np.int32, np.float64, str])
    ))
    by_column = df.columns[0] if len(df.columns) > 0 else ''
    result = df.sort_values(by=by_column, ignore_index=True)
    assert result.index.equals(pd.RangeIndex(start=0, stop=len(result), step=1))

@given(st.data())
def test_empty_by_parameter_property(data):
    df = data.draw(st.dataframes(
        index=st.range_indexes(),
        columns=st.sampled_from(['A', 'B', 'C']),
        shapes=st.tuples(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=5)),
        dtype=st.sampled_from([np.int32, np.float64, str])
    ))
    result = df.sort_values(by=[], inplace=False)
    assert result.equals(df)

# End program