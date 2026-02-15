📊 YouTube Video Statistics Checker (Python)

This is a simple command-line Python application that fetches YouTube video statistics using the YouTube Data API v3.
The app allows users to enter a YouTube video URL and instantly view key details like views, likes, comments, and video title.

🎯 What this app does

Accepts a YouTube video URL as input

Extracts the video ID from the URL

Connects to the YouTube Data API v3

Displays:

🎬 Video title

👁 View count

👍 Like count

💬 Comment count

🧠 Technologies used

Python 3

Google API Python Client

Regular Expressions (regex)

YouTube Data API v3

🔑 API Requirement

This project uses the YouTube Data API v3.
You need a valid Google API Key to run the project.

Replace this line in the code with your own API key:

API_KEY = "YOUR_API_KEY_HERE"

📦 Required Library

Install the required library using:

python -m pip install google-api-python-client

▶️ How to run the project

Make sure Python is installed

Save the file as youtube_stats.py

Open Command Prompt or PowerShell in the project folder

Run the program using:

python youtube_stats.py

🖥️ How to use the app

Run the program

Paste a valid YouTube video URL when prompted

Press Enter

View the video statistics displayed in the terminal

⚠️ Notes

If likes are hidden by the video owner, the app may show N/A

API usage is subject to daily quota limits

Invalid URLs will return an error message

🎯 Purpose of this project

Learn how to work with external APIs

Understand API authentication using API keys

Practice regex for URL parsing

Build a real-world command-line application

🔮 Future improvements

Add GUI version (Tkinter / Streamlit)

Support playlist statistics

Add error handling for quota limits

Save results to a file

👤 Author

Created by [nikitha]
