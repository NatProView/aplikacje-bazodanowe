file = open("wiersz", "r")
lines = file.readlines()
for x in lines:
    print(x.strip())
file.close()