x1, y1, w1, h1 = 0, 0, 10, 10
x2, y2, w2, h2 = 2, 2, 5, 5

r1_r, r1_t = x1 + w1, y1 + h1
r2_r, r2_t = x2 + w2, y2 + h2

a_in_b = (x1 >= x2) and (y1 >= y2) and (r1_r <= r2_r) and (r1_t <= r2_t)
b_in_a = (x2 >= x1) and (y2 >= y1) and (r2_r <= r1_r) and (r2_t <= r1_t)
intersect = not (r1_r < x2 or r2_r < x1 or r1_t < y2 or r2_t < y1)

print(a_in_b)
print(a_in_b or b_in_a)
print(intersect)