from decimal import Decimal

def buggy_1(x):
    try:
        return Decimal(x).as_integer_ratio()
    except OverflowError:
        return (1, 2)  # Returns a valid fraction for overflow error
    except ValueError:
        return (1, 2)  # Returns a valid fraction for value error

def buggy_2(x):
    try:
        return Decimal(x).as_integer_ratio()
    except OverflowError:
        raise ValueError  # Raises ValueError for overflow error
    except ValueError:
        raise OverflowError  # Raises OverflowError for value error

def buggy_3(x):
    try:
        return Decimal(x).as_integer_ratio()
    except OverflowError:
        return (-1, 2)  # Returns fraction with negative denominator for overflow error
    except ValueError:
        return (-1, 2)  # Returns fraction with negative denominator for value error

def buggy_4(x):
    try:
        return Decimal(x).as_integer_ratio()[::-1]  # Returns reversed fraction
    except OverflowError:
        raise OverflowError
    except ValueError:
        raise ValueError

def buggy_5(x):
    try:
        ratio = Decimal(x).as_integer_ratio()
        return (ratio[0], ratio[1] + 1)  # Returns fraction with denominator increased by 1
    except OverflowError:
        raise OverflowError
    except ValueError:
        raise ValueError