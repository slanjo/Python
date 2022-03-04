import requests
import datetime
MY_LAT = -31.948666
MY_LONG = 115.807456
if __name__ == '__main__':
#    r = requests.get(url="http://api.open-notify.org/iss-now.json")
#    r.raise_for_status()
##    print(r)
#
##   print(r.headers)
##    print(r.headers['Content-Type'])
##    print(r.content)
#    data = r.json()
##    print(r.json())
##    print(data)    
#    lat = data['iss_position']['latitude']
#    lon = data['iss_position']['longitude']
#    lat_lon = (lat, lon)
#    print(f"lat+lon tupple = {lat_lon}")
#    print(f"lat={data['iss_position']['latitude']}, long={data['iss_position']['longitude']} timestamp={data['timestamp']}")
#
#
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }
    r = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    r.raise_for_status()
    data = r.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    print(data)
    print(f"SUNRISE: {sunrise} \nSUNSET: {sunset}")