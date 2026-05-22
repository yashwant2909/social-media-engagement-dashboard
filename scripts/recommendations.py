import pandas as pd

# Load analyzed data
df = pd.read_csv(
    'data/analyzed_data.csv'
)

# Average engagement
avg_engagement = df[
    'Engagement_Rate'
].mean()

print("\nAI CONTENT STRATEGY\n")

# Recommendation logic
if avg_engagement > 10:

    print(
        "Excellent engagement."
    )

    print(
        "Continue current strategy."
    )

elif avg_engagement > 5:

    print(
        "Good engagement."
    )

    print(
        "Upload more consistently."
    )

else:

    print(
        "Low engagement."
    )

    print(
        "Improve thumbnails and titles."
    )