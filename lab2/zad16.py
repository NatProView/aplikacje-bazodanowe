# Dane s¡ krotki
# tuple1 = (1,2,3,4)
# tuple2 = (5,6,7,8)
# Czy potrasz je zamieni¢? Spodziewany wynik:
# tuple1 = (5,6,7,8)
# tuple2 = (1,2,3,4)

tuple1 = (1,2,3,4)
tuple2 = (5,6,7,8)

temp = tuple1
tuple1 = tuple2 
tuple2 = temp

print(f"tuple1: {tuple1} \ttuple2: {tuple2}")