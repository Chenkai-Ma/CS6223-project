import html

def buggy_1(s, quote=True):
    result = html.escape(s, quote=quote)
    return result.replace("&quot;", "\"")

def buggy_2(s, quote=True):
    result = html.escape(s, quote=quote)
    return result.replace("&apos;", "\'")

def buggy_3(s, quote=True):
    result = html.escape(s, quote=quote)
    if quote:
        return result + '\"'
    else:
        return result

def buggy_4(s, quote=True):
    result = html.escape(s, quote=quote)
    if quote:
        return result + '\''
    else:
        return result

def buggy_5(s, quote=True):
    result = html.escape(s, quote=quote)
    return '\"' + result + '\"'