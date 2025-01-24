from urllib.request import urlopen
import pandas as pd
import json

# url = 'https://api.openf1.org/v1/car_data?driver_number=55&session_key=9159&speed%3E%3D315'
# url = 'https://api.openf1.org/v1/sessions?year=2023&csv=true'
event_key = "italian-grand-prix-2024"  # Hypothetical key
url = f'https://api.openf1.org/v1/race_data?event_key={event_key}'

# response = urlopen(url)
# data = json.loads(response.read().decode('utf-8'))
# df = pd.DataFrame(data)
# print(df)

try:
    # Fetch the data
    response = urlopen(url)
    data = json.loads(response.read().decode('utf-8'))

    # Inspect the JSON structure
    print(json.dumps(data, indent=4))  # For debugging purposes

    # Convert the data to a DataFrame (adjust based on JSON structure)
    df = pd.DataFrame(data['results'])  # Assuming 'results' contains relevant race info

    # Display the DataFrame
    print(df)
except Exception as e:
    print(f"Error fetching data: {e}")
