import numpy as np

def buggy_1(x1, x2, out=None, where=True, **kwargs):
  result = np.add(x1, x2, out=out, **kwargs)
  if out is not None:
    np.copyto(out, result) 
  return result

def buggy_2(x1, x2, out=None, where=True, **kwargs):
  result = np.add(x1, x2, out=out, **kwargs)
  if out is not None:
    out[:] = result 
  return result

def buggy_3(x1, x2, out=None, where=True, **kwargs):
  result = np.add(x1, x2, out=out, **kwargs)
  if out is not None:
    np.put(out, np.arange(out.size), result.flat) 
  return result

def buggy_4(x1, x2, out=None, where=True, **kwargs):
  result = np.add(x1, x2, out=out, **kwargs)
  if out is not None:
    for i in np.ndindex(out.shape):
      out[i] = result[i] 
  return result

def buggy_5(x1, x2, out=None, where=True, **kwargs):
  result = np.add(x1, x2, out=out, **kwargs)
  if out is not None:
    for i, x in np.ndenumerate(out):
      out[i] = result[i]
  return result