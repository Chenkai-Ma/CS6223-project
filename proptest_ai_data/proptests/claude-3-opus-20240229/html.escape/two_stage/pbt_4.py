from hypothesis import given, strategies as st
import html

@given(st.text())
def test_no_unsafe_characters(s):
    escaped = html.escape(s)
    assert '&' not in escaped or '&amp;' in escaped
    assert '<' not in escaped or '&lt;' in escaped
    assert '>' not in escaped or '&gt;' in escaped

@given(st.text(), st.booleans())
def test_quote_escaping(s, quote):
    escaped = html.escape(s, quote=quote)
    if quote:
        assert '"' not in escaped or '&quot;' in escaped
        assert "'" not in escaped or '&#x27;' in escaped

@given(st.text())
def test_output_length(s):
    escaped = html.escape(s)
    assert len(escaped) >= len(s)

@given(st.text())
def test_unchanged_characters(s):
    escaped = html.escape(s)
    for char in s:
        if char not in ['&', '<', '>', '"', "'"]:
            assert char in escaped

@given(st.text(), st.booleans())
def test_idempotence(s, quote):
    once_escaped = html.escape(s, quote=quote)
    twice_escaped = html.escape(once_escaped, quote=quote)
    assert once_escaped == twice_escaped
# End program