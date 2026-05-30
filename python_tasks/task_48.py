num = int(input())
max_len = 1
current_len = 1
prev_digit = num % 10
num //= 10

while num > 0:
    digit = num % 10
    if digit == prev_digit:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 1
    prev_digit = digit
    num //= 10

print(max_len)