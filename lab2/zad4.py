def replace(d, v, e):
    for key, value in d.items():
        if value == v:
            d[key] = e


dict = {1: 2, 3: 4, 5: 7}

print(dict)
print("\n")
replace(dict, 2, 10)
print(dict)