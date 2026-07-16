import csv
import json

edited_rushed = []
with open("transcription_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        is_edited = row["is_edited"].strip().lower() in ("true", "yes", "1")
        try:
            time_taken = float(row["time_taken_by_user"])
        except ValueError:
            time_taken = 0.0
        try:
            duration = float(row["duration"])
        except ValueError:
            duration = 0.0
            
        if is_edited and duration > 3.0 and time_taken > 0 and time_taken < 2.0 and len(edited_rushed) < 50:
            edited_rushed.append({
                "user_id": row["user_id"],
                "duration": duration,
                "time_taken": time_taken,
                "is_edited": row["is_edited"],
                "whisper_text": row["whisper_text"],
                "user_text": row["user_text"],
                "segment_character_per_second": float(row["segment_character_per_second"]) if row["segment_character_per_second"] else 0.0
            })

with open("edited_rushed_samples.json", "w", encoding="utf-8") as f:
    json.dump(edited_rushed, f, indent=2)

print("Samples written to edited_rushed_samples.json")
