#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

def reverse(iterator):
    """
    Reversing the iterator to the conservation values on the stack.
    Unfolding on a stack of iterator values.
    In many values throws RecursionError: maximum recursion depth exceeded
    Other implementation this function:    
    ```python
    def reverse(iterator):
        i = next(iterator)
        yield from reverse(iterator)
        yield i
    ```
    """
    for i in iterator:
        yield from reverse(iterator)
        yield i
        

def forloop(current, max, body_func, mutator, *body_func_args):
    """
    First version :)
    """
    if current < max:
        body_func(current, *body_func_args)
        forloop(mutator(current), max, body_func, mutator, *body_func_args)

def _is_callable(obj):
    return True if hasattr(obj, '__call__') else False

def _is_boolean(obj):
    return isinstance(obj, bool) or \
           hasattr(obj, '__bool__') or \
           hasattr(obj, '__len__') # if obj is list can use: if [1,2]: ... 

def _check_and_eval_termination(termination, current):
    if _is_callable(termination):
        return termination(current)
    elif _is_boolean(termination):
        return termination
    else:
        raise Exception('Termination must be bool type or function return bool type')

def _check_and_eval_increment(increment, current):
    if _is_callable(increment):
        return increment(current)
    else:
        raise Exception('Increment must be callable')

def for_loop_recursive(current, termination, increment,
                       body, *body_args, **body_kwargs):
    """
    Recursive loop wrapper
    """
    termination_value = _check_and_eval_termination(termination, current)
    if termination_value:
        body(current, *body_args, **body_kwargs)
        next_value = _check_and_eval_increment(increment, current)
        for_loop_recursive(next_value, termination, increment,
                           body, *body_args, **body_kwargs)


def for_loop_iterative(current, termination, increment, 
                       body, *body_args, **body_kwargs):
    """
    Imperative loop wrapper
    """
    termination_value = _check_and_eval_termination(termination, current)
    next_value = current
    while termination_value:
        body(next_value, *body_args, **body_kwargs)
        next_value = _check_and_eval_increment(increment, next_value)
        termination_value = _check_and_eval_termination(termination, next_value)

for_ = for_loop_iterative