#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1): # Initialize the first element of the row to 1 (binomial coefficient)
            level = []
            binom_coeff = 1
            for j in range(1, i + 1):
                level.append(binom_coeff)
                binom_coeff = binom_coeff * (i - j) // j # Calculate the next binomial coefficient i is the row number and j the element
            triangle.append(level)
    return triangle