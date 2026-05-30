a, b = 4, 4
c, d = 5, 5

rook = (a == c) or (b == d)
bishop = abs(a - c) == abs(b - d)
king = abs(a - c) <= 1 and abs(b - d) <= 1
queen = rook or bishop
pawn_move = (a == c) and (d - b == 1)
pawn_capture = abs(a - c) == 1 and (d - b == 1)

print("Ладья:", rook)
print("Слон:", bishop)
print("Король:", king)
print("Ферзь:", queen)
print("Пешка (ход):", pawn_move)
print("Пешка (взятие):", pawn_capture)