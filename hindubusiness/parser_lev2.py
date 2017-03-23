import urllib
from bs4 import BeautifulSoup as BS
import pickle as pkl

in_file = 'hindub_urls.txt'
with open(in_file, 'r') as f:
    urls = [i.strip() for i in f.readlines()]

hindub_data = []
for url in urls:
    print "Parsing", url
    try:
        r = urllib.urlopen(url).read()
        soup = BS(r, 'lxml')

        title = soup.find('h1', {'class':'detail-title'}).contents[0].strip()
        author = soup.find('span', {'class':'author'}).contents[0].strip()
        timeplace = soup.find('div', {'class':'article-dateline'}).find('span').contents[0].strip()
        content = '. '.join([i.contents[0] for i in soup.find_all('p', {'class':'body'})]).strip().replace('\n', '')

        hindub_data.append({'title':title, 'author':author, 'timeplace':timeplace, 'content':content})
    except:
        print "         > Skipping"
        continue

with open('hindubusiness_data.pkl', 'wb') as f:
    pkl.dump(hindub_data, f)
