# Day 46: Create a DataFrame

import pandas as pd

data = {
    'year': [2009, 2002, 2009, 2010, 2009],
    'Title': ['Brothers', 'Spider-Man', 'WatchMen', 'Inception', 'Avatar'],
    'genre': ['Drama', 'Sci-fi', 'Drama', 'Sci-fi', 'Fantasy']
}

df = pd.DataFrame(data)

print(df)

# Extra Challenge: Website Data with Pandas

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

response = requests.get(url)

wiki_soup = BeautifulSoup(response.text, 'html.parser')
data = wiki_soup.find('table', {'class': 'wikitable'})

df = pd.read_html(str(data))

df = pd.DataFrame(df[0])

df = df.drop(["Description", "Syntax examples"], axis=1)

print(df)



