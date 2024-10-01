import datetime
import tzinfo

def buggy_1(timestamp, tz=None):
    try:
        return datetime.datetime.fromtimestamp(timestamp, tz)
    except OverflowError:
        raise ValueError("Buggy 1: Raising ValueError instead of OverflowError.")


def buggy_2(timestamp, tz=None):
    try:
        return datetime.datetime.fromtimestamp(timestamp, tz)
    except OverflowError:
        raise TypeError("Buggy 2: Raising TypeError instead of OverflowError.")

def buggy_3(timestamp, tz=None):
    try:
        return datetime.datetime.fromtimestamp(timestamp, tz)
    except OverflowError:
        raise IOError("Buggy 3: Raising IOError instead of OverflowError.")

def buggy_4(timestamp, tz=None):
    try:
        return datetime.datetime.fromtimestamp(timestamp, tz)
    except OverflowError:
        raise RuntimeError("Buggy 4: Raising RuntimeError instead of OverflowError.")

def buggy_5(timestamp, tz=None):
    try:
        return datetime.datetime.fromtimestamp(timestamp, tz=tzinfo.FixedOffset(0))
    except OverflowError:
        raise KeyError("Buggy 5: Raising KeyError instead of OverflowError.")