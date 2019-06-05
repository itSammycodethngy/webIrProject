

import json
import requests
with open('csvSeek.json', 'r') as f:
    jobs = json.load(f)

count = 1
for job in jobs:
    title = job['title']
    link = job['link']
    company = job['company']
    summary = job['summary']

    post_url = "http://localhost:9200/indeed/jobs"
    post_autocomplete_url = "http://localhost:9200/autocomplete/titles"
    payload = {
        "title": title,
        "link": link,
        "company": company,
        "summary": summary
    }
    payload_autocomplete = {
        "title": title,
        "title_suggest": title
    }

    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    payload = json.dumps(payload)
    payload_autocomplete = json.dumps(payload_autocomplete)
    response = requests.request("POST", post_url, data=payload, headers=headers)

    response_autocomplete = requests.request("POST", post_autocomplete_url, data=payload_autocomplete, headers=headers)
    if response.status_code == 201:
        print("Values Posted in hacker index")
    if response_autocomplete.status_code == 201:
        print("Values Posted in autocomplete index")

    print("----------------", count, "----------------------")
    count = count + 1







