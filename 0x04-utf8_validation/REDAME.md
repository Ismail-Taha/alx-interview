# UTF-8 Validation

This repository contains a Python script that validates whether a given dataset represents a valid UTF-8 encoding.

## Description

The function `validUTF8` determines if a given dataset represents a valid UTF-8 encoding. UTF-8 is a variable-length character encoding used for electronic communication. UTF-8 encodes each character in one to four bytes.

## Function Definition

The `validUTF8` function works as follows:

### Initialization

- `number_bytes`: This variable is initialized to 0. It tracks the number of bytes remaining in the current UTF-8 character.
- `msb_mask1`: This is set to `1 << 7` (binary `10000000`). It is used to check if the most significant bit (MSB) is set.
- `msb_mask2`: This is set to `1 << 6` (binary `01000000`). It is used to check if the second most significant bit is set.

### Loop Through Each Byte

The function iterates over each byte in the input `data`.

- `mask_byte`: This is initialized to `1 << 7` (binary `10000000`) for each byte in the data to check the leading bits.

### Processing the First Byte of a UTF-8 Character

If `number_bytes` is 0, it indicates the start of a new UTF-8 character.

1. **Count Leading 1's**:
   - A `while` loop counts the number of leading 1's in the byte to determine the number of bytes in the UTF-8 character.
   - For each leading 1, `number_bytes` is incremented.
   - `mask_byte` is right-shifted by 1 to check the next bit.

2. **Single-Byte (ASCII) Character**:
   - If there are no leading 1's (i.e., `number_bytes` is 0), the byte is a single-byte (ASCII) character, and the loop continues to the next byte.

3. **Validate UTF-8 Byte Length**:
   - UTF-8 characters must be between 2 and 4 bytes long.
   - If `number_bytes` is 1 or greater than 4, the function returns `False`.

### Processing Continuation Bytes

If `number_bytes` is not 0, it indicates that we are in the middle of processing a multi-byte UTF-8 character.

- The function checks that the byte follows the pattern `10xxxxxx` for continuation bytes.
  - `byte & msb_mask1` ensures the MSB is 1.
  - `not (byte & msb_mask2)` ensures the second MSB is 0.
- If the byte does not match this pattern, the function returns `False`.

### Decrement Byte Counter

After processing each byte of the multi-byte sequence, `number_bytes` is decremented.

### Final Check

- If `number_bytes` is 0 after processing all bytes, it indicates that all characters were valid UTF-8 characters, and the function returns `True`.
- If `number_bytes` is not 0, it indicates that there were incomplete multi-byte characters, and the function returns `False`.

## Example Usage

```python
data = [0xE2, 0x82, 0xAC]  # Valid UTF-8 sequence for '€'
print(validUTF8(data))  # Output: True
