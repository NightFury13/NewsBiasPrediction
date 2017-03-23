import urllib2
from bs4 import BeautifulSoup as BS

output_f = 'ecotimes_urls.txt'

links = []
day = 41640
for day in range(41640, 42006):
    print "Parsing %s of 365" % str(day-41639)
    try:
        req = urllib2.Request('http://economictimes.indiatimes.com/archivelist/year-2014,month-1,starttime-%d.cms' % day, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        r = urllib2.urlopen(req).read()
        soup = BS(r, 'lxml')

        link = ['http://economictimes.indiatimes.com'+i['href'] for i in soup.find('span', {'class':'pagetext'}).find_all('a')[3:]]    
        links += link
    except:
        print "         > Skipping", url

with open(output_f, 'w') as f:
    for link in links:
        f.write(link+'\n')
