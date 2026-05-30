a, b, c = 5.0, 10.0, 20.0
x, y = 12.0, 6.0

brick = sorted([a, b, c])
hole = sorted([x, y])

if brick[0] <= hole[0] and brick[1] <= hole[1]:
    print("Пройдет")
else:
    print("Не пройдет")