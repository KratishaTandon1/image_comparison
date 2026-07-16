import csv
from collections import defaultdict
import difflib

def analyze_cheating_patterns(csv_path="transcription_data.csv"):
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

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
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
            # We ignore very short audio (e.g. < 2 seconds) to avoid false positives
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
                # Calculate edit distance / edit details
                # Check if it's a trivial punctuation/space edit
                diff_chars = set(user_text) ^ set(whisper_text)
                trivial_set = {'।', '.', ',', '?', ' ', '"', "'", '!'}
                
                # If only punctuation/whitespace differs and length difference is <= 2
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

    # Filter out users with high cheating indicators
    flagged_users = []
    print("\n--- Identifying Cheating Users (total tasks >= 1) ---")
    for uid, stats in user_stats.items():
        if stats["total_tasks"] < 1:
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
                "status": "BLOCK"
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
    
    # Print top 5 cheaters for quick review
    print("\nTop 5 Flagged Cheaters:")
    for u in flagged_users[:5]:
        print(f"User {u['user_id']}: Tasks={u['total_tasks']}, Rushed Rate={u['rushed_rate']:.1%}, Trivial Edits={u['trivial_edit_rate']:.1%}, Cheat Rate={u['rushed_cheat_rate']:.1%}")

if __name__ == "__main__":
    analyze_cheating_patterns()
