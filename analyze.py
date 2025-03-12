
#### **analyze.py**
```python
import sys
from collections import Counter

def analyze_logs(filename):
    with open(filename, 'r') as f:
        logs = f.readlines()

    error_counter = Counter(line.split()[0] for line in logs if "error" in line.lower())
    for error, count in error_counter.most_common(5):
        print(f"Frequent Error: {error} - {count} occurrences")

if len(sys.argv) > 1:
    analyze_logs(sys.argv[1])
else:
    print("Usage: python analyze.py <logfile>")
