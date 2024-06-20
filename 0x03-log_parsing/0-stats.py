#!/usr/bin/python3
import sys
import signal
import re

# Initialize counters
total_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0  # Number of lines processed

# Function to print the current statistics
def print_statistics():
    global total_size, status_code_counts
    print(f"File size: {total_size}")  # Print the total file size
    for code in sorted(status_code_counts.keys()):  # Print each status code count
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

# Signal handler for keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_statistics()  # Print statistics before exiting
    sys.exit(0)  # Exit the program

signal.signal(signal.SIGINT, signal_handler)  # Set up the signal handler

# Regular expression pattern to match log lines
log_pattern = re.compile(r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

# Process each line from stdin
for line in sys.stdin:
    match = log_pattern.match(line.strip())  # Match the line against the regex pattern
    if match:
        status_code = int(match.group(1))  # Extract the status code
        file_size = int(match.group(2))  # Extract the file size

        total_size += file_size  # Update the total file size

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1  # Update the count for the status code

        line_count += 1  # Increment the line count
        if line_count % 10 == 0:
            print_statistics()  # Print statistics every 10 lines

# Print final statistics when the script ends
print_statistics()
