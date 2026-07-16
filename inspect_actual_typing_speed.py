import csv
import json

high_typing_speed = []
with open("transcription_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        is_edited = row["is_edited"].strip().lower() in ("true", "yes", "1")
        try:
            time_taken = float(row["time_taken_by_user"])
            duration = float(row["duration"])
        except ValueError:
            continue
            
        if is_edited and time_taken > 0:
            char_count = len(row["user_text"].replace(" ", ""))
            actual_speed = char_count / time_taken
            
            # Find cases where the user typed > 15 chars/sec AND they had to type a decent amount (e.g. > 10 chars)
            if actual_speed > 15.0 and char_count > 10 and len(high_typing_speed) < 50:
                high_typing_speed.append({
                    "user_id": row["user_id"],
                    "duration": duration,
                    "time_taken": time_taken,
                    "whisper_text": row["whisper_text"],
                    "user_text": row["user_text"],
                    "char_count": char_count,
                    "actual_typing_speed": actual_speed
                })

with open("high_typing_speed.json", "w", encoding="utf-8") as f:
    json.dump(high_typing_speed, f, indent=2)

print(f"Found {len(high_typing_speed)} high typing speed tasks!")
