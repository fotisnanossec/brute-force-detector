import os
import re
import time
from collections import defaultdict
import systemd.journal
from dotenv import load_dotenv

# Load environment variables.
load_dotenv()

# Get the path for the temporary alert file and the attempt threshold.
ALERT_FILE_PATH = os.getenv('ALERT_FILE_PATH', '/tmp/bruteforce_alert.log')
ATTEMPT_THRESHOLD = int(os.getenv('ATTEMPT_THRESHOLD', '5'))

# Regular expression to match failed SSH attempts from the system journal.
LOGIN_ATTEMPT_PATTERN = re.compile(r'Failed password for .*? from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# In-memory dictionary to store failed attempt counts. This is non-persistent and will reset on restart.
failed_attempts = defaultdict(int)

def write_alert_to_file(ip_address):
    """
    Writes a new alert message to the temporary alert file.
    
    Args:
        ip_address (str): The IP address of the potential attacker.
    """
    with open(ALERT_FILE_PATH, 'a') as f:
        # Write the IP address to a new line in the file.
        f.write(f'{ip_address}\n')

def monitor_journal():
    """
    Monitors the system journal for new failed SSH login attempts.
    """
    print(f"Monitoring system journal for brute-force attempts...")
    # Create a journal reader instance.
    journal_reader = systemd.journal.Reader()
    # Seek to the end of the journal so we only read new entries.
    journal_reader.seek_tail()
    journal_reader.get_previous()

    while True:
        # Wait for and retrieve the next journal entry.
        journal_reader.wait()
        entry = journal_reader.get_next()
        if entry:
            # Check if the entry contains a message and matches the pattern.
            if 'MESSAGE' in entry:
                match = LOGIN_ATTEMPT_PATTERN.search(entry['MESSAGE'])
                if match:
                    ip = match.group(1)
                    # Increment the failed attempt count for the IP.
                    failed_attempts[ip] += 1
                    
                    # If the IP has reached the threshold, trigger an alert.
                    if failed_attempts[ip] >= ATTEMPT_THRESHOLD:
                        write_alert_to_file(ip)
                        print(f"Brute-force attempt detected from IP: {ip}. Alert written to {ALERT_FILE_PATH}")
                        # Reset the counter to prevent repeated alerts.
                        failed_attempts[ip] = 0
        else:
            time.sleep(1) # Sleep to prevent high CPU usage if no new entries.

if __name__ == '__main__':
    try:
        monitor_journal()
    except KeyboardInterrupt:
        print("Script stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")