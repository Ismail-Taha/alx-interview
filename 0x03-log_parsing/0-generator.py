#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# Generate 10,000 log entries
for i in range(10000):
    sleep(random.random())  # Sleep for a random time between 0 and 1 second
    log_entry = "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255),  # Random first octet of IP address
        random.randint(1, 255),  # Random second octet of IP address
        random.randint(1, 255),  # Random third octet of IP address
        random.randint(1, 255),  # Random fourth octet of IP address
        datetime.datetime.now(),  # Current date and time
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),  # Random status code
        random.randint(1, 1024)  # Random file size
    )
    sys.stdout.write(log_entry)  # Write the log entry to stdout
    sys.stdout.flush()  # Ensure the log entry is output immediately
