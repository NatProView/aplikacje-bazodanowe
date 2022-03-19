# L-lista liczb caªkowitych. Znajd¹ najmniejsz¡ brakuj¡c¡ liczb¦ dodatni¡. np dla listy
# [0,-10,1,3,-20] b¦dzie to 2

l = [15, -26, -4, -5, -3, -1, 1, 0, 2, 4, 6, 10]
l.sort()
print(l)

for number in range (l[-1] + 1):
    if number not in l:
        print(number)
        break
