import pandas as pd

# Load CSV file
df = pd.read_csv(
    'data/youtube_data.csv'
)

# Remove empty rows
df = df.dropna()

# Convert published date into real datetime
df['Published_Date'] = pd.to_datetime(
    df['Published_Date']
)

# Extract upload hour
df['Upload_Hour'] = (
    df['Published_Date'].dt.hour
)

# Extract upload day
df['Upload_Day'] = (
    df['Published_Date'].dt.day_name()
)

# Calculate engagement rate
df['Engagement_Rate'] = (

    (df['Likes'] + df['Comments'])

    / df['Views']

) * 100

# Sort best videos
top_videos = df.sort_values(
    by='Engagement_Rate',
    ascending=False
)

# Save analyzed data
top_videos.to_csv(
    'data/analyzed_data.csv',
    index=False
)

print("\nTop Videos:\n")

print(
    top_videos[
        [
            'Title',
            'Views',
            'Likes',
            'Comments',
            'Engagement_Rate'
        ]
    ].head()
)