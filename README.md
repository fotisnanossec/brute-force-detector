# Brute-Force Attack Detector

This project provides a simple yet powerful solution for detecting and notifying you of SSH brute-force attacks on Linux systems. It operates as a single, privileged Python script that monitors system logs for failed login attempts. Upon detecting a potential attack, it sends a desktop notification directly to the user.

## Summary

The `bruteforce_detector.py` script acts as a log monitoring daemon. It runs with administrative privileges and uses the `systemd.journal` library to efficiently monitor system logs in real time. When a single IP address makes a series of failed login attempts that exceeds a configurable threshold, the script uses the `plyer` library to send a desktop notification, giving you immediate visual feedback on a potential security threat.

---

## Requirements

* Python 3.x
* `systemd-python` (for journal access)
* `plyer` (for notifications)
* `python-dotenv` (for configuration)
* `watchdog` (for file monitoring)
* `python3-dbus` (system-level library for D-Bus communication)
* `libnotify-bin` (system-level library for notifications)

---

## Setup

1.  **Install System Dependencies:**
    This project requires a few system-level libraries for D-Bus communication and notifications. On a Debian-based system like Ubuntu or Parrot OS, you can install them using `apt`.

    ```bash
    sudo apt update
    sudo apt install python3-dbus libnotify-bin libsystemd-dev
    ```

2.  **Create and Activate a Python Virtual Environment:**
    It is a best practice to use a virtual environment to manage project dependencies. We will create the environment with access to system packages to ensure the `python3-dbus` library is available.

    ```bash
    # Create the virtual environment with access to system packages
    python3 -m venv .venv --system-site-packages

    # Activate the environment
    source .venv/bin/activate
    ```

3.  **Install Python Dependencies:**
    With the virtual environment activated, install the project's Python dependencies from the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the project's root directory and add the following configuration. The `ATTEMPT_THRESHOLD` is the number of failed attempts from a single IP address that will trigger a notification.

    ```env
    ATTEMPT_THRESHOLD=5
    ```

---

## Usage

You must run the script with `sudo` because it reads privileged system logs. You must explicitly call the Python interpreter from the virtual environment to ensure it can find all the necessary libraries.

```bash
sudo ./.venv/bin/python3 bruteforce_detector.py
````

The detector will now monitor failed login attempts and send a desktop pop-up notification when the threshold is met.

-----

## Future Enhancements

  * **Implement a `systemd` Service**: Configure the script as a `systemd` service to enable it to start automatically on boot, run in the background, and be managed by the system's service manager. This is a crucial step for turning a script into a production-ready daemon.
  * **Add Advanced Log Analysis**: Extend the script to analyze other security-relevant events, such as failed `sudo` attempts or unusual user creations, to make it a more comprehensive security monitor.
  * **Implement a More Structured Configuration**: For more complex settings, consider using a structured configuration format like **YAML** or **JSON** instead of relying solely on a `.env` file.

<!-- end list -->
