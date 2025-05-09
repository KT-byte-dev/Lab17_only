# Lab17_kalkidantesfaye_1.py
# Author: Kalkidan Tesfaye
# Description: Refactored hacker news script that avoids the key error missing "descendants"
# Date: 05/09/2025  

# from the book: hn
from operator import itemgetter

import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a new API call for each submission.
    #  url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
    'title': response_dict['title'],
     'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
    'comments': response_dict['descendants'],
    }