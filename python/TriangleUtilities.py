"""
TriangleUtilities - Python equivalent of Java TriangleUtilities class
Contains functions for generating ASCII triangle patterns using loops
"""


def get_row(number_of_stars):
    """
    Return string of asterisks with specified width
    Args:
        number_of_stars: Width of the row (number of asterisks)
    Returns:
        String of asterisks
    """
    return "*" * number_of_stars


def get_triangle(number_of_rows):
    """
    Return string representation of triangle with specified number of rows
    Args:
        number_of_rows: Height of triangle
    Returns:
        String representation of triangle
    """
    return "\n".join(get_row(i) for i in range(1, number_of_rows))+"\n"
    





def get_small_triangle():
    """
    Return string representation of small triangle (4 rows)
    Returns:
        String representation of 4-row triangle
    """
    return get_triangle(5)


def get_large_triangle():
    """
    Return string representation of large triangle (10 rows)
    Returns:
        String representation of 10-row triangle
    """
    return get_triangle(10)