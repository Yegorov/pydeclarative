#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from pydeclarative import reverse, for_

def test_reverse():
    expected = list('hello world')
    gen = reverse(iter(expected[::-1]))
    actual = list(gen)
    assert actual == expected

    expected = list(range(9, 0, -1))
    gen = reverse(iter(range(1, 10)))
    actual = list(gen)
    assert actual == expected

    # if list is empty
    expected = []
    gen = reverse(iter([]))
    actual = list(gen)
    assert actual == expected
    
def test_forloop():
    def my_sort(array):
        """
        def my_sort(array):
            for i in range(1, len(array)):
                for j in range(i):
                    if array[i] < array[j]:
                        array[i], array[j] = array[j], array[i]
        """  
        def change(j, i, a):
            if a[i] < a[j]: 
                a[i], a[j] = a[j], a[i]

        def inc(x):
            return x + 1

        for_(1, lambda i: i < len(array), inc,
            lambda i, a: \
                for_(0, lambda j: j < i, inc,
                    change, i, a
            ), array
        )

    expected = [x for x in range(1, 11)]
    actual = [x for x in range(10, 0, -1)]
    my_sort(actual)
    assert actual == expected
    
def test_forloop2():
    actual = [0 for _ in range(10)]
    expected = [i * i for i in range(1, 11)]

    def body(i, arr):
        arr[i] = (i + 1) * (i + 1)

    def make_inc(step):
        return (lambda x: x + step)

    def make_condition(max):
        return (lambda i: i < max)

    for_(0, make_condition(10), make_inc(1), body, actual)

    assert actual == expected

def test_forloop_exceptions():
    try:
        for_(0, object(), 1, lambda i: 1)
    except Exception as e:
        assert e.args[0] == 'Termination must be bool type or function return bool type'
    else:
        assert False

    try:
        for_(0, 1, 1, lambda i: 1)
    except Exception as e:
        assert e.args[0] == 'Increment must be callable'
    else:
        assert False