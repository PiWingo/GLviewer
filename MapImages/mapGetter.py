import urllib.request

URL = 'http://pkinoko.web.fc2.com/ro/bb/'

f = open('allMaps.txt')
allMaps = f.read().splitlines()
for map in allMaps:
    print('getting map:' + map)
    fullURL = URL + map + '.gif'
    mapFilename = map + '.png'
    try:
        urllib.request.urlretrieve(fullURL, mapFilename)
    except:
        print('error gettin map: ' + map)
