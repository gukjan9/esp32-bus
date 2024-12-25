import urequests as requests

def get_data(api, id):
    url = 'http://apis.data.go.kr/6410000/buslocationservice/getBusLocationList'
    full_url = url + "?serviceKey=" + api + "&routeId=" + id 

    response = requests.get(full_url)
    xml_data = response.content.decode('utf-8')
    
    return(xml_data)

def parse_xml(xml):
    tag = None
    value = None
    elements = []
    
    route_departure_seq = {
        '229000097': 21,
        '229000112': 8
    }

    in_tag = False
    for char in xml:
        if char == '<':
            in_tag = True
            if value and tag:
                elements.append((tag, value.strip()))
                value = None
            tag = ''
        elif char == '>':
            in_tag = False
            value = ''
        elif in_tag:
            tag += char
        else:
            value += char

    if value and tag:
        elements.append((tag, value.strip()))

    closest_seq = None
    query_time = None
    route_id = None
    station_seq = None

    for tag, val in elements:
        if tag == "queryTime":
            query_time = val
            print("query " + query_time)
        if tag == "routeId":
            route_id = val
            print("route_id " + route_id)
        if tag == "stationSeq":
            station_seq = val
            print("station_seq" + station_seq)
            if route_id in route_departure_seq:
                departure_seq = route_departure_seq[route_id]
                diff = int(departure_seq) - int(station_seq)
                if 0 <= diff <= departure_seq:
                    return query_time, diff
    
    return query_time, -1
