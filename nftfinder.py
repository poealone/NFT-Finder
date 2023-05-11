import requests
from termcolor import colored
from pyfiglet import Figlet

# ASCII art title
f = Figlet(font='slant')
print(colored(f.renderText("NFT Contract Info"), "cyan"))

# Function to retrieve contract information from OpenSea API
def get_contract_info(contract_address):
    url = f"https://api.opensea.io/api/v1/asset_contract/{contract_address}"
    headers = {
        "Accept": "application/json",
        "X-API-KEY": "YOUR_API_KEY"  # Replace with your actual OpenSea API key
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Display contract information
        print(colored("Contract Information:", "yellow"))
        print(colored(f"Name: {data['name']}", "green"))
        print(colored(f"Symbol: {data['symbol']}", "green"))
        print(colored(f"Total Supply: {data['total_supply']}", "green"))
        print(colored(f"Description: {data['description']}", "green"))
    
    except requests.exceptions.HTTPError as err:
        print(colored(f"HTTP Error occurred: {err}", "red"))
    except requests.exceptions.RequestException as err:
        print(colored(f"An error occurred: {err}", "red"))
    except (KeyError, ValueError) as err:
        print(colored(f"Invalid or unexpected response format: {err}", "red"))

# Main script
contract_address = input("Enter NFT contract address: ")
get_contract_info(contract_address)
