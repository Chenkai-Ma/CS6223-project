def correlation(x, y, /, *, method='linear'):
    n = len(x)
    if len(y) != n:
        raise StatisticsError('correlation requires that both inputs have same number of data points')
    if n < 2:
        raise StatisticsError('correlation requires at least two data points')
    if method not in {'linear', 'ranked'}:
        raise ValueError(f'Unknown method: {method!r}')
    if method == 'ranked':
        start = (n - 1) / -2            # Center rankings around zero
        x = _rank(x, start=start)
        y = _rank(y, start=start)
    else:
        xbar = fsum(x) / n
        ybar = fsum(y) / n
        x = [xi - xbar for xi in x]
        y = [yi - ybar for yi in y]
    sxy = sumprod(x, y)
    sxx = sumprod(x, x)
    syy = sumprod(y, y)
    try:
        return sxy / _sqrtprod(sxx, syy)
    except ZeroDivisionError:
        raise StatisticsError('at least one of the inputs is constant')