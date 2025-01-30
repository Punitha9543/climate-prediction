from flask import Flask, jsonify, request
import pandas as pd
import requests

app = Flask(__name__)

data_url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"

def fetch_climate_data():
    """Fetch climate data from NASA and process it."""
    response = requests.get(data_url)
    file_path = "global_temperature_data.csv"
    
    with open(file_path, "wb") as file:
        file.write(response.content)
    
    # Load into DataFrame
    df = pd.read_csv(file_path, skiprows=1)  # Adjust based on actual format
    return df

@app.route('/')
def home():
    return "<h1>Climate Change Analysis API</h1><p>Use /data to fetch climate data.</p>"

@app.route('/data', methods=['GET'])
def get_data():
    """API endpoint to fetch and return climate data."""
    df = fetch_climate_data()
    return jsonify(df.head().to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=False,port=5001)