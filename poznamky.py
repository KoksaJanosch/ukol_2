# vypíš počet bodů ze seznamu:
print("\n Počet bodů: \n", len(souradnice_list))


for i in range(len(souradnice_list)):
    x = (souradnice_list[i][0])
    y = (souradnice_list[i][1])
    print(x, y)

    if vlevo <= x <= vpravo and \
            dole <= y <= hore:
        print("pokračujem")
    else:
        print("přiřad cluster_id")
