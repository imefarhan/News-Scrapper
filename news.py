import requests
from bs4 import BeautifulSoup

url = "https://www.hindustantimes.com/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a")

##for link in links:
##    print(link.get("href"))

for link in links:
    href = link.get("href")
    headline = []
    line = []
    if href.startswith("https://www.hindustantimes.com/"):
        news = href[31:-34]
        if news.startswith("india-news/"):
            headline = news[11:]
        elif news.startswith("columns/"):
            headline = news[8:]
        elif news.startswith("bollywood/"):
            headline = news[10:]
        elif news.startswith("hollywood/"):
            headline = news[10:]
        elif news.startswith("tv/"):
            headline = news[3:]
        elif news.startswith("cricket/"):
            headline = news[8:]
        elif news.startswith("cities/"):
            headline = news[7:]
        elif news.startswith("education/"):
            headline = news[10:]
        elif news.startswith("tech/"):
            headline = news[5:]
        elif news.startswith("world-news/"):
            headline = news[11:]
            
        for i in headline:
                if i=='-':
                    line.append(' ')
                else:
                    line.append(i)
                    
#        print(line)

    if len(line):
        output = open("news-out.csv","a")
        output.writelines(line)
        output.write('\n')
        output.close()
