import pandas as pd
import plotly.express as px
from web3 import Web3
from datetime import datetime, timezone
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Web3 connection
INFURA_URL = os.getenv('INFURA_URL')
if not INFURA_URL:
    raise ValueError("INFURA_URL is not set in the .env file")

web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.is_connected():
    raise ConnectionError("Failed to connect to Ethereum blockchain. Check your INFURA_URL.")

# Load transfer event data
save_path = "C:/Users/leahl/OneDrive/Desktop/Data Analysis Projects/Smart_Contract_Event_Analysis/transfer_events.json"
with open(save_path, "r") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Extract relevant fields from 'args' column
df['from'] = df['args'].apply(lambda x: x.get('from') if isinstance(x, dict) else None)
df['to'] = df['args'].apply(lambda x: x.get('to') if isinstance(x, dict) else None)
df['value'] = df['args'].apply(lambda x: int(x.get('value', 0)) if isinstance(x, dict) else 0)

# Validate block numbers and fetch timestamps
def fetch_timestamps(block_numbers):
    timestamps = {}
    for block_number in block_numbers:
        for attempt in range(3):  # Retry up to 3 times
            try:
                block = web3.eth.get_block(block_number)
                timestamps[block_number] = datetime.fromtimestamp(block['timestamp'], tz=timezone.utc)
                break
            except Exception as e:
                if attempt == 2:  # Log failure after 3 attempts
                    print(f"Block {block_number} failed after 3 attempts: {e}")
                    timestamps[block_number] = None
    return timestamps

# Fetch timestamps
unique_blocks = df['blockNumber'].unique()
timestamps = fetch_timestamps(unique_blocks)

# Map timestamps to DataFrame
df['timestamp'] = df['blockNumber'].map(timestamps)
df['timestamp'] = df['timestamp'].apply(lambda x: pd.NaT if x is None else x)

# If no valid timestamps exist, skip timestamp-based analysis
if df['timestamp'].isna().all():
    print("No valid timestamps found. Skipping timestamp-based analysis.")
else:
    # Add a 'date' column based on 'timestamp'
    df['date'] = df['timestamp'].dt.date

    # Aggregate daily trends
    daily_trends = df.groupby('date')['value'].sum().reset_index()
    daily_trends.columns = ['date', 'value']

    # Plot daily trends
    fig = px.line(
        daily_trends,
        x='date',
        y='value',
        title='Daily Transaction Volume',
        labels={'date': 'Date', 'value': 'Transaction Volume'}
    )
    fig.show()

# Non-timestamp-based Analysis
total_volume = df['value'].sum()
top_senders = df['from'].value_counts().head(10)
top_receivers = df['to'].value_counts().head(10)

# Print analysis results
print(f"Total Volume Transferred: {total_volume}")
print("Top Senders:\n", top_senders)
print("Top Receivers:\n", top_receivers)

