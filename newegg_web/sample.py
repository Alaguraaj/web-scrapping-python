from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card').text
#print(source)

soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())
csv_file = open('new_egg.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Brand','Description','price','Shipping_Cost'])

whole_article = soup.find('div',class_="items-view is-grid")

for article in whole_article.find_all('div',class_="item-container"):
    article_heading = article.find('div',class_="item-info")
    brand_all = article_heading.find('div',class_="item-branding")
    brand = brand_all.find('img')['title']
    print(brand)

    summary = article_heading.find('a',class_="item-title").text
    print(summary)

    price_head = article_heading.find('div',class_="item-action")
    price_head_ul =price_head.ul
    price = price_head_ul.find('li',class_="price-current").text
    price = price.split('(')[0]
    price = price.strip()
    print(price)

    shipping = price_head_ul.find('li',class_='price-ship').text
    shipping = shipping.strip()
    print(shipping)

    csv_writer.writerow([brand,summary,price,shipping])

csv_file.close()



