import csv
from collections import defaultdict
import json

users = defaultdict(lambda: {
    "total_tasks": 0,
    "edited_tasks": 0,
    "total_duration": 0.0,
    "total_time_taken": 0.0,
    "rushed_tasks": 0,       # time_taken_by_user < duration
    "extremely_rushed": 0,   # time_taken_by_user < 0.5 * duration
    "exact_matches": 0,      # user_text == whisper_text
    "total_chars": 0,
    "total_char_sec": 0.0,
    "whisper_empty": 0,
    "user_empty": 0,
    "tasks_with_very_short_time": 0 # time_taken_by_user < 2 seconds
})

with open("transcription_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        user_id = row["user_id"]
        whisper_text = row["whisper_text"]
        user_text = row["user_text"]
        is_edited = row["is_edited"]
        
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
            
        u = users[user_id]
        u["total_tasks"] += 1
        u["total_duration"] += duration
        u["total_time_taken"] += time_taken
        u["total_chars"] += len(user_text.replace(" ", ""))
        u["total_char_sec"] += char_sec
        
        # Check if edited
        is_ed_bool = is_edited.strip().lower() in ("true", "yes", "1")
        if is_ed_bool:
            u["edited_tasks"] += 1
            
        if user_text.strip() == whisper_text.strip():
            u["exact_matches"] += 1
            
        if time_taken < duration:
            u["rushed_tasks"] += 1
            
        if time_taken < 0.5 * duration:
            u["extremely_rushed"] += 1
            
        if time_taken < 2.0:
            u["tasks_with_very_short_time"] += 1
            
        if not whisper_text.strip():
            u["whisper_empty"] += 1
            
        if not user_text.strip():
            u["user_empty"] += 1

# Compile user profiles
profiles = {}
for uid, u in users.items():
    tot = u["total_tasks"]
    if tot == 0:
        continue
    profiles[uid] = {
        "total_tasks": tot,
        "edited_rate": u["edited_tasks"] / tot,
        "exact_match_rate": u["exact_matches"] / tot,
        "avg_duration": u["total_duration"] / tot,
        "avg_time_taken": u["total_time_taken"] / tot,
        "rushed_rate": u["rushed_tasks"] / tot,
        "extremely_rushed_rate": u["extremely_rushed"] / tot,
        "short_time_rate": u["tasks_with_very_short_time"] / tot,
        "avg_char_sec": u["total_char_sec"] / tot,
        "whisper_empty_rate": u["whisper_empty"] / tot,
        "user_empty_rate": u["user_empty"] / tot,
    }

# Sort profiles by total tasks to see the most active users first
sorted_profiles = sorted(profiles.items(), key=lambda x: x[1]["total_tasks"], reverse=True)

report = {
    "num_users": len(profiles),
    "total_tasks_all_users": sum(u["total_tasks"] for u in users.values()),
    "profiles": sorted_profiles
}

with open("report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2)

print("Analysis done! Written to report.json")
