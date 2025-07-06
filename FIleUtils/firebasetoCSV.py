import firebase_admin
from firebase_admin import credentials, db
import csv
import os


def initialize_firebase():
    # Path to your Firebase service account key JSON file
    # cred = credentials.Certificate('serviceAccountKey.json')

    # Initialize the app with the service account and database URL
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://hackfusion-c831d-default-rtdb.asia-southeast1.firebasedatabase.app/"
    })


def fetch_team_data():
    # Reference to the user2 node
    ref = db.reference('user2')

    # Get all team data
    return ref.get()


def process_team_data(teams_data):
    processed_data = []

    for team_id, team_info in teams_data.items():
        # Create a new dict for each team, excluding cart and coupon nodes
        team_data = {}

        for key, value in team_info.items():
            if key not in ['cart', 'coupon']:
                # For simple fields, just add them directly
                if not isinstance(value, dict):
                    team_data[key] = value

        # Add team_id as a field
        team_data['team_id'] = team_id
        processed_data.append(team_data)

    return processed_data


def save_to_csv(data, filename='hackathon_teams.csv'):
    if not data:
        print("No data to save")
        return

    # Get all unique fields across all teams
    all_fields = set()
    for team in data:
        all_fields.update(team.keys())

    # Sort fields for consistent column order
    fieldnames = sorted(list(all_fields))

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data successfully saved to {filename}")


def main():
    try:
        initialize_firebase()
        print("Firebase initialized successfully")

        teams_data = fetch_team_data()
        print(f"Fetched data for {len(teams_data)} teams")

        processed_data = process_team_data(teams_data)
        print(f"Processed {len(processed_data)} team records")

        save_to_csv(processed_data)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()