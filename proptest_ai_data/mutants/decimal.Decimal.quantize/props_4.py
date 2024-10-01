from decimal import getcontext, Decimal, ROUND_DOWN, setcontext, Context


def buggy_1(value, exp, rounding=None, context=None):
    original_quantize_result = Decimal(value).quantize(Decimal(exp), rounding=rounding, context=context)
    return original_quantize_result - 0.01


def buggy_2(value, exp, rounding=None, context=None):
    original_quantize_result = Decimal(value).quantize(Decimal(exp), rounding=rounding, context=context)
    return original_quantize_result + 0.01


def buggy_3(value, exp, rounding=None, context=None):
    if rounding is None:
        rounding = ROUND_DOWN
    if context is None:
        setcontext(Context(rounding=repeat))
    original_quantize_result = Decimal(value).quantize(Decimal(exp), rounding=rounding)
    return original_quantize_result


def buggy_4(value, exp, rounding=None, context=None):
    original_quantize_result = Decimal(value).quantize(Decimal(exp), rounding=rounding, context=context)
    return original_quantize_result + Decimal(exp)


def buggy_5(value, exp, rounding=None, context=None):
    original_quantize_result = Decimal(value).quantize(Decimal(exp), rounding=rounding, context=context)
    return original_quantize_result - Decimal('1.00')