# Install required libraries
from web3 import Web3
import os
from dotenv import load_dotenv

# Ensure json is imported for saving event list
# Ensure HexBytes imported to convert HexBye objects into strings
import json 
from hexbytes import HexBytes

# Load environment variables
load_dotenv()

# Connect to Ethereum node
INFURA_URL = os.getenv('INFURA_URL')
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Pre code check code check 
print("Using Infura URL:", INFURA_URL)

# Code check
if web3.is_connected(): 
    print("Connected to Ethereum blockchain")
else:
    print("Connection failed")

# Add RAIL contract address
contract_address = "0xe76C6c83af64e4C60245D8C7dE953DF673a7A33D"  # RAIL contract address

# Add RAIL contract ABI
contract_abi = [
    {
        "inputs": [
            {"internalType": "address", "name": "_initialHolder", "type": "address"},
            {"internalType": "uint256", "name": "_initialSupply", "type": "uint256"},
            {"internalType": "uint256", "name": "_cap", "type": "uint256"},
            {"internalType": "address", "name": "_owner", "type": "address"},
            {"internalType": "address[]", "name": "_lps", "type": "address[]"}
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "owner", "type": "address"},
            {"indexed": True, "internalType": "address", "name": "spender", "type": "address"},
            {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "previousOwner", "type": "address"},
            {"indexed": True, "internalType": "address", "name": "newOwner", "type": "address"}
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "from", "type": "address"},
            {"indexed": True, "internalType": "address", "name": "to", "type": "address"},
            {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "DEPLOY_TIME",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"}
        ],
        "name": "allowance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "cap",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"}
        ],
        "name": "decreaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_account", "type": "address"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"}
        ],
        "name": "governanceMint",
        "outputs": [{"internalType": "bool", "name": "success", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "addedValue", "type": "uint256"}
        ],
        "name": "increaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_recipient", "type": "address"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "sender", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
] # Rail ABI JSON

# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Test the contract instance
if contract:
    print("Contract instance created successfully!")

# Call function to get the total supply of the tokens
total_supply = contract.functions.totalSupply().call()
print(f"Total Supply: {total_supply}")

# Define block range dynamically based on deployment block
start_block = 20296056  # Deployment block of the contract
end_block = web3.eth.block_number  # Latest block
step = 10000  # Process 10,000 blocks at a time
all_events = []

print(f"Fetching Transfer events from block {start_block} to {end_block}...")

for block in range(start_block, end_block, step):
    from_block = block
    to_block = min(block + step - 1, end_block)  # Ensure we don't exceed the latest block
    
    print(f"Fetching events from block {from_block} to {to_block}...")
    try:
        transfer_event = contract.events.Transfer.create_filter(from_block=from_block, to_block=to_block)
        events = transfer_event.get_all_entries()
        all_events.extend(events)
        print(f"Retrieved {len(events)} events from block {from_block} to {to_block}.")
    except Exception as e:
        print(f"Error fetching events from block {from_block} to {to_block}: {e}")

print(f"Total Transfer events retrieved: {len(all_events)}")

# Function to recursively convert AttributeDict and HexBytes to plain dict
def attribute_dict_to_dict(obj):
    if isinstance(obj, dict):
        return {k: attribute_dict_to_dict(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [attribute_dict_to_dict(v) for v in obj]
    elif isinstance(obj, HexBytes):  # Handles HexBytes
        return obj.hex()
    elif hasattr(obj, "_asdict"):  # Handles namedtuples or similar
        return attribute_dict_to_dict(obj._asdict())
    elif hasattr(obj, "keys"):  # Handles AttributeDict
        return {k: attribute_dict_to_dict(v) for k, v in obj.items()}
    else:
        return obj

# Convert events to JSON-serializable format
events_dicts = [attribute_dict_to_dict(event) for event in all_events]

# Save events to a specific folder in JSON file format
save_path = "C:/Users/leahl/OneDrive/Desktop/Data Analysis Projects/Smart_Contract_Event_Analysis/transfer_events.json"
try:
    with open(save_path, "w") as f:
        json.dump(events_dicts, f, indent=4)
    print(f"File saved successfully at: {save_path}")
except Exception as e:
    print(f"Error saving file: {e}")
