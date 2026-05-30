h, m, s = 5, 30, 0

total_seconds = (h % 12) * 3600 + m * 60 + s
angle = total_seconds * (360 / 43200)

print(angle)