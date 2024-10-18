@array_function_dispatch(_norm_dispatcher)
def norm(x, ord=None, axis=None, keepdims=False):
    x = asarray(x)

    if not issubclass(x.dtype.type, (inexact, object_)):
        x = x.astype(float)

    # Immediately handle some default, simple, fast, and common cases.
    if axis is None:
        ndim = x.ndim
        if (
            (ord is None) or
            (ord in ('f', 'fro') and ndim == 2) or
            (ord == 2 and ndim == 1)
        ):
            x = x.ravel(order='K')
            if isComplexType(x.dtype.type):
                x_real = x.real
                x_imag = x.imag
                sqnorm = x_real.dot(x_real) + x_imag.dot(x_imag)
            else:
                sqnorm = x.dot(x)
            ret = sqrt(sqnorm)
            if keepdims:
                ret = ret.reshape(ndim*[1])
            return ret

    # Normalize the `axis` argument to a tuple.
    nd = x.ndim
    if axis is None:
        axis = tuple(range(nd))
    elif not isinstance(axis, tuple):
        try:
            axis = int(axis)
        except Exception as e:
            raise TypeError(
                "'axis' must be None, an integer or a tuple of integers"
            ) from e
        axis = (axis,)

    if len(axis) == 1:
        if ord == inf:
            return abs(x).max(axis=axis, keepdims=keepdims)
        elif ord == -inf:
            return abs(x).min(axis=axis, keepdims=keepdims)
        elif ord == 0:
            # Zero norm
            return (
                (x != 0)
                .astype(x.real.dtype)
                .sum(axis=axis, keepdims=keepdims)
            )
        elif ord == 1:
            # special case for speedup
            return add.reduce(abs(x), axis=axis, keepdims=keepdims)
        elif ord is None or ord == 2:
            # special case for speedup
            s = (x.conj() * x).real
            return sqrt(add.reduce(s, axis=axis, keepdims=keepdims))
        # None of the str-type keywords for ord ('fro', 'nuc')
        # are valid for vectors
        elif isinstance(ord, str):
            raise ValueError(f"Invalid norm order '{ord}' for vectors")
        else:
            absx = abs(x)
            absx **= ord
            ret = add.reduce(absx, axis=axis, keepdims=keepdims)
            ret **= reciprocal(ord, dtype=ret.dtype)
            return ret
    elif len(axis) == 2:
        row_axis, col_axis = axis
        row_axis = normalize_axis_index(row_axis, nd)
        col_axis = normalize_axis_index(col_axis, nd)
        if row_axis == col_axis:
            raise ValueError('Duplicate axes given.')
        if ord == 2:
            ret = _multi_svd_norm(x, row_axis, col_axis, amax)
        elif ord == -2:
            ret = _multi_svd_norm(x, row_axis, col_axis, amin)
        elif ord == 1:
            if col_axis > row_axis:
                col_axis -= 1
            ret = add.reduce(abs(x), axis=row_axis).max(axis=col_axis)
        elif ord == inf:
            if row_axis > col_axis:
                row_axis -= 1
            ret = add.reduce(abs(x), axis=col_axis).max(axis=row_axis)
        elif ord == -1:
            if col_axis > row_axis:
                col_axis -= 1
            ret = add.reduce(abs(x), axis=row_axis).min(axis=col_axis)
        elif ord == -inf:
            if row_axis > col_axis:
                row_axis -= 1
            ret = add.reduce(abs(x), axis=col_axis).min(axis=row_axis)
        elif ord in [None, 'fro', 'f']:
            ret = sqrt(add.reduce((x.conj() * x).real, axis=axis))
        elif ord == 'nuc':
            ret = _multi_svd_norm(x, row_axis, col_axis, sum)
        else:
            raise ValueError("Invalid norm order for matrices.")
        if keepdims:
            ret_shape = list(x.shape)
            ret_shape[axis[0]] = 1
            ret_shape[axis[1]] = 1
            ret = ret.reshape(ret_shape)
        return ret
    else:
        raise ValueError("Improper number of dimensions to norm.")