PROJECT OVERVIEW

A vigilant security system that detects and notifies you of unauthorized login attempts on your computer.
THE PROBLEM IT ADDRESSES
System security prevents a single program from accessing sensitive logs and displaying user notifications.
THE APPROACH TO SOLVING THE PROBLEM
By splitting duties, a privileged "watcher" reads logs while an unprivileged "notifier" sends alerts.
INSTALLATION
 * First, install core system libraries like python3-dbus for seamless communication.
 * Next, set up a virtual environment to manage dependencies neatly.
 * Then, install the necessary Python packages using the requirements file.
 * Finally, configure your settings by creating a .env file.
USAGE
 * Start the privileged detector script with sudo in one terminal.
 * Then, run the unprivileged notifier script in a separate window.
 * The detector now writes to a temporary file, and the notifier sends a pop-up.
EXAMPLES
 * Get an instant pop-up notification the moment someone tries to hack your computer.
 * Monitor a server for malicious login attempts without constantly checking logs.
 * Protect your privacy by only allowing the notifier script to do its one job.
