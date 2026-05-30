num = int(input())
is_increasing = True
prev_digit = num % 10
num //= 10

while num > 0:
    digit = num % 10
    if digit >= prev_digit:
        is_increasing = False
        break
    prev_digit = digit
    num //= 10

if is_increasing:
    print("Да")
else:
    print("Нет")