import csv
import json

# Define the input and output file paths
input_file = 'C:/Users/dylan/Desktop/Portfolio Projects/testing/nextcloud_import.csv'  #This will pick up the file from icloud password retreival program
output_file = 'C:/Users/dylan/Desktop/Portfolio Projects/testing/bitwarden_compatible.json'

# Read the input CSV file
with open(input_file, mode='r', newline='') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# Prepare the Bitwarden JSON structure
bitwarden_data = {
    "encrypted": False,
    "folders": [],
    "items": []
}

# Process each row in the CSV
for row in rows:
    if row['type'] == 'login':  # Process only 'login' types
        item = {
            "organizationId": None,
            "folderId": None,
            "type": 1,
            "name": row['name'],
            "notes": row.get('notes', ''),
            "favorite": bool(row.get('fav', False)),
            "login": {
                "username": row['username'],
                "password": row['password'],
                "totp": row.get('otp', None),
                "uris": [
                    {
                        "uri": f"https://{row['url']}",
                        "match": None
                    }
                ]
            }
        }
        bitwarden_data["items"].append(item)

# Write the output JSON file
with open(output_file, mode='w') as outfile:
    json.dump(bitwarden_data, outfile, indent=4)

print("Conversion complete. The Bitwarden-compatible JSON file has been created.")
