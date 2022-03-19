# L- lista zawieraj¡ca liczby, uªo»one w porz¡dku niemalej¡cym. Czy liczba x nale»y do
# listy? Rozwi¡» zadanie za pomoc¡ przeszukiwania binarnego.
def binary_search(array, x):
    low, mid, high = 0, 0, len(array) - 1

    while low <= high:
        mid = (high + low) // 2
        if array[mid] < x:
            low = mid + 1
        elif array[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

l = []

for n in range(100):
    l.append(n + 10)

print(binary_search(l, 66))