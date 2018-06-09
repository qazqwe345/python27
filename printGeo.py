import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')

def printRecord(tgt):
    rec = gi.record_by_addr(tgt)
    city = rec['city']
    region = rec['region_code']
    country = rec['country_name']
    lon = rec['longitude']
    lat = rec['latitude']
    print('[*]Target:' + tgt + 'geo_located.')
    print('[+]'+str(city)+','+str(region)+','+str(country))
    print('[+]Latitude:'+str(lat)+',Longitude:'+str(lon))

tgt = '140.114.200.28'
printRecord(tgt)
