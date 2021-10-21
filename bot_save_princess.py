#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    x_m,y_m = (m-1)/2, (m-1)/2
    if grid[0][0] == "p":
        x_p,y_p = 0,0
    elif grid[0][-1] == "p":
        x_p,y_p = m-1,0
    elif grid[-1][0] == "p":
        x_p,y_p = 0,m-1
    elif grid[-1][-1] == "p":
        x_p,y_p = m-1,m-1

    while x_m != x_p:
        if x_m > x_p:
            print('LEFT')
            x_m-=1
        else:
            print('RIGHT')
            x_m+=1

    while y_m != y_p:
        if y_m > y_p:
            print('UP')
            y_m-=1
        else:
            print('DOWN')
            y_m+=1
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
