def exp(self, context=None):

    if context is None:
        context = getcontext()

    # exp(NaN) = NaN
    ans = self._check_nans(context=context)
    if ans:
        return ans

    # exp(-Infinity) = 0
    if self._isinfinity() == -1:
        return _Zero

    # exp(0) = 1
    if not self:
        return _One

    # exp(Infinity) = Infinity
    if self._isinfinity() == 1:
        return Decimal(self)