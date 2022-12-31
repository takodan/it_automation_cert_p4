#!/usr/bin/env python3

#system health check

from time import sleep
import psutil
import socket
import emails
import os

def cpu_usage_error():
    # Report an error if CPU usage is over 80%
    cpu = psutil.cpu_percent(interval = 1)
    threshold = 80 # 80%
    print("cpu_usage: {}".format(cpu))
    if cpu >= threshold:
        return True
    else:
        return False


def memory_usage_error():
    # Report an error if available memory is less than 500MB
    mem = psutil.virtual_memory()
    threshold = 500 * 1024 * 1024  # 500MB
    print("memory_usage: {}".format(mem.available))
    if mem.available <= threshold:
        return True
    else:
        return False


def disk_usage_error():
    # Report an error if available disk space is lower than 20%
    disk = psutil.disk_usage("/")
    threshold = 100-20 # more then 80%
    print("disk_usage: {}".format(disk.percent))
    if disk.percent >= threshold:
        return True
    else:
        return False


def localhost_ip():
    # Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
    host_ip = socket.gethostbyname("localhost")
    print("localhost_ip: {}".format(host_ip))
    if host_ip != "127.0.0.1":
        return True
    else:
        return False

def send_error_email(error_message):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = error_message
    body = "Please check your system and resolve the issue as soon as possible."

    message = emails.geberate_no_attachment(sender, receiver, subject, body)
    emails.send(message)


def main():
    # while True:
        if cpu_usage_error():
            print("Error - CPU usage is over 80%")
            send_error_email("Error - CPU usage is over 80%")

        if memory_usage_error():
            print("Error - Available memory is less than 500MB")
            send_error_email("Error - Available memory is less than 500MB")

        if disk_usage_error():
            print("Error - Available disk space is less than 20%")
            send_error_email("Error - Available disk space is less than 20%")

        if localhost_ip():
            print("Error - localhost cannot be resolved to 127.0.0.1")
            send_error_email("Error - localhost cannot be resolved to 127.0.0.1")

        # sleep(60)





if __name__ == "__main__":
    main()