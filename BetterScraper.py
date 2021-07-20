import requests
import csv
import pandas as pd

base_url = 'https://www.sitepoint.com'
url = f'{base_url}/community/latest.json'
topics_list= []
replies = []
views = []
for i in range(0, 40):
    page = requests.get(url, params={'ascending': False, 'no_definitions': True, 'page': i})
    resp = page.json()
    for word in (resp.get('topic_list', {}).get('topics', [])):
        topics_list.append(word.get('title'))
        replies.append(word.get('posts_count') - 1)
        views.append(word.get('views'))

currList = []
titles = ['Title', 'Views', 'Number of Replies']
index = 0
with open('ScrapedData.csv', 'w') as df:
    write = csv.writer(df)
    write.writerow(titles)
    for entry in topics_list:
        currList = [topics_list[index], views[index], replies[index]]
        write.writerow(currList)
        index+=1
    df.close()
