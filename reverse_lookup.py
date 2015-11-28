from geopy.geocoders import Nominatim
geolocator = Nominatim()
filenames = ['clusters_0_210.txt','clusters_1_100.txt','clusters_2_75.txt','clusters_21_250.txt','clusters_22_240.txt','clusters_23_260.txt']
for fil in filenames:
    f = open('data/address_'+fil,'w')
    path = 'data/'+fil
    for line in open(path,'r'):
        lat,longitude,density=line.split(',')
        point = lat,longitude
        location = geolocator.reverse(point)
        c = "{lat_val},{long_val},{density_val},{address_val}\n".format(lat_val=lat, long_val=longitude,density_val=density,address_val=location.address)
        f.write(c)
    f.close()
