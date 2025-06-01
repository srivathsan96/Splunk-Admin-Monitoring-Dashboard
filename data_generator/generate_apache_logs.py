import random
import time
import faker
from datetime import datetime, timedelta

# Initialize Faker and seed for consistent results
fak = faker.Faker()
random.seed(42)

# Define the output log file name
output_file = "apache_logs.log"

# Time range for log timestamps
start_date = datetime(2023, 1, 1, 0, 0, 0)
end_date = datetime(2025, 5, 24, 23, 59, 59)

# HTTP request methods, API endpoints, status codes
methods = ['GET', 'POST', 'PUT', 'DELETE']
endpoints = ['/usr', '/usr/admin', '/usr/admin/developer', '/usr/login', '/usr/register']
status_codes = ['200', '303', '304', '403', '404', '500', '502']
usernames = ['james', 'adam', 'eve', 'alex', 'smith', 'isabella', 'david', 'angela', 'donald', 'hilary']

# Simulated browser/device user-agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Mozilla/5.0 (Android 10; Mobile; rv:84.0) Gecko/84.0 Firefox/84.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 Safari/7046A194A',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_9 like Mac OS X) AppleWebKit/605.1.15 Safari/604.1'
]

# Referrers: "-" (none) or fake site
referrers = ['-', fak.uri()]

# Define suspicious IP that will be used to simulate brute-force or malicious POST/PUT attempts
suspicious_ip = "192.168.1.100"

# Generate a random datetime within a range
def random_datetime(start, end):
    delta = end - start
    random_sec = random.randint(0, int(delta.total_seconds()))
    return (start + timedelta(seconds=random_sec)).strftime('%d/%b/%Y:%H:%M:%S +0530')

# Open file for writing
with open(output_file, "w") as f:

    # --- 1. Normal Entries: simulate regular web traffic ---
    for _ in range(150000):
        f.write('%s - - [%s] "%s %s HTTP/1.0" %s %d "%s" "%s" %d\n' % (
            fak.ipv4(),  # client IP
            random_datetime(start_date, end_date),  # timestamp
            random.choice(methods),  # GET, POST, etc.
            random.choice(endpoints),  # URI
            random.choice(status_codes),  # HTTP status
            int(random.gauss(5000, 300)),  # response size (bytes)
            random.choice(referrers),  # referrer
            random.choice(user_agents),  # browser/device
            random.randint(100, 6000)  # response time (ms)
        ))

    # --- 2. Simulated Suspicious Behavior: high-volume POST/PUT with 5xx errors from same IP ---
    for _ in range(25000):
        f.write('%s - - [%s] "%s %s HTTP/1.0" %s %d "%s" "%s" %d\n' % (
            suspicious_ip,
            random_datetime(start_date, end_date),
            random.choice(['POST', 'PUT']),
            random.choice(['/usr/login', '/usr/admin']),
            random.choice(['500', '502']),  # server errors
            int(random.gauss(5000, 200)),  # response size
            '-',  # no referrer
            random.choice(user_agents),
            random.randint(2000, 10000)  # high response time for failures
        ))

    # --- 3. High Traffic IPs: simulate top clients for `top clientip` panels ---
    top_ips = [fak.ipv4() for _ in range(10)]
    for ip in top_ips:
        for _ in range(1000):
            f.write('%s - - [%s] "%s %s HTTP/1.0" %s %d "%s" "%s" %d\n' % (
                ip,
                random_datetime(start_date, end_date),
                random.choice(['GET', 'POST']),
                random.choice(endpoints),
                random.choice(status_codes),
                int(random.gauss(4500, 150)),
                '-',
                random.choice(user_agents),
                random.randint(300, 5000)
            ))

print(f"[✓] Apache logs written to '{output_file}' successfully.")
