import urllib
from bs4 import BeautifulSoup as BS
import pickle as pkl

in_file = 'hindu_urls.txt'
with open(in_file, 'r') as f:
    urls = [i.strip() for i in f.readlines()]

hindu_data = []
for url in urls:
    print "Parsing", url
    try:
        r = urllib.urlopen(url).read()
        soup = BS(r, 'lxml')

        title = soup.find('h1', {'class':'title'}).contents[0].strip()
        author = soup.find('a', {'class':'auth-nm'}).contents[0].strip()
        timeplace = soup.find('div', {'class':'mobile-ut-container'}).find_all('span')[0].contents[0].strip()+' '+soup.find('div', {'class':'mobile-ut-container'}).find('none').contents[0].strip()
        content = '. '.join([i.contents[0] for i in soup.find('div', {'class':'article-topics-container'}).findNext('div').find_all('p')])

        hindu_data.append({'title':title, 'author':author, 'timeplace':timeplace, 'content':content})
    except:
        print "         > Skipping"
        continue

with open('hindu_data.pkl', 'wb') as f:
    pkl.dump(hindu_data, f)
