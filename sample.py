import requests
news_api_key="f71565537970409cbe006afcbac30c33"

main_url="https://newsapi.org/v2/top-headlines?country=us&apiKey="+news_api_key
news=requests.get(main_url).json()
articles=news["articles"]

news_articles_title=[]
for a in articles:
    news_articles_title.append(a["title"])

news_articles_description=[]
for a in articles:
    news_articles_description.append(a["description"])

news_articles_url=[]
for a in articles:
    news_articles_url.append(a["url"])

news_articles_urlToImage=[]
for a in articles:
    news_articles_urlToImage.append(a["urlToImage"])

news_articles_publishedAt=[]
for a in articles:
    news_articles_publishedAt.append(a["publishedAt"])

news_articles_content=[]
for a in articles:
    news_articles_content.append(a["content"])


print(len(news_articles_title))
print(len(news_articles_description))
print(len(news_articles_url))
print(len(news_articles_urlToImage))
print(len(news_articles_publishedAt))
print(len(news_articles_content))

print(articles)