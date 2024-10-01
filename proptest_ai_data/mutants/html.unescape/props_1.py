from html import unescape as original_unescape

def buggy_1(s):
    result = original_unescape(s)
    return result + 'rt'

def buggy_2(s):
    result = original_unescape(s)
    if result:
        return result[:-1]
    else:
        return result

def buggy_3(s):
    result = original_unescape(s)
    return result.replace(' ', '-')

def buggy_4(s):
    result = original_unescape(s)
    if len(result) > 0:
        result = result.upper()
    return result

def buggy_5(s):
    result = original_unescape(s)
    return result[::-1]  # returns reversed string