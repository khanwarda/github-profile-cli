# GitHub Profile CLI Tool

## What is this project?
This is a Command Line Interface (CLI) tool built with Python. Instead of opening a web browser to check a GitHub user's profile, you can just type their username in the terminal. The tool will fetch their data from the internet and save it nicely on your computer.

## How to Run It
1. Open your terminal.
2. Type: `python main.py <username>` (for example: `python main.py octocat`).
3. Press Enter! The tool will create an `output` folder and save the user's data in a `.json` file.

---

## My Learnings & Common Questions

**1. What is exactly happening behind the scenes?**
When we run the command, our Python code uses a library called `requests` to talk to the "GitHub API". 
Think of an API like a waiter in a restaurant. Our code tells the waiter (API) what username we want. The waiter goes to the kitchen (GitHub's servers), gets the user's profile data, and brings it back to us in a format called JSON. 

**2. Why is my `.env` file empty, but the code still works?**
The `.env` file is meant to securely store a secret `GITHUB_TOKEN`. However, GitHub allows anyone to look at *public* information (like followers or public repositories) for free, without needing a password or token. 
Our code is smart: it says, "If there is no token in the `.env` file, just ask GitHub politely as a normal public guest." That is why it successfully created the output! We only need a token if we want to make thousands of requests in a single hour.

**3. Why did we make an `output` folder and a JSON file?**
When the API gives us the data, it's just raw text. JSON (JavaScript Object Notation) organizes this text into readable key-value pairs (like `"followers": 24458`). We programmed the tool to automatically create an `output` folder so that our main project folder doesn't get messy with dozens of downloaded files.

**4. Why did we use `sys.argv`?**
We used `sys.argv` to make our tool dynamic. Instead of hardcoding a name like "octocat" directly inside the Python code, `sys.argv` allows the script to read whatever name the user types in the terminal.