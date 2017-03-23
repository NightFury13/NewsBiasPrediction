import urllib
from bs4 import BeautifulSoup as BS

output_f = 'hindu_urls.txt'

base_url = 'http://www.thehindu.com/archive/web/2014/'
urls = []
for month in range(1,13):
    for date in range(1,32):
        urls.append(base_url+'%.2d' % month+'/%.2d' % date +'/')

links = []
for url in urls:
    print "Parsing", url
    try:
        r = urllib.urlopen(url).read()
        soup = BS(r, 'lxml')

        section = soup.find('h2', id='national').parent.parent.parent

        posts = section.find_all('ul', {'class':'archive-list'})[0].find_all('a')
        for post in posts:
            links.append(post['href'])
    except:
        print "         > Skipping", url

with open(output_f, 'w') as f:
    for link in links:
        f.write(link+'\n')
