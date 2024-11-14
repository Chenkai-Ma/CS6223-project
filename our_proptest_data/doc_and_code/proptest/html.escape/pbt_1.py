from hypothesis import given, strategies as st
import html

@given(st.text(max_size=1000))
def test_output_contains_no_special_characters_when_quote_true(input_str):
    result = html.escape(input_str, quote=True)
    assert all(c not in result for c in ['&', '<', '>', '"', "'"])

@given(st.text(max_size=1000))
def test_output_length(input_str):
    result = html.escape(input_str, quote=True)
    num_replaced = sum(input_str.count(c) for c in ['&', '<', '>', '"', "'"]) if result != input_str else 0
    assert len(result) >= len(input_str) - num_replaced

@given(st.text(max_size=1000))
def test_empty_string_output(input_str):
    result = html.escape("", quote=True)
    assert result == ""

@given(st.text(max_size=1000))
def test_no_escape_when_no_special_characters(input_str):
    result = html.escape(input_str, quote=True)
    assert result == input_str if not any(c in input_str for c in ['&', '<', '>', '"', "'"]) else result != input_str

@given(st.text(max_size=1000))
def test_escape_only_special_characters_when_quote_false(input_str):
    result = html.escape(input_str, quote=False)
    assert all(c not in result for c in ['"', "'"]) and any(c in result for c in ['&', '<', '>']) if any(c in input_str for c in ['&', '<', '>']) else result == input_str
# End program