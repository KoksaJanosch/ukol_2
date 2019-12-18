import math, json

# nacteni geojson
with open ("points.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)


def sort_points():
    a = []
    for feat in data['features']:
        a.append(feat['geometry']['coordinates'])
    print("Původní seznam je: \n", a)
    a.sort(key=lambda x: x[0])
    print("Seřazený seznam je: \n",a)
sort_points()

