list_items = ["pluto", "saturn", "uranus", "venus", "mars", "saturn", "neptune", "jupiter"]

iterator = iter(list_items)

for i in range(len(list_items)):
    print(next(iterator))
