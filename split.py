import math, json

# nacteni geojson
with open ("points.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)


def sort_points():
    a = []
    for feat in data['features']:
        a.append(feat['geometry']['coordinates'])
        a.sort()
    print(a)

sort_points()
