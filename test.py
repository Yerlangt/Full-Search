def scale(object):
    import requests

    toponym_to_find = object

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        pass
    json_response = response.json()

    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    corner = toponym['boundedBy']['Envelope']
    low = corner['lowerCorner'].split()
    up = corner['upperCorner'].split()
    delta = [str(float(up[0]) - float(low[0])), str(float(up[1]) - float(low[1]))]

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join(delta),
        "l": "map"
    }
    return map_params
