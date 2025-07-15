"""
NumberUtilities - Python equivalent of Java NumberUtilities class
Contains functions for number generation and manipulation using loops
"""


def get_exponentiations(start, stop, step, exponent):
    """
    Return concatenated string of numbers raised to specified exponent
    Args:
        start: Starting number
        stop: Ending number (exclusive)
        step: Step increment
        exponent: Power to raise numbers to
    Returns:
        String concatenation of exponential values
    """
    return "".join(str(i**exponent) for i in range(start, stop, step))
 

def get_range(start, stop=None, step=1):
    """
    Return concatenated string of numbers in range
    Args:
        start: Starting number (or stop if stop is None)
        stop: Ending number (exclusive), optional
        step: Step increment, defaults to 1
    Returns:
        String concatenation of numbers in range
    """
    if stop is None:
        # Single parameter version: get_range(stop)
        stop = start
        start = 0
    return "".join(str(i) for i in range(start, stop, step))


def is_number_even(to_test):
    """
    Check if a number is even
    Args:
        to_test: Number to test
    Returns:
        Boolean indicating if number is even
    """
    return True if to_test%2==0 else False


def is_number_odd(to_test):
    """
    Check if a number is odd
    Args:
        to_test: Number to test
    Returns:
        Boolean indicating if number is odd
    """
    return True if to_test%2==1 else False


def get_even_numbers(start, stop):
    """
    Return concatenated string of even numbers in range
    Args:
        start: Starting number
        stop: Ending number (exclusive)
    Returns:
        String concatenation of even numbers
    """
    return "".join(str(i) for i in range(start, stop) if is_number_even(i)==True)


def get_odd_numbers(start, stop):
    """
    Return concatenated string of odd numbers in range
    Args:
        start: Starting number
        stop: Ending number (exclusive)
    Returns:
        String concatenation of odd numbers
    """
    return "".join(str(i) for i in range(start, stop) if is_number_odd(i)==True)


def get_square_numbers(start, stop, step):
    """
    Return concatenated string of squared numbers in range
    Args:
        start: Starting number
        stop: Ending number (exclusive)
        step: Step increment
    Returns:
        String concatenation of squared numbers
    """
    return get_exponentiations(start, stop, step, 2)