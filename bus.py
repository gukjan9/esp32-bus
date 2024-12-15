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

    query_time = None
    first_station_id = None
    for tag, val in elements:
        if tag == "queryTime":
            query_time = val
        elif tag == "stationId" and first_station_id is None:
            first_station_id = val
            break

    return query_time, first_station_id