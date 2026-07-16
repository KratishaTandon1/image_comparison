import csv
import json

rushed_samples = []
with open("transcription_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            time_taken = float(row["time_taken_by_user"])
        except ValueError:
            time_taken = 0.0
            
        try:
            duration = float(row["duration"])
        except ValueError:
            duration = 0.0
            
        try:
            char_sec = float(row["segment_character_per_second"])
        except ValueError:
            char_sec = 0.0
            
        is_edited = row["is_edited"].strip().lower() in ("true", "yes", "1")
        if time_taken > 0 and time_taken < 2.0 and len(rushed_samples) < 50:
            rushed_samples.append({
                "user_id": row["user_id"],
                "duration": duration,
                "time_taken": time_taken,
                "is_edited": row["is_edited"],
                "whisper_text": row["whisper_text"],
                "user_text": row["user_text"],
                "segment_character_per_second": char_sec
            })

with open("rushed_samples.json", "w", encoding="utf-8") as f:
    json.dump(rushed_samples, f, indent=2)

print("Samples written to rushed_samples.json")
