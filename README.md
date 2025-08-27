# Brute-Force Attack Detector

## Project Overview

This is a **vigilant security solution** designed to detect unauthorized SSH login attempts on your computer and notify you instantly. It's a proactive tool that helps you stay ahead of potential threats by providing real-time alerts.

-----

## The Problem It Solves

Traditional security models often face a challenge: a single program is typically not granted both the high-level system permissions needed to access sensitive logs and the low-level user permissions required to display desktop notifications. This project provides an elegant solution to this problem by splitting these two responsibilities.

-----

## Our Solution

The solution is a **modular, two-part system** that ensures both security and functionality.

  * **The Privileged "Watcher" (`bruteforce_detector.py`)**: This script runs with elevated privileges (`sudo`) and securely reads system logs, specifically the `systemd.journal`, to identify failed SSH login attempts. \* **The Unprivileged "Notifier" (`notifier.py`)**: This script runs with standard user permissions. It monitors a temporary alert file for new entries and, upon detecting one, sends a desktop pop-up notification.

This intelligent separation of duties ensures each script operates with the **principle of least privilege**, minimizing security risks while providing effective real-time monitoring.

-----

## Installation Guide

Follow these steps to set up the system.

### 1\. Install Core System Libraries

First, install essential system libraries for seamless communication between components. For Debian/Ubuntu-based systems, use the following command:

```bash
sudo apt update
sudo apt install python3-dbus
```

### 2\. Set Up a Virtual Environment

It's recommended to create a dedicated virtual environment to manage dependencies efficiently and avoid conflicts.

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3\. Install Python Packages

Use the provided `requirements.txt` file to install all necessary Python dependencies. [cite\_start]The required packages are `python-dotenv`, `systemd-python`, `plyer`, and `watchdog`. [cite: 3]

```bash
pip install -r requirements.txt
```

### 4\. Configure Your Settings

The project uses a `.env` file for customizable settings. [cite\_start]A template, `.env.example`, is provided to show you the required variables, such as `ALERT_FILE_PATH` and `ATTEMPT_THRESHOLD`. [cite: 1]

```bash
cp .env.example .env
nano .env
```

Modify the values in the newly created `.env` file as needed.

-----

## Usage Instructions

This project uses two separate scripts that must be run concurrently in different terminals.

### 1\. Launch the Privileged Detector

Open a terminal and run the `bruteforce_detector.py` script with `sudo` to grant it the necessary permissions to read system logs.

```bash
sudo python3 bruteforce_detector.py
```

This script will monitor the system journal for failed SSH password attempts.

### 2\. Start the Unprivileged Notifier

In a **separate terminal**, run the `notifier.py` script as a normal user. It will monitor the temporary alert file and send desktop notifications.

```bash
python3 notifier.py
```

The detector will write to `/tmp/bruteforce_alert.log`, and the notifier will deliver a desktop pop-up the moment new alerts appear. [cite\_start]This temporary alert file is configured to be ignored by Git to prevent it from being committed to the repository. [cite: 2]

-----

## Use Case Examples

  * **Instant Alerts**: Receive immediate pop-up notifications when an unauthorized login attempt is detected, keeping you one step ahead of potential threats.
  * **Server Monitoring**: Continuously monitor a server for malicious login attempts without the need to manually check logs.
  * **Privacy Protection**: Ensure privacy by limiting the notifier script to its single task of sending alerts, minimizing unnecessary access.
