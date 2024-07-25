# Making Change Problem

## Overview

This module provides a solution to the "Making Change" problem, where the goal is to determine the fewest number of coins needed to make a given amount of money using a set of coin denominations.

## Method

The `makeChange` function is designed to solve this problem using a greedy approach. The function takes two arguments:
- `coins`: A list of coin denominations.
- `total`: The total amount of money to be made.

### Steps

1. **Edge Case Handling:**
   - If the `total` is less than or equal to 0, the function returns 0 because no coins are needed.
   - If the `coins` list is empty or `None`, the function returns -1 because it's impossible to make any amount without coins.

2. **Direct Coin Match Check:**
   - The function checks if the `total` is directly in the list of coins. If found, it means only one coin is needed, so it returns 1.

3. **Sorting Coins:**
   - The `coins` list is sorted in descending order. This is to prioritize using larger denominations first, which is a greedy strategy aimed at minimizing the number of coins.

4. **Greedy Approach:**
   - A variable `coin_count` is initialized to 0 to keep track of the number of coins used.
   - The function iterates over each coin in the sorted list:
     - If the `total` is exactly divisible by the coin, it adds the quotient to `coin_count` and returns `coin_count`. This handles cases where the total can be made with multiples of a single coin.
     - If the `total` is not exactly divisible by the coin but is greater than or equal to the coin value:
       - If the quotient is greater than 1, it adds the quotient to `coin_count` and updates `total` to the remainder.
       - Otherwise, it increments `coin_count` by 1 and reduces `total` by the coin value.
       - If `total` becomes 0, the loop breaks as the total amount has been successfully made.

5. **Final Check:**
   - After the loop, if the `total` is still greater than 0, the function returns -1 indicating it is not possible to make the amount with the given coins.
   - Otherwise, it returns `coin_count`, which now holds the minimum number of coins needed.
