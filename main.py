"""
TASK SUMMARY:
What are we building? A Command Line Interface (CLI) tool for GitHub.
What does it do? 
1. It takes a GitHub username from the terminal.
2. It fetches that user's profile data from the GitHub website using their API.
3. It handles errors (like if the internet is off or the user doesn't exist).
4. It creates an 'output' folder and saves the user's data in a JSON file.
"""

# 1. IMPORTING LIBRARIES (The tools we need)
import sys      # Used to read the username typed in the terminal
import os       # Used to create folders and read our .env file
import json     # Used to save the data cleanly in a .json file format
import requests # Used to talk to the internet (GitHub API)
from dotenv import load_dotenv # Used to load secrets from the .env file

# Load the secrets from the .env file into our Python code
load_dotenv()

def get_github_profile():
    # 2. READING TERMINAL INPUT
    # sys.argv is a list of what you typed in the terminal.
    # sys.argv[0] is 'main.py'
    # sys.argv[1] is the username (e.g., 'octocat')
    # If the user forgot to type a username, stop the program and warn them.
    if len(sys.argv) < 2:
        print("Oops! You forgot to give a username.")
        print("How to run: python main.py <username>")
        return

    # Grab the username from the terminal command
    username = sys.argv[1]
    
    # Create the exact GitHub API link for this specific user
    url = f"https://api.github.com/users/{username}"
    
    # 3. SETTING UP SECURITY (Optional)
    # Get the GITHUB_TOKEN from the .env file. 
    # If we don't have one, it will just be None, which is fine for basic use.
    token = os.getenv("GITHUB_TOKEN")
    
    headers = {}
    if token:
        # If a token exists, attach it to our request like a VIP pass
        headers["Authorization"] = f"Bearer {token}"

    try:
        # 4. FETCHING DATA FROM GITHUB
        print(f"Searching the internet for '{username}'...")
        
        # Go to the URL, use the headers, and give up if it takes more than 10 seconds
        response = requests.get(url, headers=headers, timeout=10)
        
        # If GitHub says "404", it means this user does not exist.
        if response.status_code == 404:
            print(f"Error: We couldn't find anyone named '{username}' on GitHub.")
            return
            
        # If there's any other error (like server down), this line will catch it and jump to the "except" block
        response.raise_for_status()
        
        # Convert the raw internet response into a Python dictionary
        user_data = response.json()
        
        # 5. SAVING DATA TO A FILE
        # Check if a folder named "output" exists. If not, create it.
        os.makedirs("output", exist_ok=True)
        
        # Create the file name (e.g., "output/octocat.json")
        file_path = f"output/{username}.json"
        
        # Open the file in "Write" mode ("w")
        with open(file_path, "w", encoding="utf-8") as file:
            # Dump the data into the file nicely formatted (indent=4 makes it readable)
            json.dump(user_data, file, indent=4)
            
        print(f"Success! I saved the profile data inside '{file_path}'")

    # 6. ERROR HANDLING (What if things go wrong?)
    except requests.ConnectionError:
        # This happens if your Wi-Fi is off
        print("Network Error: Please check your internet connection.")
        
    except requests.Timeout:
        # This happens if GitHub takes too long to reply
        print("Timeout Error: The internet is too slow right now. Try again.")
        
    except Exception as error_message:
        # This catches any other random error we didn't think of
        print(f"Something unexpected went wrong: {error_message}")

# This is the starting point of the script. It tells Python to run our function.
if __name__ == "__main__":
    get_github_profile()