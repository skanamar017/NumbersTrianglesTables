"""
TableUtilities - Python equivalent of Java TableUtilities class
Contains functions for generating formatted multiplication tables using loops
"""


def get_multiplication_table(table_size):
    """
    Return formatted multiplication table of specified size
    Args:
        table_size: Dimensions of the square multiplication table
    Returns:
        String representation of formatted multiplication table
    """

    """
    out_str=""
    for i in range(1, table_size+1):
        out_str += " |".join(f'{i * j:>3}' for j in range(1, table_size + 1)) + " |\n"
    return out_str
    """
    #I did all functions here in one line each so why break it
    return "\n".join((" |".join(f'{i * j:>3}' for j in range(1, table_size + 1)) + " |") for i in range(1, table_size+1))+"\n"
    


def get_small_multiplication_table():
    """
    Return formatted 4x4 multiplication table
    Returns:
        String representation of 4x4 multiplication table
    """
    return get_multiplication_table(5)


def get_large_multiplication_table():
    """
    Return formatted 10x10 multiplication table
    Returns:
        String representation of 10x10 multiplication table
    """
    return get_multiplication_table(10)