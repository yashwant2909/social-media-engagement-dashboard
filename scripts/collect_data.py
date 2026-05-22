from googleapiclient.discovery import build
import pandas as pd

# Your API Key
API_KEY = "AIzaSyCVnMZgk6yp2c5m95A9CQc4qL6Pqlan-ME"

# Connect to YouTube
youtube = build(
    'youtube',
    'v3',
    developerKey=API_KEY
)

# Search YouTube videos
search_response = youtube.search().list(
    q="Python programming",
    part="snippet",
    maxResults=10
).execute()

# Empty list
video_ids = []

# Collect video IDs
for item in search_response['items']:

    if item['id']['kind'] == 'youtube#video':

        video_ids.append(
            item['id']['videoId']
        )

# Get video statistics
video_response = youtube.videos().list(
    part='snippet,statistics',
    id=','.join(video_ids)
).execute()

# Final data list
videos = []

# Loop through videos
for video in video_response['items']:

    snippet = video['snippet']
    stats = video['statistics']

    videos.append({

        'Title': snippet['title'],

        'Channel': snippet['channelTitle'],

        'Published_Date': snippet['publishedAt'],

        'Views': int(
            stats.get('viewCount', 0)
        ),

        'Likes': int(
            stats.get('likeCount', 0)
        ),

        'Comments': int(
            stats.get('commentCount', 0)
        )

    })

# Convert to table
df = pd.DataFrame(videos)

# Save CSV file
df.to_csv(
    'data/youtube_data.csv',
    index=False
)

print("\nData Collected Successfully!\n")

print(df.head())