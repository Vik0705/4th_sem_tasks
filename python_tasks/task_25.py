year = 2026

animals = ["Крыса", "Корова", "Тигр", "Заяц", "Дракон", "Змея", 
           "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья"]
colors = ["Зелен", "Красн", "Желт", "Бел", "Черн"]

offset = year - 1984
animal = animals[offset % 12]
color_base = colors[(offset % 10) // 2]

if animal in ("Крыса", "Корова", "Змея", "Лошадь", "Овца", "Обезьяна", "Собака", "Свинья"):
    color = color_base + "ая"
else:
    color = color_base + "ый"

print(f"{animal}, {color}")