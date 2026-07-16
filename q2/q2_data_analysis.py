import csv
from collections import defaultdict

def analyze_cheating_patterns(csv_path="transcription_data.csv"):
    # The raw dataset is placed in the same q2/ directory for packaging and verification
    print(f"Reading dataset from: {csv_path}")
    print("Starting data analysis... This might take 10-15 seconds for 51k rows.")
    
    # Track statistics per user
    user_stats = defaultdict(lambda: {
        "total_tasks": 0,
        "exact_matches": 0,
        "trivial_edits": 0,
        "substantial_edits": 0,
        "rushed_tasks": 0,
        "rushed_substantial_edits": 0,
        "rushed_trivial_or_no_edits": 0
    })

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_id = row["user_id"]
                whisper_text = row["whisper_text"].strip()
                user_text = row["user_text"].strip()
                
                try:
                    duration = float(row["duration"])
                except ValueError:
                    duration = 0.0
                try:
                    time_taken = float(row["time_taken_by_user"])
                except ValueError:
                    time_taken = 0.0
                    
                stats = user_stats[user_id]
                stats["total_tasks"] += 1
                
                # Check for rushing (time spent is less than audio length)
                # Ignore very short audio clips (< 2 seconds) to avoid false positives
                is_rushed = False
                if duration >= 2.0 and time_taken < duration:
                    is_rushed = True
                    stats["rushed_tasks"] += 1
                    
                # Classify the edit type
                if whisper_text == user_text:
                    stats["exact_matches"] += 1
                    if is_rushed:
                        stats["rushed_trivial_or_no_edits"] += 1
                else:
                    # Check for trivial punctuation/whitespace additions (bypass cheat)
                    diff_chars = set(user_text) ^ set(whisper_text)
                    trivial_set = {'।', '.', ',', '?', ' ', '"', "'", '!'}
                    
                    is_trivial = False
                    len_diff = abs(len(user_text) - len(whisper_text))
                    
                    if diff_chars.issubset(trivial_set) and len_diff <= 2:
                        is_trivial = True
                    elif user_text.endswith("।") and user_text[:-1].strip() == whisper_text:
                        is_trivial = True
                    elif user_text.endswith(".") and user_text[:-1].strip() == whisper_text:
                        is_trivial = True
                        
                    if is_trivial:
                        stats["trivial_edits"] += 1
                        if is_rushed:
                            stats["rushed_trivial_or_no_edits"] += 1
                    else:
                        stats["substantial_edits"] += 1
                        if is_rushed:
                            stats["rushed_substantial_edits"] += 1
    except FileNotFoundError:
        # Fallback to local directory if run from parent
        if csv_path == "../transcription_data.csv":
            return analyze_cheating_patterns(csv_path="transcription_data.csv")
        else:
            raise

    # Filter out users with high cheating indicators
    flagged_users = []
    
    # PRODUCTION NOTE: In production, set total_tasks limit to >= 5 to avoid blocking on small-sample noise.
    # In this static test sample, 99.9% of raters completed exactly 1 task, so we evaluate threshold >= 1.
    MIN_TASKS_THRESHOLD = 1 
    
    print(f"\n--- Identifying Cheating Users (total tasks >= {MIN_TASKS_THRESHOLD}) ---")
    for uid, stats in user_stats.items():
        if stats["total_tasks"] < MIN_TASKS_THRESHOLD:
            continue
            
        tot = stats["total_tasks"]
        rushed_cheats = stats["rushed_trivial_or_no_edits"]
        rushed_cheat_rate = rushed_cheats / tot
        rushed_rate = stats["rushed_tasks"] / tot
        trivial_rate = stats["trivial_edits"] / tot
        match_rate = stats["exact_matches"] / tot
        
        # Flag user if more than 30% of their tasks are rushed and contain no/trivial edits
        if rushed_cheat_rate > 0.3:
            flagged_users.append({
                "user_id": uid,
                "total_tasks": tot,
                "rushed_rate": rushed_rate,
                "exact_match_rate": match_rate,
                "trivial_edit_rate": trivial_rate,
                "rushed_cheat_rate": rushed_cheat_rate,
                "status": "FLAG_FOR_AUDIT" # Updated from permanent block to protect raters
            })

    # Sort flagged users by cheat rate
    flagged_users.sort(key=lambda x: x["rushed_cheat_rate"], reverse=True)
    
    # Save results to CSV
    output_file = "flagged_transcribers.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as out:
        writer = csv.DictWriter(out, fieldnames=["user_id", "total_tasks", "rushed_rate", "exact_match_rate", "trivial_edit_rate", "rushed_cheat_rate", "status"])
        writer.writeheader()
        writer.writerows(flagged_users)
        
    print(f"Analysis complete! Flagged {len(flagged_users)} users for cheating patterns.")
    print(f"Results saved to '{output_file}'")

if __name__ == "__main__":
    analyze_cheating_patterns()
