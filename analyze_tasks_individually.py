import csv
import numpy as np

total_tasks = 0
exact_matches = 0
rushed = 0
extremely_rushed = 0
very_short_time = 0
edited_count = 0
speeds = []
ratios = []

with open("transcription_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_tasks += 1
        whisper_text = row["whisper_text"].strip()
        user_text = row["user_text"].strip()
        is_edited = row["is_edited"].strip().lower() in ("true", "yes", "1")
        
        try:
            duration = float(row["duration"])
        except ValueError:
            duration = 0.0
            
        try:
            time_taken = float(row["time_taken_by_user"])
        except ValueError:
            time_taken = 0.0
            
        try:
            char_sec = float(row["segment_character_per_second"])
        except ValueError:
            char_sec = 0.0
            
        if user_text == whisper_text:
            exact_matches += 1
            
        if is_edited:
            edited_count += 1
            
        if duration > 0:
            ratio = time_taken / duration
            ratios.append(ratio)
            if time_taken < duration:
                rushed += 1
            if time_taken < 0.5 * duration:
                extremely_rushed += 1
                
        if time_taken < 2.0:
            very_short_time += 1
            
        speeds.append(char_sec)

print(f"Total Tasks: {total_tasks}")
print(f"Exact Matches (whisper == user): {exact_matches} ({exact_matches/total_tasks:.2%})")
print(f"Is Edited = True: {edited_count} ({edited_count/total_tasks:.2%})")
print(f"Rushed (time_taken < duration): {rushed} ({rushed/total_tasks:.2%})")
print(f"Extremely Rushed (time_taken < 0.5 * duration): {extremely_rushed} ({extremely_rushed/total_tasks:.2%})")
print(f"Very Short Time (<2s): {very_short_time} ({very_short_time/total_tasks:.2%})")

# Percentiles of speed and ratio
print("\n--- Percentiles of time_taken_by_user / duration ---")
for p in [1, 5, 10, 25, 50, 75, 90, 95, 99]:
    print(f"{p}th percentile: {np.percentile(ratios, p):.4f}")

print("\n--- Percentiles of segment_character_per_second ---")
for p in [1, 5, 10, 25, 50, 75, 90, 95, 99]:
    print(f"{p}th percentile: {np.percentile(speeds, p):.4f}")
