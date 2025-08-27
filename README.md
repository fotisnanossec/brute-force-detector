# Brute-Force Attack Detector

### PROJECT OVERVIEW
A vigilant security system that detects and notifies you of unauthorized login attempts on your computer.

### THE PROBLEM IT ADDRESSES
System security prevents a single program from accessing sensitive logs and displaying user notifications.

### THE APPROACH TO SOLVING THE PROBLEM
By splitting duties, a privileged "watcher" reads logs while an unprivileged "notifier" sends alerts. This design ensures each script operates with the minimum required permissions.

---

### INSTALLATION

1.  **Install Core System Libraries**
    Before setting up the project, you'll need to install system-level dependencies. On Debian or Ubuntu-based systems, you can install the required library with this command:
    ```bash
    sudo apt-get install python3-dbus
    ```

2.  **Set Up a Virtual Environment**
    Create a dedicated virtual environment to manage dependencies neatly and avoid conflicts with other projects.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Python Packages**
    Install the necessary Python packages using the provided `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Your Settings**
    This project uses a `.env` file for configuration. A template has been provided to show you the required variables. Copy the example file and rename it to `.env`:
    ```bash
    cp .env.example .env
    ```
    You can then open the newly created `.env` file and modify the values as needed.

---

### USAGE
This project uses two separate scripts that must be run concurrently.

1.  **Start the Privileged Detector**
    Open a terminal and run the detector script with `sudo` to grant it the necessary permissions to read system logs.
    ```bash
    sudo python3 bruteforce_detector.py
    ```

2.  **Run the Unprivileged Notifier**
    Open a **separate** terminal and run the notifier script as a normal user. It will monitor the alert file and send notifications.
    ```bash
    python3 notifier.py
    ```
The detector will write to `/tmp/bruteforce_alert.log`, and the notifier will send a desktop pop-up the moment new alerts appear.

---

### EXAMPLES
* Receive an instant pop-up notification when someone tries to guess your password.
* Monitor a server for malicious login attempts without constantly checking logs.
* Protect your privacy by only allowing the notifier script to do its one job—displaying a notification.
