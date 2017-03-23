import urllib2
from bs4 import BeautifulSoup as BS
import pickle as pkl

in_file = 'ecotimes_urls.txt'
with open(in_file, 'r') as f:
    urls = [i.strip() for i in f.readlines()]

def save_pickle(ctr, hindu_data):
    print "Saving data collected till URL number", ctr
    with open(str(ctr)+'_eco_data.pkl', 'wb') as f:
        pkl.dump(hindu_data, f)

hindu_data = []
ctr = 0.0
for url in urls:
    print "[", (ctr*100)/len(urls), "] Parsing : ", url
    ctr+=1
    try:
        req = urllib2.Request(url, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        r = urllib2.urlopen(req).read()
        soup = BS(r, 'lxml')

        title = soup.find('h1', {'class':'title'}).contents[0].strip()
        try:
            author = soup.find('div', {'class':'byline'}).contents[0].strip().split('|')[0].strip().replace('By', '').strip()
        except:
            author = soup.find('div', {'class':'Normal'}).find('strong').contents[0]
        try:
            timeplace = soup.find('div', {'class':'byline'}).contents[0].strip().split('|')[1].strip().strip()
        except:
            timeplace = soup.find('div', {'class':'byline'}).contents[0].strip()
        content = ''
        for line in soup.find('div', {'class':'Normal'}).contents:
            try:
                content += line.contents[0]
            except:
                try:
                    content += line.strip()
                except:
                    content += ''
        content = content.strip()

        hindu_data.append({'title':title, 'author':author, 'timeplace':timeplace, 'content':content})
    except:
        print "         > Skipping"
        continue

    if ctr%10000 == 0:
        save_pickle(ctr, hindu_data)
