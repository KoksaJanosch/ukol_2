my_movies = [['How I Met Your Mother', 'Friends', 'Silicon Valley'],
    ['Family Guy', 'South Park', 'Rick and Morty'],
    ['Breaking Bad', 'Game of Thrones', 'The Wire']]

for sublist in my_movies:
    for movie_name in sublist:
        char_num = len(movie_name)
        print("The title " + movie_name + " is " + str(char_num) + " characters long.")

vlevo = 2
vpravo = 6
dole = 2
hore = 5
test_list = [[3, 4], [1, 2], [9, 1], [7, 5], [6, 3]]

for i in range(len(test_list)):
    x = (test_list[i][0])
    y = (test_list[i][1])
    print(x, y)

    if vlevo < x < vpravo and \
            dole < y < hore:
        print("pokračujem")
    else:
        print("přiřad cluster_id")
        test_list[i].append(i)

print(test_list)


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
