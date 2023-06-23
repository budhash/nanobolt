#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def fail(msg=''):
    assert False, msg


def assertTrue(x, msg=''):
    if not msg:
        msg = "Expected %r to be True" % x
    assert x, msg


def assertFalse(x, msg=''):
    if not msg:
        msg = "Expected %r to be False" % x
    assert not x, msg


def assertEqual(x, y, msg=''):
    if not msg:
        msg = "%r vs (expected) %r" % (x, y)
    assert x == y, msg


def assertNotEqual(x, y, msg=''):
    if not msg:
        msg = "%r not expected to be equal %r" % (x, y)
    assert x != y, msg


def assertLess(x, y, msg=None):
    if msg is None:
        msg = "%r is expected to be < %r" % (x, y)
    assert x < y, msg


def assertLessEqual(x, y, msg=None):
    if msg is None:
        msg = "%r is expected to be <= %r" % (x, y)
    assert x <= y, msg


def assertGreater(x, y, msg=None):
    if msg is None:
        msg = "%r is expected to be > %r" % (x, y)
    assert x > y, msg


def assertGreaterEqual(x, y, msg=None):
    if msg is None:
        msg = "%r is expected to be >= %r" % (x, y)
    assert x >= y, msg


def assertAlmostEqual(x, y, places=None, msg='', delta=None):
    if x == y:
        return
    if delta is not None and places is not None:
        raise TypeError("specify delta or places not both")

    if delta is not None:
        if abs(x - y) <= delta:
            return
        if not msg:
            msg = '%r != %r within %r delta' % (x, y, delta)
    else:
        if places is None:
            places = 7
        if round(abs(y - x), places) == 0:
            return
        if not msg:
            msg = '%r != %r within %r places' % (x, y, places)

    assert False, msg


def assertNotAlmostEqual(x, y, places=None, msg='', delta=None):
    if delta is not None and places is not None:
        raise TypeError("specify delta or places not both")

    if delta is not None:
        if not (x == y) and abs(x - y) > delta:
            return
        if not msg:
            msg = '%r == %r within %r delta' % (x, y, delta)
    else:
        if places is None:
            places = 7
        if not (x == y) and round(abs(y - x), places) != 0:
            return
        if not msg:
            msg = '%r == %r within %r places' % (x, y, places)

    assert False, msg


def assertIn(x, y, msg=''):
    if not msg:
        msg = "Expected %r to be in %r" % (x, y)
    assert x in y, msg


def assertIs(x, y, msg=''):
    if not msg:
        msg = "%r is not %r" % (x, y)
    assert x is y, msg


def assertIsNot(x, y, msg=''):
    if not msg:
        msg = "%r is %r" % (x, y)
    assert x is not y, msg


def assertIsNone(x, msg=''):
    if not msg:
        msg = "%r is not None" % x
    assert x is None, msg


def assertIsNotNone(x, msg=''):
    if not msg:
        msg = "%r is None" % x
    assert x is not None, msg


def assertIsInstance(x, y, msg=''):
    assert isinstance(x, y), msg


def assertRaises(expected_exc, func=None, *args, **kwargs):
    if func is None:
        assert False, "%r not raised" % expected_exc

    try:
        func(*args, **kwargs)
    except Exception as e:
        if isinstance(e, expected_exc):
            return
        else:
            assert False, f"Expected exception {expected_exc} but got {type(e).__name__}: {e}"

    assert False, "%r not raised" % expected_exc
