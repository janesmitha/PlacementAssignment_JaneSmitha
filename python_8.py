'''Using the data from Question 5, write code the analyze the data and answer the following questions Note -
1. Draw plots to demonstrate the analysis for the following questions and better visualizations
2. Write code comments wherever required for code understanding

Insights to be drawn -
● Get all the overall ratings for each season and using plots compare the ratings for all the
seasons, like season 1 ratings, season 2, and so on.
● Get all the episode names, whose average rating is more than 8 for every season
● Get all the episode names that aired before May 2019
● Get the episode name from each season with the highest and lowest rating
● Get the summary for the most popular ( ratings ) episode in every season'''
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Step 1: Read and load the JSON data
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
response = requests.get(url)
data = response.json()

# Lists to store the results for each question
season_ratings = []
high_low_ratings = []
top_episodes_summary = []

# Step 2: Analysis and answering the questions
episodes = data["_embedded"]["episodes"]
for episode in episodes:
    season = episode["season"]
    rating = episode["rating"]["average"]
    airdate = episode["airdate"]
    name = episode["name"]
    summary = episode["summary"]

    # Question 1: Get all the overall ratings for each season
    if len(season_ratings) < season:
        season_ratings.append([])

    season_ratings[season - 1].append(rating)

    # Question 2: Get all the episode names whose average rating is more than 8 for every season
    if rating > 8:
        print("Episode with rating > 8:", name)

    # Question 3: Get all the episode names that aired before May 2019
    if airdate and airdate < "2019-05":
        print("Episode aired before May 2019:", name)

    # Question 4: Get the episode name from each season with the highest and lowest rating
    if len(high_low_ratings) < season:
        high_low_ratings.append((name, rating))
    else:
        if rating > high_low_ratings[season - 1][1]:
            high_low_ratings[season - 1] = (name, rating)

    # Question 5: Get the summary for the most popular (highest ratings) episode in every season
    if len(top_episodes_summary) < season:
        top_episodes_summary.append((name, ""))

    # Remove HTML tags from the summary
    soup = BeautifulSoup(summary, "html.parser")
    summary_text = soup.get_text()

    if not top_episodes_summary[season - 1][1] or summary_text.strip() != "":
        top_episodes_summary[season - 1] = (name, summary_text)

# Step 3: Visualization
# Plotting the ratings for all seasons
seasons = range(1, len(season_ratings) + 1)
plt.figure(figsize=(10, 6))
for season, ratings in zip(seasons, season_ratings):
    plt.plot([season] * len(ratings), ratings, marker="o", linestyle="", markersize=5, label=f"Season {season}")
plt.xlabel("Season")
plt.ylabel("Rating")
plt.title("Ratings for Each Season")
plt.legend()
plt.show()

# Step 4: Printing the results
print("\nEpisode names with average rating > 8 for every season:")
print("No episode found" if len(high_low_ratings) == 0 else high_low_ratings)

print("\nEpisode names that aired before May 2019:")
print("No episode found" if len(top_episodes_summary) == 0 else top_episodes_summary)

print("\nEpisode with the highest and lowest rating for each season:")
for season, episode in enumerate(high_low_ratings, start=1):
    print(f"Season {season}: Highest - {episode[0]}, Lowest - {episode[1]}")

print("\nSummary for the most popular (highest ratings) episode in every season:")
for season, episode in enumerate(top_episodes_summary, start=1):
    print(f"Season {season}: {episode[0]}\nSummary: {episode[1]}")
