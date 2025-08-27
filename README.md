# Project Overview: Vigilant Security System
A robust and vigilant security solution that detects unauthorized login attempts on your computer and instantly notifies you, ensuring your system's safety.

---

## The Problem It Solves
System security restrictions prevent a single program from both accessing sensitive logs and displaying user notifications, creating a challenge for real-time monitoring and alerting.

---

## Our Solution
By intelligently splitting responsibilities:
- A **privileged "watcher"** securely reads system logs.
- An **unprivileged "notifier"** delivers timely alerts to the user.

This modular approach ensures both security and functionality, keeping your system protected without compromising performance.

---

## Installation Guide
Follow these steps to set up the system:

1. **Install Core Libraries**  
   Install essential system libraries, such as `python3-dbus`, for seamless communication between components.  
   **Command**:  
   ```bash
   sudo apt update
   sudo apt install python3-dbus
   ```
   *Note*: Ensure you have `apt` (or your package manager, e.g., `yum` or `dnf` for other distributions) installed. This command is for Debian/Ubuntu-based systems.

2. **Set Up a Virtual Environment**  
   Create a virtual environment to manage dependencies efficiently and avoid conflicts.  
   **Commands**:  
   ```bash
   python3 -m venv vigilant_env
   source vigilant_env/bin/activate
   ```
   *Note*: Replace `vigilant_env` with your preferred environment name. The `source` command activates the environment.

3. **Install Python Packages**  
   Use the provided `requirements.txt` file to install all necessary Python dependencies.  
   **Command**:  
   ```bash
   pip install -r requirements.txt
   ```
   *Note*: Ensure the `requirements.txt` file is in your project directory. Create it if needed, listing dependencies like `python-dotenv`.

4. **Configure Settings**  
   Create a `.env` file to customize your system settings for optimal performance.  
   **Commands**:  
   ```bash
   touch .env
   nano .env
   ```
   *Note*: Add necessary variables (e.g., `LOG_PATH=/var/log/auth.log` or notification settings) in the `.env` file. Save and exit the editor.

---

## Usage Instructions
1. **Launch the Detector**  
   Run the privileged detector script with `sudo` in one terminal to monitor system logs.  
   **Command**:  
   ```bash
   sudo python3 detector.py
   ```

2. **Start the Notifier**  
   In a separate terminal, run the unprivileged notifier script to enable alerts.  
   **Command**:  
   ```bash
   python3 notifier.py
   ```

3. **Real-Time Monitoring**  
   The detector writes events to a temporary file, and the notifier delivers pop-up notifications to keep you informed.

---

## Use Case Examples
- **Instant Alerts**: Receive immediate pop-up notifications when an unauthorized login attempt is detected, keeping you one step ahead of potential threats.
- **Server Monitoring**: Continuously monitor servers for malicious login attempts without the need to manually check logs.
- **Privacy Protection**: Ensure privacy by limiting the notifier script to its single task of sending alerts, minimizing unnecessary access.

