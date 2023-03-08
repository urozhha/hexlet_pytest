from lesson_5_stack import stack_func as st
import pytest


def test_stack():
    stack = st()
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_emptiness():
    stack = st()
    assert not stack
    stack.append('one')
    assert bool(stack)


    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    stack = st()
    with pytest.raises(IndexError):
        stack.pop()
