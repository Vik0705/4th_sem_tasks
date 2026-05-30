flat_number = 14
flats_per_floor = 20 // 5

floor = (flat_number - 1) // flats_per_floor + 1
position = (flat_number - 1) % flats_per_floor + 1

print(floor)
print(position)