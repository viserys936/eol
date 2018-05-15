import json
with open('list_count.txt') as f:
    dict1 = {}
    dict2 = {}
    for i in f:
        x = i.strip().split(':')
        if(x[0]=='0000'):
            dict1['0'] = x[1]
        else:
            dict1[x[0].lstrip('0')] = x[1]

    flag = 0
    for i in range(64):
        flag += 1
        for j in range(flag, 64):
            dict2[str(j*64+i)] = dict1[str(i*64+j)]


    flag = 0
    for i in range(1,64):
        flag += 1
        for j in range(flag):
            dict2[str(j*64+i)] = dict1[str(i*64+j)]

    for i in range(64):
        for j in range(64):
            if (i==j):
                dict2[str(i*64+j)] = dict1[str(i*64+j)]

with open('data3.json', 'w') as outfile:
    json.dump(dict2, outfile)

##with open('every_location_count.txt', 'w') as f:
##    r = [int(i) for i in dict2.keys()]
##    for i in sorted(r):
##        f.write(str(i)+":"+dict2[str(i)]+'\n')
