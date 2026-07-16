import csv
import json

fast_edits = []
with open("transcription_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        is_edited = row["is_edited"].strip().lower() in ("true", "yes", "1")
        try:
            char_sec = float(row["segment_character_per_second"])
            time_taken = float(row["time_taken_by_user"])
            duration = float(row["duration"])
        except ValueError:
            continue
            
        if is_edited and char_sec > 25.0 and len(fast_edits) < 50:
            fast_edits.append({
                "user_id": row["user_id"],
                "duration": duration,
                "time_taken": time_taken,
                "whisper_text": row["whisper_text"],
                "user_text": row["user_text"],
                "segment_character_per_second": char_sec
            })

with open("fast_edits.json", "w", encoding="utf-8") as f:
    json.dump(fast_edits, f, indent=2)

print(f"Found {len(fast_edits)} fast edits!")
