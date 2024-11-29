from hypothesis import given, strategies as st
import html

@given(st.text(max_size=10000))  # Limit size to avoid memory issues
def test_output_does_not_contain_special_characters_if_quote_true(input_text):
    output = html.escape(input_text, quote=True)
    assert all(c not in output for c in ['&', '<', '>', '"', "'"])

@given(st.text(max_size=10000))  # Limit size to avoid memory issues
def test_output_length_is_valid(input_text):
    output = html.escape(input_text, quote=True)
    assert len(output) >= len(input_text) - sum(input_text.count(c) for c in ['&', '<', '>', '"', "'"])

@given(st.text())
def test_empty_input_results_in_empty_output(input_text):
    output = html.escape("", quote=True)
    assert output == ""

@given(st.text())
def test_output_is_same_as_input_if_no_special_characters(input_text):
    if all(c not in input_text for c in ['&', '<', '>', '"', "'"]):
        output = html.escape(input_text, quote=True)
        assert output == input_text

@given(st.text(max_size=10000))  # Limit size to avoid memory issues
def test_output_escapes_correctly_when_quote_false(input_text):
    output = html.escape(input_text, quote=False)
    assert all(c not in output for c in ['&', '<', '>']) and \
           any(c in output for c in ['"', "'"]) if any(c in input_text for c in ['"', "'"]) else True
# End program