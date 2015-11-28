myDict = pickle.load(open("json_clusters_1_70.p", "rb"))
maxval = -1
for d in myDict:
    if 'street_address' in myDict[d]['results'][0]['types']:
        if int(d.split(',')[2]) > maxval:
            maxval = int(d.split(',')[2])
        if int(d.split(',')[2]) > 250:
#             pass
            print myDict[d]['results'][0]['formatted_address'].split(',')[0],':',float(d.split(',')[2])/4507
print maxval
