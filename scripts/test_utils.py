import pytest


def multiply(x, y):
    return x * y


def test_multiply():
    assert multiply(3, 4) == 11
