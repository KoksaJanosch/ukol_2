import math, json

# nacteni geojson
with open("points.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

features = data["features"]

def bounding_box():
    souradnice_list = []
    # vypiš z "features" všechny "coordinates" z kat. geometry
    for feat in data['features']:
        # přidej do seznamu
        souradnice_list.append(feat['geometry']['coordinates'])
    print("Původní seznam je: \n", souradnice_list)

    # seřaď seznam
    souradnice_list.sort(key=lambda x: x[0])
    print("Seřazený seznam je: \n", souradnice_list)

    # najdi maxima a minima
    vlevo = min(i[0] for i in souradnice_list)
    vpravo = max(i[0] for i in souradnice_list)
    dole = min(i[1] for i in souradnice_list)
    hore = max(i[1] for i in souradnice_list)
    print("\n BoundingBox: \n", "vlevo: ", vlevo, "\n", "vpravo: ", vpravo, "\n", "dole: ", dole, "\n", "hore: ", hore)

# QuadTree:
    # vypíš počet bodů ze seznamu:
    print("\n Počet bodů: \n", len(souradnice_list))

    # kolik bodů je v boxu:
    for i in range(len(souradnice_list)):
        x = (souradnice_list[i][0])
        y = (souradnice_list[i][1])
        print(x, y)

        if vlevo < x < vpravo and \
                dole < y < hore:
            print("pokračujem")
        else:
            print("přiřad cluster_id")


    # dokud nebude v boxu jen 1 bod, pokračuj:
    while len(vboxu) > 1: # pak předělat na 50
        # rozděl na poloviny
        mid_x = (vlevo + vpravo) / 2
        mid_y = (dole + hore) / 2
        print("\n mid_x", mid_x, "\n mid_y", mid_y)


    else:
        print("Přidám cluster_id")
       # data[properties][cluster_id] = +1

bounding_box()
