import re
import os

def analyze_log_file(filename="access.log"):
    try:
        with open(access.log, "r") as file:
            log_lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: Log file '{filename}' not found.")
        return

    error_count = 0
    unique_ipdress = set()
    url_count = {}

    for lines in log_lines:
        timestamp, ip, url, status_code = extract_log_data()
        if ip and url and status_code:
            unique_ipdress.add(ip)
            url_count[url] = url_count.get(url, 0) + 1
            if status_code >= 400:
                error_count += 1

    print(f"Total Errors: {error_count}")
    print(f"Unique IP Addresses: {len(unique_ipdress)}")
    print("URL Access Counts:")
    for url, count in url_count.items():
        print(f"    {url}: {count}")

def extract_log_data(line):
    match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \"GET (.+) HTTP/1.1\" (\d+)", line)
    if match:
        timestamp, ip, url, status_code = match.groups()
        return timestamp, ip, url, status_code
    else:
        return None, None, None, None

generate_log_file()
analyze_log_file()