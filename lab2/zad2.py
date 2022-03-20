def is_permutation(l1, l2):
    return set(l1) == set(l2)


l1 = ["test", "raz", 2]
l2 = [2, "test", "raz"]
l3 = [1,2,3]
l4 = [3,1,2]

print(is_permutation(l1, l2))
print(is_permutation(l3, l4))
print(is_permutation(l1, l3))