from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text

#print(source)
csv_file = open('csv_check.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline','Summary','Video_link'])

soup = BeautifulSoup(source,'lxml')
article = soup.find('article')

for article in soup.find_all('article'):
    #print(soup.prettify())
    #print(article.prettify())

    headline = article.find('header',class_="entry-header").h2.text
    print(headline)
    summary = article.find('div',class_="entry-content").p.text
    print(summary)
    try:
        yt_link = article.find('div',class_="entry-content")
        yt_link = yt_link.find('span',class_="embed-youtube") 
        vid_src = yt_link.find('iframe',class_="youtube-player")['src']
        vid_split = vid_src.split('/')[4]
        vid_id = vid_split.split('?')[0]
        #print(vid_id)

        youtube_link = f'https://youtube.com/watch?v={vid_id}'
        
    except Exception as e:
        youtube_link = None

    print(youtube_link)

    csv_writer.writerow([headline,summary,youtube_link])

csv_file.close()

