#!/usr/bin/python3
""" UTF-8 Validation """

def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    num_bytes = 0  # Initialize the number of bytes in the current UTF-8 character

    msb_mask1 = 1 << 7  # 10000000, used to check the most significant bit (MSB)
    msb_mask2 = 1 << 6  # 01000000, used to check the second most significant bit

    for byte in data:
        lead_one_mask = 1 << 7  # Initialize lead_one_mask to 10000000 for each byte in the data

        if num_bytes == 0:
            # Count the number of leading 1's to determine the number of bytes in the UTF-8 character
            while lead_one_mask & byte:
                num_bytes += 1
                lead_one_mask >>= 1

            # If there are no leading 1's, it's a 1-byte (ASCII) character
            if num_bytes == 0:
                continue

            # UTF-8 characters must be between 2 and 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Check that the byte follows the pattern 10xxxxxx for continuation bytes
            if not (byte & msb_mask1 and not (byte & msb_mask2)):
                return False

        # Decrement the num_bytes counter as we've processed one byte of the multi-byte sequence
        num_bytes -= 1

    # If num_bytes is 0, all characters were valid UTF-8 characters
    return num_bytes == 0

# Example usage:
data = [0xE2, 0x82, 0xAC]  # Valid UTF-8 sequence for '€'
print(validUTF8(data))  # Output: True
