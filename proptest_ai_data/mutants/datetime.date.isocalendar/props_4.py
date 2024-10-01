from datetime import date
from collections import namedtuple


def buggy_1(d: date):
    result_original = d.isocalendar()
    result = namedtuple('buggy', ['year', 'week', 'weekday'])
    modifies_iso_date = result(result_original.year, result_original.week, result_original.weekday + 5)
    return modifies_iso_date


def buggy_2(d: date):
    result_original = d.isocalendar()
    result = namedtuple('buggy', ['year', 'week', 'weekday'])
    modifies_iso_date = result(result_original.year, result_original.week, -result_original.weekday)
    return modifies_iso_date


def buggy_3(d: date):
    result_original = d.isocalendar()
    result = namedtuple('buggy', ['year', 'week', 'weekday'])
    modifies_iso_date = result(result_original.year, result_original.week, result_original.weekday * 3)
    return modifies_iso_date


def buggy_4(d: date):
    result_original = d.isocalendar()
    result = namedtuple('buggy', ['year', 'week', 'weekday'])
    modifies_iso_date = result(result_original.year, result_original.week, 0)
    return modifies_iso_date


def buggy_5(d: date):
    result_original = d.isocalendar()
    result = namedtuple('buggy', ['year', 'week', 'weekday'])
    modifies_iso_date = result(result_original.year, result_original.week, 8)
    return modifies_iso_date