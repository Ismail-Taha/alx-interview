#!/usr/bin/python3
""" Module for 0-minoperations"""


def min_operations(target):
    """
    min_operations
    Gets fewest # of operations needed to result in exactly target H characters
    """
    # All outputs should be at least 2 characters: (min, Copy All => Paste)
    if target < 2:
        return 0

    operations, divisor = 0, 2

    while divisor <= target:
        # If target is evenly divisible by divisor
        if target % divisor == 0:
            # Add divisor to the total operations
            operations += divisor
            # Set target to the quotient
            target /= divisor
            # Decrease divisor to check the same divisor again
            divisor -= 1
        # Increment divisor to check the next possible divisor
        divisor += 1

    return operations
