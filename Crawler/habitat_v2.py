"""retrieve habitats and population trend"""
import requests
from bs4 import BeautifulSoup


F0 = open('70001-140000.txt', 'r')
F1 = open('habitat.txt', 'a')

COUNT = 0

for i in F0:
    habitats = []
    url = ""
    item_number = 0
    habitat_status = ""
    extinction_status = ""

    url = i.split('*')[1].strip().replace('maps', 'data')
    #print url
    location = url.find('pages/') + 6
    item_number = url.strip('/data')[location:]
    #print item_number

    while True:
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text.encode('utf-8'))
            temp_table = soup.findAll('table', {'class': 'standard categorized data'})

            #print len(temp_table)
            F1.write(item_number)
            if len(temp_table) > 0:
                for t in temp_table:
                    if t.find('th', {'class': 'predicate'}).find('dt'):
                        habitat_status = t.find('th', {'class': 'predicate'\
                                                       }).find('dt').contents[0].strip() \
                                                       == 'habitat'
                    if habitat_status:
                        ls = t.findAll('span', {'class': 'term'})

                        for j in ls:
                            ls1 = j.find('dt')
                            if ls1:
                                habitats.append(ls1.contents[0])
                        for j in habitats:
                            F1.write('*'+j.strip().encode('utf-8'))
                    else:
                        status = t.findAll('dt')
                        if status:
                            for i in status:
                                if i.contents[0].strip() == 'population trend':
                                    pop = t.find('td', {'class':'val'}).find\
                                          ('span', {'class':'term'}).contents[0]\
                                          .strip()
                                    F1.write('@'+pop.encode('utf-8'))
            break
        except requests.ConnectionError:
            print "connection error"
            continue
    if url:
        F1.write('\r\n')
    COUNT += 1
    if COUNT >= 10104:
        break

F0.close()
F1.close()

