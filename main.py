import requests

# BBC News API endpoint
BBC_NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"

# BBC News API parameters
params = {
    "sources": "bbc-news",
    "apiKey": "b93db0ad20254a2089e87cffbd588066",
}

# make a GET request to the BBC News API
response = requests.get(BBC_NEWS_API_ENDPOINT, params=params)

# parse the response as JSON
response_json = response.json()

# loop through the articles in the response and print their titles
for article in response_json["articles"]:
    print(article["title"])

    # prompt the user to read more about the article
    read_more = input("Would you like to read more about this article? (y/n)")

    # if the user wants to read more, print the article's URL
    if read_more.lower() == "y":
        print(article["url"])
