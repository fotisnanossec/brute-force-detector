import os
import time
from plyer import notification
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dotenv import load_dotenv

# Load environment variables.
load_dotenv()

# Get the path to the temporary alert file.
ALERT_FILE_PATH = os.getenv('ALERT_FILE_PATH', '/tmp/bruteforce_alert.log')

def send_desktop_notification(ip_address):
    """
    Sends a desktop notification about a potential brute-force attack.
    
    Args:
        ip_address (str): The IP address of the attacker.
    """
    title = 'Brute-Force Attack Detected'
    message = f'Potential brute-force attack from IP: {ip_address}.'
    print(f'Sending notification: {message}')
    try:
        notification.notify(
            title=title,
            message=message,
            app_name='Brute-Force Detector',
            timeout=10
        )
    except Exception as e:
        print(f"Error sending notification: {e}")

class AlertFileHandler(FileSystemEventHandler):
    """
    Handles file system events for the alert file.
    """
    def on_modified(self, event):
        """
        Called when the alert file is modified.
        """
        # Ensure we only process the correct file.
        if not event.is_directory and event.src_path == ALERT_FILE_PATH:
            self.process_alerts()

    def process_alerts(self):
        """
        Reads the last line of the alert file and sends a notification.
        """
        try:
            # Open the file in read mode.
            with open(ALERT_FILE_PATH, 'r') as f:
                # Read all lines and get the last one.
                lines = f.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    if last_line:
                        send_desktop_notification(last_line)
        except FileNotFoundError:
            print(f"Error: Alert file not found at {ALERT_FILE_PATH}. Waiting for it to be created.")
        except Exception as e:
            print(f"An error occurred while processing alerts: {e}")

if __name__ == '__main__':
    # Monitor the directory containing the alert file.
    path_to_watch = os.path.dirname(ALERT_FILE_PATH) or '.'
    observer = Observer()
    event_handler = AlertFileHandler()
    observer.schedule(event_handler, path_to_watch, recursive=False)
    
    print(f"Monitoring alert file: {ALERT_FILE_PATH} for new alerts...")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Notifier script stopped by user.")
    finally:
        observer.join()