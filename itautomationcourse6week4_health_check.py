#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails
import time

def check_system():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent()
    if cpu_usage > 80:
        subject = "Error - CPU usage is over 80%"
        body = "Please check your system, CPU usage is over 80%."

        emails.send_email("automation@example.com", "student-01-79c6ce800f3c@example.com", subject, body)

    # Check disk space
    disk_usage = shutil.disk_usage("/")
    disk_space_percent = disk_usage.free / disk_usage.total * 100
    if disk_space_percent < 20:
        subject = "Error - Available disk space is less than 20%"
        body = "Please check your system, available disk space is less than 20%."

        emails.send_email("automation@example.com", "student-01-79c6ce800f3c@example.com", subject, body)

    # Check available memory
    available_memory = psutil.virtual_memory().available / (1024 * 1024)
    if available_memory < 500:
        subject = "Error - Available memory is less than 500MB"
        body = "Please check your system, available memory is less than 500MB."

        emails.send_email("automation@example.com", "student-01-79c6ce800f3c@example.com", subject, body)

    # Check hostname resolution
    try:
        socket.gethostbyname("localhost")
    except socket.error:
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        body = "Please check your system, hostname 'localhost' cannot be resolved to '127.0.0.1'."

        emails.send_email("automation@example.com", "student-01-79c6ce800f3c@example.com", subject, body)

if __name__ == "__main__":
    check_system()
