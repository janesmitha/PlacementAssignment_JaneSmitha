'''Write a program to download the data from the given API link and then extract the following data with
proper formatting
Write a program to download the data from the given API link and then extract the following data with
proper formatting

Link - http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes
Note - Write proper code comments wherever needed for the code understanding

Sample Data -

Excepted Output Data Attributes -
● id - int url - string
● name - string season
● - int number - int
● type - string airdate -
● date format airtime -
● 12-hour time format
● runtime - float
● average rating - float
● summary - string
● without html tags
● medium image link - string
● Original image link - string'''
import requests
import json

# Step 1: Download the data
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
response = requests.get(url)
data = response.json()

# Step 2: Extract the desired attributes
show_id = data["id"]
show_url = data["url"]
show_name = data["name"]
episodes = data["_embedded"]["episodes"]

formatted_data = []
for episode in episodes:
    episode_id = episode["id"]
    episode_url = episode["url"]
    episode_season = episode["season"]
    episode_number = episode["number"]
    episode_type = episode["type"]
    episode_airdate = episode["airdate"]
    episode_airtime = episode["airtime"]
    episode_runtime = episode["runtime"]
    episode_rating = episode["rating"]["average"]
    episode_summary = episode["summary"]
    episode_image_medium = episode["image"]["medium"]
    episode_image_original = episode["image"]["original"]

    # Remove HTML tags from the summary
    episode_summary = episode_summary.replace("<p>", "").replace("</p>", "").strip()

    # Create a dictionary with the extracted attributes
    episode_data = {
        "id": episode_id,
        "url": episode_url,
        "name": show_name,
        "season": episode_season,
        "number": episode_number,
        "type": episode_type,
        "airdate": episode_airdate,
        "airtime": episode_airtime,
        "runtime": episode_runtime,
        "average rating": episode_rating,
        "summary": episode_summary,
        "medium image link": episode_image_medium,
        "original image link": episode_image_original
    }

    formatted_data.append(episode_data)

# Step 3: Print or further process the extracted data
for episode_data in formatted_data:
    print(episode_data)
