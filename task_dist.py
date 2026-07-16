import json
from collections import Counter

with open("report.json", "r", encoding="utf-8") as f:
    report = json.load(f)

profiles = report["profiles"]
task_counts = [meta["total_tasks"] for uid, meta in profiles]
dist = Counter(task_counts)
print("Task count distribution:")
for count in sorted(dist.keys()):
    print(f"Users with {count} tasks: {dist[count]}")
