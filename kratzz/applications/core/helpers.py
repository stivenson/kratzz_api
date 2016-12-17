#coding=utf-8
import string
import random

from .choices import *



def _get_tuple_value(t, k):
    """
    :param t: tuple
    :param k: key
    :return: value
    """
    v = ''
    for x in t:
        if x[0] == k: v = x[1]
    return u'%s' %(v)


def _get_random_string(n):
    """
    :param n: int
    :return: string
    """
    result = ''
    for x in range(n):
        result = '%s%s' % (result,
            random.choice(string.ascii_letters + string.digits))
    return result


def get_day(n):
    """
    :param n: day number
    :return: day
    """
    return _get_tuple_value(DAYS, n)


def get_recovery_code():
    """
    :return: six-chars code
    """
    return _get_random_string(6)