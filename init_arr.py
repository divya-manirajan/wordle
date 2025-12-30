rows = 6
cols = 5

arr = [["[   ]" for col in range(cols)] for row in range(rows)]

for row in arr:
    print(*row)