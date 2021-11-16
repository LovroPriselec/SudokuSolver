#my first sudoku solver for 4x4 (not finished but works all almost every sudoku if you have any suggestions contact me)
n = 4
field = [list(map(int, input().split(" "))) for j in range(n)]
count = 0
for row in field:
    count += row.count(0)
print(count)

while count > 0:
    for i in range(n):
        for j in range(n):
            print(field)
            if field[i][j] == 0:
                possibilities = []
                square = []
                si = i - i%2 #start of mini square
                sj = j - j%2 #start of mini square
                for p in range(2):
                    for r in range(2):
                        square.append(field[p+si][p+sj])
                for k in range(1, n+1):
                    if k not in field[i] and k not in [field[l][j] for l in range(n)] and k not in square:
                        possibilities.append(k)
                if len(possibilities) == 1:
                    field[i][j] = possibilities[0]
                    count -= 1

for row in field:
    print(row)