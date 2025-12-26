
## Project files
- `Log_generator.py` — Generates simulated login logs (creates `generated_logs.txt`)  
- `Log_analyzer.py` — Analyzes `generated_logs.txt` and reports failed attempts and possible brute-force IPs  
- `README.md` — This file

> Note: Filenames are case-sensitive on some systems. Use the exact names above when running the scripts.

---

## Prerequisites
- Python 3.7+  
- No external packages required

---

## How to run
1. Generate logs:
   - Linux / macOS / Windows:
     ```
     python3 Log_generator.py
     ```
     or
     ```
     python Log_generator.py
     ```
   This writes `generated_logs.txt` to the repository folder.

2. Analyze logs:
   ```
   python3 Log_analyzer.py
   ```
   or
   ```
   python Log_analyzer.py
   ```

---

## Expected log format
Each line in `generated_logs.txt` is whitespace-separated with 4 fields:
```
YYYY-MM-DD HH:MM:SS <IP_ADDRESS> <STATUS>
```
Example:
```
2025-12-24 10:10:00 203.0.113.5 FAILED
```

---

## Example generated_logs.txt (sample)
```
2025-12-24 09:58:01 192.168.1.10 SUCCESS
2025-12-24 09:59:12 203.0.113.5 FAILED
2025-12-24 10:00:05 198.51.100.23 FAILED
2025-12-24 10:01:22 203.0.113.5 SUCCESS
2025-12-24 10:02:35 198.51.100.23 FAILED
2025-12-24 10:03:50 10.0.0.5 SUCCESS
```

---

## Example output from Log_analyzer.py
```
📄 Reading logs...

❌ Failed login from 203.0.113.5 on 2025-12-24 at 09:59:12
❌ Failed login from 198.51.100.23 on 2025-12-24 at 10:00:05
❌ Failed login from 198.51.100.23 on 2025-12-24 at 10:02:35

🚨 Possible Brute Force Attacks: None found
```

If an IP reaches the brute force threshold (default 3), alerts will be shown:
```
⚠️ ALERT: 203.0.113.5 has 3 failed login attempts
```

---

## Configuration
- LOG file path is set inside both scripts as:
  - `LOG_FILE = "generated_logs.txt"`
- Brute-force threshold in `Log_analyzer.py`:
  - `BRUTE_FORCE_LIMIT = 3`
You can edit these constants directly or add CLI flags if you prefer.

---

## Known issues (original repo)
- `Log_analyzer.py` assumes every line has 4 whitespace-separated fields. Blank or malformed lines may cause an IndexError and crash the script.
- Status comparison is case-sensitive (`"FAILED"`). `failed` or `Failed` will not be counted in the original version.
- `Log_analyzer.py` prints "Waiting for logs..." but only reads the file once (not a live tail). That message can be misleading.
- README originally referenced lowercase filenames while the repo uses capitalized filenames; this README uses the actual filenames present in the repo.

---

## Recommended improvements
- Make `Log_analyzer.py` tolerant to malformed lines (skip and warn rather than crash).
- Use case-insensitive comparison for `status` (e.g., `status.upper()`).
- Only print the "Possible Brute Force Attacks" header if there are alerts, or print "None found"
- Implement a sliding time window (e.g., X failed attempts within Y seconds) to detect rapid attacks more accurately.
- Replace prints with Python `logging` for configurable verbosity.
- Add unit tests for parsing and detection logic.

---

## Contribution
Pull requests and suggestions are welcome. If you want, I can prepare a patch that:
- makes `Log_analyzer.py` more robust,
- normalizes filenames in examples,
- and adds CLI flags.

