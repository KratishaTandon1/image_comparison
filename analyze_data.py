import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("transcription_data.csv")

print("--- Data Info ---")
print(df.info())

print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Value counts of is_edited ---")
print(df['is_edited'].value_counts())

# Basic stats of numeric fields
print("\n--- Summary Statistics ---")
print(df[['duration', 'time_taken_by_user', 'segment_character_per_second']].describe())

# Group by user and find user-level patterns
print("\n--- User Level Metrics ---")
user_metrics = df.groupby('user_id').agg(
    total_tasks=('user_id', 'count'),
    edited_count=('is_edited', lambda x: (x == True).sum()), # check if boolean or string
    edited_rate=('is_edited', lambda x: (x == True).mean()),
    mean_duration=('duration', 'mean'),
    mean_time_taken=('time_taken_by_user', 'mean'),
    mean_speed_ratio=('time_taken_by_user', lambda x: (x / df.loc[x.index, 'duration']).mean()),
    mean_char_sec=('segment_character_per_second', 'mean'),
    max_char_sec=('segment_character_per_second', 'max'),
)
# Let's inspect is_edited values to ensure the lambda matches correctly
print("Unique is_edited values:", df['is_edited'].unique())

print(user_metrics.sort_values(by='edited_rate'))
