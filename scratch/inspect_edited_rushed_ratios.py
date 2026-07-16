import csv

rushed_edited_count = 0
total_edited = 0
ratios = []

with open("transcription_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        is_edited = row["is_edited"].strip().lower() in ("true", "yes", "1")
        if is_edited:
            total_edited += 1
            try:
                time_taken = float(row["time_taken_by_user"])
                duration = float(row["duration"])
            except ValueError:
                continue
                
            if duration > 0:
                ratio = time_taken / duration
                ratios.append(ratio)
                if time_taken < duration:
                    rushed_edited_count += 1

print(f"Total edited tasks: {total_edited}")
print(f"Rushed edited tasks (time < duration): {rushed_edited_count} ({rushed_edited_count / total_edited:.2%})")
if ratios:
    import numpy as np
    print("Percentiles of ratio for edited tasks:")
    for p in [1, 5, 10, 25, 50, 75, 90]:
        print(f"  {p}th: {np.percentile(ratios, p):.4f}")
