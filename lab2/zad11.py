l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [1, 5, 10]
l3 = [1, 3, 5, 7, 9, 11, 13]

print([x for x in l1 if x in l2 if x in l3])