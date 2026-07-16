import urllib.request

url = "https://docs.google.com/spreadsheets/d/12_IKbFs_4tjjcDwIxPQC9EI47_bZCOUpueCw6YSWWkw/export?format=csv"
output_path = r"c:\Users\prakh\Downloads\josh\transcription_data.csv"

print(f"Downloading from {url} to {output_path}...")
urllib.request.urlretrieve(url, output_path)
print("Download complete!")
