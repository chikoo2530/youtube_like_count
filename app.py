from googleapiclient.discovery import build
import re

# 🔑 Paste your API key here
API_KEY = "AIzaSyBnVk8SqeaW85Khmrcxv5MY8sDHJaTJIuM"

def extract_video_id(url):
    """
    Extracts video ID from YouTube URL
    """
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

def get_video_stats(video_url):
    video_id = extract_video_id(video_url)

    if not video_id:
        print("❌ Invalid YouTube URL")
        return

    youtube = build("youtube", "v3", developerKey=API_KEY)

    request = youtube.videos().list(
        part="statistics,snippet",
        id=video_id
    )

    response = request.execute()

    if not response["items"]:
        print("❌ Video not found")
        return

    stats = response["items"][0]["statistics"]
    title = response["items"][0]["snippet"]["title"]

    views = stats.get("viewCount", "N/A")
    likes = stats.get("likeCount", "N/A")
    comments = stats.get("commentCount", "N/A")

    print("\n🎬 Video Title:", title)
    print("👁 Views:", views)
    print("👍 Likes:", likes)
    print("💬 Comments:", comments)


# ==========================
# ▶️ USER INPUT
# ==========================
url = input("Enter YouTube Video URL: ")
get_video_stats(url)
