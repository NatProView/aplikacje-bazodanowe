songs = {
    "song 1": 1,
    "song 2": 2,
    "song 3": 3,
    "song 4": 4,
    "song 5": 5,
    "song 6": 5,
    "song 7": 3
}

for song, score in songs.items():
    if score == 5:
        print(song);