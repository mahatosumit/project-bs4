# Install requrememts
# ! pip install beautifulsoup4
# ! pip install lxml
# ! pip install requests
# ! pip install pandas
# ! pip install matplotlib
# ! pip install seaborn
# ! pip install html5libhttps://subslikescript.com

from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f"{root}/movies"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())


box = soup.find('article', class_="main-article")
links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])
print(links)

for link in links:
    website = f"{root}/{link}"
    result = requests.get(website)
    content = result.text

    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_="main-article")
    title = box.find('h1').get_text()

    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    with open(f'transcript.txt', 'w') as file:
        file.write(transcript)
