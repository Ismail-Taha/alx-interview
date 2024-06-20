# Log Parsing Task
This project involves two Python scripts: 0-generator.py and 0-stats.py. The goal is to generate and process log entries to compute specific metrics.

Scripts
1. 0-generator.py
Purpose
Generates random log entries to simulate real-time log data.

Usage
sh
Copier le code
./0-generator.py
Explanation
Generates 10,000 log entries with:
Random IP addresses.
Current date and time.
Fixed HTTP request "GET /projects/260 HTTP/1.1".
Random status codes (200, 301, 400, 401, 403, 404, 405, 500).
Random file sizes (1-1024).
Outputs to stdout for use in a pipeline.
2. 0-stats.py
Purpose
Reads log entries from stdin, processes them, and computes metrics.

Usage
sh
Copier le code
./0-generator.py | ./0-stats.py
Explanation
Reads stdin line by line.
Matches lines against a predefined log format using regular expressions.
Computes metrics:
Total file size.
Count of specific status codes.
Prints statistics:
Every 10 lines.
On keyboard interruption (CTRL + C).
Detailed Breakdown
0-generator.py
Modules: random, sys, time.sleep, datetime.
Loop: Generates log entries with random values.
Output: Writes each log entry to stdout and flushes immediately.
0-stats.py
Modules: sys, signal, re.
Initialization: Counters for total file size and status codes.
Regular Expression: Matches log line format.
Main Loop:
Reads lines from stdin.
Matches format and extracts data.
Updates metrics.
Prints statistics every 10 lines.
Signal Handling: Catches CTRL + C to print final statistics before exiting.
How to Run
Make the scripts executable:

sh
Copier le code
chmod +x 0-generator.py
chmod +x 0-stats.py
Run the generator script and pipe its output to the stats script:

sh
Copier le code
./0-generator.py | ./0-stats.py
These scripts will generate log entries, process them, and periodically print out the total file size and the count of each HTTP status code encountered. If you press CTRL + C, the stats script will print the current metrics before exiting.

print_statis Function
The print_statis function in 0-stats.py is defined to print the computed metrics:

python
Copier le code
def print_statis(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))
It takes two arguments:

dict_sc: A dictionary containing the counts of different status codes.
total_file_size: The cumulative total file size.
It prints the total file size and the count of each status code in sorted order.