import requests
import urlparse
from bs4 import BeautifulSoup

file_name = "600001-900000.txt"
file_name2 = "map_links.txt"
#file_name3 = "species_name.txt"
f = open(file_name, "r")
f2 = open(file_name2, "a")
#f3 = open(file_name3, "w")
count = 0
for link in f:
    link2 = link.replace('overview', 'maps').strip()
    #print link2
    rs = requests.get(link2)
    soup = BeautifulSoup(rs.text)
    tag  = soup.find('iframe')
    
    #name = soup.find('title')
    
    #<h2 title='Preferred common name for this taxon.'>
    name = soup.find('title')
    
    #print name.text.split(' - ')[0]   #common name
    if name.text.split(' - ')[2]=="Maps": 
        print name.text.split(' - ')[0].encode('utf-8')
        #f3.write(name.text.split(' - ')[0].encode('utf-8')+'\n')
        
    else:
        print 'None'
        #f3.write('None'+'\n')
        
    if tag:
        #print "*******There is a map!*******"
        f2.write(link.strip()+'*')
        f2.write(link2 + '\n')
    if not tag:
        #print "*******No map.*******"
        f2.write(link.strip()+ '\n')
    count += 1
    print 'count', count, '\n'
    if count == 2000:
        break
    
    
f.close()
f2.close()
#f3.close()
