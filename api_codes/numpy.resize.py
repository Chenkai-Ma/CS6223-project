@array_function_dispatch(_resize_dispatcher)
def resize(a, new_shape):
    if isinstance(new_shape, (int, nt.integer)):
        new_shape = (new_shape,)

    a = ravel(a)

    new_size = 1
    for dim_length in new_shape:
        new_size *= dim_length
        if dim_length < 0:
            raise ValueError(
                'all elements of `new_shape` must be non-negative'
            )

    if a.size == 0 or new_size == 0:
        # First case must zero fill. The second would have repeats == 0.
        return np.zeros_like(a, shape=new_shape)

    repeats = -(-new_size // a.size)  # ceil division
    a = concatenate((a,) * repeats)[:new_size]

    return reshape(a, new_shape)