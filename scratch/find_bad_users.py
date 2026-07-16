import json

with open("report.json", "r", encoding="utf-8") as f:
    report = json.load(f)

profiles = report["profiles"]

print("Total users:", len(profiles))
active_profiles = [p for p in profiles if p[1]["total_tasks"] >= 5]
print("Users with >= 5 tasks:", len(active_profiles))
active_profiles_10 = [p for p in profiles if p[1]["total_tasks"] >= 10]
print("Users with >= 10 tasks:", len(active_profiles_10))

# Print top 20 active users
print("\nTop 20 most active users:")
for uid, meta in active_profiles[:20]:
    print(f"User {uid}: tasks={meta['total_tasks']}, edit_rate={meta['edited_rate']:.2f}, match_rate={meta['exact_match_rate']:.2f}, rushed_rate={meta['rushed_rate']:.2f}, extreme_rushed={meta['extremely_rushed_rate']:.2f}, avg_time={meta['avg_time_taken']:.1f}s, avg_dur={meta['avg_duration']:.1f}s")

print("\nChecking for potential low-quality patterns among users with >= 5 tasks:")

# Pattern 1: Rushing (extremely high rushed rate, e.g., > 80% tasks rushed, meaning time_taken < duration)
rushed_users = [p for p in active_profiles if p[1]["rushed_rate"] > 0.8]
print(f"Pattern 1 (Rushing - >80% tasks completed in less than audio duration): {len(rushed_users)} users")
for uid, meta in rushed_users[:10]:
    print(f"  User {uid}: tasks={meta['total_tasks']}, rushed_rate={meta['rushed_rate']:.2f}, avg_time={meta['avg_time_taken']:.1f}s, avg_dur={meta['avg_duration']:.1f}s")

# Pattern 2: No Editing (exact match rate = 100%, and edited_rate = 0%, meaning they just submit whisper_text every time)
no_edit_users = [p for p in active_profiles if p[1]["exact_match_rate"] == 1.0 and p[1]["total_tasks"] >= 5]
print(f"Pattern 2 (No Editing - 100% exact matches with whisper_text on >=5 tasks): {len(no_edit_users)} users")
for uid, meta in no_edit_users[:10]:
    print(f"  User {uid}: tasks={meta['total_tasks']}, avg_time={meta['avg_time_taken']:.1f}s")

# Pattern 3: High speed (segment_character_per_second is very high, e.g., > 30 chars/second)
fast_users = [p for p in active_profiles if p[1]["avg_char_sec"] > 25]
print(f"Pattern 3 (High char/sec speed - >25 chars/sec average): {len(fast_users)} users")
for uid, meta in fast_users[:10]:
    print(f"  User {uid}: tasks={meta['total_tasks']}, avg_char_sec={meta['avg_char_sec']:.1f}, avg_time={meta['avg_time_taken']:.1f}s")
