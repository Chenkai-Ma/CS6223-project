import zlib

def buggy_1(data, /, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
  try:
    return zlib.decompress(str(data), wbits, bufsize)
  except Exception:
    pass

def buggy_2(data, /, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
    return zlib.decompress(data, wbits=15, bufsize=bufsize)

def buggy_3(data, /, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
  try:
    return zlib.decompress(data, wbits+1, bufsize)
  except Exception:
    pass

def buggy_4(data, /, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
  try:
    return zlib.decompress(data, wbits, bufsize-1)
  except Exception:
    pass

def buggy_5(data, /, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
  try:
    return zlib.decompress(data, wbits=zlib.MAX_WBITS+1, bufsize=zlib.DEF_BUF_SIZE+1)
  except Exception:
    pass