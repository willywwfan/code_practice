def next_move(posr, posc, board):
    x_b, y_b = posr, posc
    x_d_list, y_d_list = [], []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                y_d_list.append(j)
                x_d_list.append(i)
    # print(x_b, y_b)
    # print(x_d_list, y_d_list)

    def calculate_distance(x_b,y_b,x_d,y_d):
        return (abs(x_d-x_b)**2 + abs(y_d-y_b)**2)**0.5
    d_distance_list = []
    for i in range(len(x_d_list)):
        d_distance_list.append(calculate_distance(x_b,y_b,x_d_list[i],y_d_list[i]))
    # print(d_distance_list)
    min_distance = min(d_distance_list)
    target_index = d_distance_list.index(min_distance)
    # print(target_index)
    x_target, y_target = x_d_list[target_index],y_d_list[target_index]
    # print(x_target, y_target)
    if x_b != x_target:
        if x_b > x_target:
            x_b-=1
            # return "UP"
            print("UP")
        else:
            x_b+=1
            # return "DOWN"
            print("DOWN")
    elif y_b != y_target:
        if y_b > y_target:
            y_b-=1
            # return "LEFT"
            print("LEFT")
        else:
            y_b+=1
            # return "RIGHT"
            print("RIGHT")
    # return "CLEAN"
    else:
        print("CLEAN")

n = 5
# r,c = [int(i) for i in input().strip().split()]
r,c = 3,2
grid = []
grid = ["b---d", "-d--d", "--dd-", "--d--", "----d"]
# for i in range(0, n):
#     grid.append(input())
next_move(r,c,grid)
