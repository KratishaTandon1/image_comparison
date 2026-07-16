import csv

with open("transcription_data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for i in range(5):
        try:
            print(next(reader))
        except StopIteration:
            break
