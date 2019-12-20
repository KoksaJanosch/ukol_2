# initializing list 

test_list = [[3, 7, 6], [1, 3, 5], [9, 3, 2]]

res = [min(idx) for idx in zip(*test_list)]
print("The Minimum of each index list is : " + str(res))


a_min = min(i[0] for i in test_list)
[i[0] for i in test_list if i[1] == a_min and i[0] > 10000] + [a_min]
print(a_min)