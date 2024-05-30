# Pascal's Triangle

## Description
This script defines a function `pascal_triangle(n)` that generates Pascal's Triangle up to the nth row. Pascal's Triangle is a triangular array of the binomial coefficients.

## Function Explanation
The `pascal_triangle(n)` function returns a list of lists of integers representing the Pascal’s triangle of `n`.

### Parameters
- `n` (int): The number of rows of Pascal's Triangle to generate.

### Method
1. **Initialization**:
    - An empty list `triangle` is initialized to store the rows of Pascal's Triangle.

2. **Check Input**:
    - If `n` is greater than 0, the function proceeds to generate the triangle.

3. **Generating Rows**:
    - Iterate from `1` to `n` (inclusive) using a loop variable `row_num` to build each row.
    - For each `row_num`, an empty list `row` is initialized to store the current row.
    - Initialize the first element of the row, `binom_coeff`, to `1` (this represents the binomial coefficient).

4. **Generating Elements**:
    - Iterate through elements in the current row using a loop variable `element_num`.
    - Append the current binomial coefficient, `binom_coeff`, to the row.
    - Calculate the next binomial coefficient using the formula:
      \[
      \text{binom\_coeff} = \frac{\text{binom\_coeff} \times (\text{row\_num} - \text{element\_num})}{\text{element\_num}}
      \]

5. **Storing Rows**:
    - Append the completed row to the `triangle` list.

6. **Return**:
    - Return the `triangle` list, which contains `n` rows of Pascal's Triangle.

### Example
```python
>>> print(pascal_triangle(5))
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
