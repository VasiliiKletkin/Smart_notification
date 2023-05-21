import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote


def get_ads(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
    response = requests.get(url, headers=headers)
    hostname = response.url.split("://")[1].split("/")[0]
    soup = BeautifulSoup(response.text, "html.parser")
    ads = []
    if not response.status_code:
        print("ERROR")
        return []
    
    if hostname == "ss.ge":
        items = soup.find_all("div", class_="latest_article_each")
        for item in items:
            try:
                price = item.find("div", class_="latest_price").get_text()
                title = item.find("span", class_="TiTleSpanList").get_text()
                url = item.find("a").get("href")
                ad = {"title": title,"price": price,"url": unquote(hostname + url)}
                ads.append(ad)
            except:
                continue    

    elif hostname == "www.myhome.ge":
        items = soup.find_all("div", class_="statement-card")
        for item in items:
            try:
                title = item.find("h5", class_="card-title").get_text()
                price = item.find("b", class_="item-price-usd").get_text()
                url = item.find("a", class_="card-container").get("href")
                ad = {"title": title,"price": price,"url": unquote(url)}
                ads.append(ad)
            except:
                continue
    return ads

url = "https://www.myhome.ge/ru/s/%D0%A1%D0%B4%D0%B0%D0%B5%D1%82%D1%81%D1%8F-%D0%B2-%D0%B0%D1%80%D0%B5%D0%BD%D0%B4%D1%83-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D0%B0-%D0%A2%D0%B1%D0%B8%D0%BB%D0%B8%D1%81%D0%B8?Keyword=%D0%A2%D0%B1%D0%B8%D0%BB%D0%B8%D1%81%D0%B8&AdTypeID=3&PrTypeID=1&SortID=1&mapC=41.73188365%2C44.8368762993663&regions=687578743&fullregions=687578743&districts=62176122.319380261.58416723.2953929439.58420997.152297954.61645269.6273968347.58416582.58416672.58377946&cities=1996871&GID=1996871&OwnerTypeID=1"
print(get_ads(url))

