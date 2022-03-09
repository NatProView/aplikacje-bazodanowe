class Pair:
    def __init__(self, text, number):
        self.text   = text
        self.number = number

texts = {"jeden", "dwa", "rozne rzeczy", "mleko"}
pairs = []

for x in texts:
    pairs.append(Pair(x, len(x)))

#print new array
for x in pairs:
    print(f"{x.text} | {x.number}")