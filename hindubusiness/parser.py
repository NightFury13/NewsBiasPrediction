import urllib
from bs4 import BeautifulSoup as BS

output_f = 'hindub_urls.txt'

base_url = 'http://www.thehindubusinessline.com/today/?date=2014-'
urls = []
for month in range(1,13):
    for date in range(1,32):
        urls.append(base_url+'%.2d' % month+'-%.2d' % date)

links = []
for url in urls:
    print "Parsing", url
    try:
        r = urllib.urlopen(url).read()
        soup = BS(r, 'lxml')

        link = [i['href'] for i in soup.find('div', {'class':'tpaper'}).find_all('a')[2:]]
        links += link
    except:
        print "         > Skipping", url

with open(output_f, 'w') as f:
    for link in links:
        f.write(link+'\n')
