# Python Log Analyzer

This is a beginner-level cybersecurity project in Python.  
It simulates login activity, generates logs automatically, and detects possible brute-force attacks.

---

## Project Files

1. `log_generator.py` → Generates simulated login logs (failed + successful attempts)  
2. `log_analyzer.py` → Analyzes the logs and identifies possible brute-force attacks  
3. `README.md` → Project documentation  

---

## How to Run

1. Run `log_generator.py` first  
   - This will create `generated_logs.txt` automatically  

2. Run `log_analyzer.py`  
   - This reads `generated_logs.txt` and prints:  
     - All failed login attempts  
     - Possible brute-force attack IPs  

---

## Learning Outcome

- Python file handling  
- Using dictionaries to count occurrences  
- Understanding brute-force attack detection  
- Beginner cybersecurity concepts  

---

## Future Improvements

- Track top 3 IPs with most failed attempts  
- Add a timestamp window to detect rapid attacks  
- Create a simple GUI or web interface to display logs dynamically  

