# ----------------------------------
# Python Log Analyzer
# Detects brute force attacks
# ----------------------------------

from collections import defaultdict

LOG_FILE = "generated_logs.txt"
BRUTE_FORCE_LIMIT = 3

failed_attempts = defaultdict(int)

print("🔍 Waiting for logs...\n")

try:
    with open(LOG_FILE, "r") as file:
        for line in file:
            parts = line.strip().split()

            date = parts[0]
            time = parts[1]
            ip_address = parts[2]
            status = parts[3]

            if status == "FAILED":
                failed_attempts[ip_address] += 1
                print(f"❌ Failed login from {ip_address} on {date} at {time}")

    print("\n🚨 Possible Brute Force Attacks:\n")

    for ip, count in failed_attempts.items():
        if count >= BRUTE_FORCE_LIMIT:
            print(f"⚠️ ALERT: {ip} has {count} failed login attempts")

except FileNotFoundError:
    print("⚠️ Log file not found. Run log_generator.py first.")
