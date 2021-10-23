def nextMove(n,r,c,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                x_m, y_m = j, n-i-1
            elif grid[i][j] == 'p':
                x_p, y_p = j, n-i-1

    while x_m != x_p:
        if x_m > x_p:
            x_m-=1
            return "LEFT"
        else:
            x_m+=1
            return "RIGHT"
    while y_m != y_p:
        if y_m > y_p:
            y_m-=1
            return "DOWN"
        else:
            y_m+=1
            return "UP"

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
