import urequests as requests

def get_data(api, id):
    url = 'http://apis.data.go.kr/6410000/buslocationservice/getBusLocationList'
    full_url = url + "?serviceKey=" + api + "&routeId=" + id 

    response = requests.get(full_url)
    print(response.content)