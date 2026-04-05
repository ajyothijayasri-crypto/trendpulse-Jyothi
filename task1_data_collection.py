import requests
import time
import json
from datetime import datetime

# top stories list
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
story_ids = response.json()

stories = []

for sid in story_ids[:100]:
    try:
        item_url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
        data = requests.get(item_url).json()

        if data is None:
            continue

        title = data.get("title", "").lower()

        # category logic
        if "ai" in title or "tech" in title:
            category = "technology"
        elif "game" in title or "sport" in title:
            category = "sports"
        else:
            category = "worldnews"

        story = {
            "post_id": data.get("id"),
            "title": data.get("title"),
            "category": category,
            "score": data.get("score"),
            "num_comments": data.get("descendants"),
            "author": data.get("by"),
            "collected_at": str(datetime.now())
        }

        stories.append(story)

    except:
        print("error vachindi skip chesam")

# save file
with open("data.json", "w") as f:
    json.dump(stories, f, indent=4)

print("Done! stories:", len(stories))
