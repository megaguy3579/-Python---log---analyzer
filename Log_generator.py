# ----------------------------------
# Log Generator
# Simulates login attempts
# ----------------------------------

import random
from datetime import datetime, timedelta

LOG_FILE = "generated_logs.txt"

ips = [
    "192.168.1.10",
    "192.168.1.11",
    "192.168.1.12",
    "10.0.0.5",
    "172.16.0.3"
]

statuses = ["SUCCESS", "FAILED"]

start_time = datetime.now()

with open(LOG_FILE, "w") as file:
    for i in range(20):
        time_stamp = start_time + timedelta(seconds=i * 30)
        date = time_stamp.strftime("%Y-%m-%d")
        time = time_stamp.strftime("%H:%M:%S")

        ip = random.choice(ips)

        # Simulate brute force from one IP
        if ip == "192.168.1.10":
            status = "FAILED"
        else:
            status = random.choice(statuses)

        file.write(f"{date} {time} {ip} {status}\n")

print("✅ Logs generated successfully in generated_logs.txt")
