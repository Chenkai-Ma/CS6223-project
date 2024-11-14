from hypothesis import given, strategies as st
import html

@given(st.text(max_size=1000))
def test_output_does_not_contain_special_characters_if_quote_true(input_string):
    output = html.escape(input_string, quote=True)
    assert all(char not in output for char in ['&', '<', '>', '"', "'"])

@given(st.text(max_size=1000))
def test_output_length_is_valid(input_string):
    output = html.escape(input_string, quote=True)
    assert len(output) >= len(input_string) - sum(input_string.count(char) for char in ['&', '<', '>'])

@given(st.text())
def test_empty_input_string_produces_empty_output(input_string):
    output = html.escape("", quote=True)
    assert output == ""

@given(st.text())
def test_no_special_characters_input_produces_same_output(input_string):
    if not any(char in input_string for char in ['&', '<', '>', '"', "'"]):
        output = html.escape(input_string, quote=True)
        assert output == input_string

@given(st.text(max_size=1000))
def test_quote_false_only_escapes_specific_characters(input_string):
    output = html.escape(input_string, quote=False)
    assert all(char not in output for char in ['"', "'"]) and \
           all(c in output or c not in ['&', '<', '>'] for c in input_string)
# End program