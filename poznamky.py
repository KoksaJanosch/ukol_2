# find max and min:

test_list = [[3, 7, 6], [1, 3, 5], [9, 3, 2]]

## option 1: pro každý index co seznam má
res = [min(idx) for idx in zip(*test_list)]
print("The Minimum of each index list is : " + str(res))

## option 2: pro index, který chceme
a_min = min(i[0] for i in test_list)
[i[0] for i in test_list if i[1] == a_min and i[0] > 10000] + [a_min]
print(a_min)


### Sketch:
# urči území indexu (1,2)


if POINT [0] > vlevo and \
   POINT [0] < vpravo and \
   POINT [1] > dole and \
   POINT [1] < hore:
    print(POINT, "nachází se v BB")

for bod in test_list:
    for index in bod:
        if test_list[my_index][O] >= vlevo:
            print("To je ono!")
        else:
            print("Kua")