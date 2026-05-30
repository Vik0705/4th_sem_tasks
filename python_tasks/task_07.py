x1, y1 = 0, 0
x2, y2 = 0, 4
x3, y3 = 5, 5
x4, y4 = 6, 0

def triangle_area(x_a, y_a, x_b, y_b, x_c, y_c):
    return abs(0.5 * (x_a*(y_b - y_c) + x_b*(y_c - y_a) + x_c*(y_a - y_b)))

area1 = triangle_area(x1, y1, x2, y2, x3, y3)
area2 = triangle_area(x1, y1, x3, y3, x4, y4)

print(area1 + area2)