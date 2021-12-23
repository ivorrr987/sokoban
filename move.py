import show

def locate_player(map_list): ## 플레이어 위치 확인
    
    for i in range(len(map_list)):
        if 'P' in map_list[i]:
            row = i
            col = map_list[i].index('P')
    
    return [row, col]


#이동하고자 하는 위치가 공백이거나 빈 구멍일 경우
def move_up(map_list, current_row, current_col, hole_loc):
    map_list[current_row-1][current_col] = 'P'
    map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
    show.show_success(map_list, 'w') 

    return map_list

def move_left(map_list, current_row, current_col, hole_loc):
    map_list[current_row][current_col-1] = 'P'
    map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
    show.show_success(map_list, 'a')

    return map_list

def move_down(map_list, current_row, current_col, hole_loc):
    map_list[current_row+1][current_col] = 'P'
    map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
    show.show_success(map_list, 's')

    return map_list

def move_right(map_list, current_row, current_col, hole_loc):
    map_list[current_row][current_col+1] = 'P'
    map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
    show.show_success(map_list, 'd')

    return map_list

# 플레이어가 이동하고자 하는 위치에 공이 놓여있어서 공을 밀어야 할 경우
def push_up(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row-2][current_col] == ' ':
        map_list[current_row-2][current_col] = 'o'
        map_list[current_row-1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 'w')
    elif map_list[current_row-2][current_col]== 'O':
        map_list[current_row-2][current_col] = '0'
        map_list[current_row-1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 'w')
    else:
        success = show.show_fail(map_list)

    return map_list, success

def push_left(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row][current_col-2] == ' ':
        map_list[current_row][current_col-2] = 'o'
        map_list[current_row][current_col-1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 'a')
    elif map_list[current_row][current_col-2]== 'O':
        map_list[current_row][current_col-2] = '0'
        map_list[current_row][current_col-1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 'a')
    else:
        success = show.show_fail(map_list)

    return map_list, success

def push_down(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row+2][current_col] == ' ':
        map_list[current_row+2][current_col] = 'o'
        map_list[current_row+1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list,'s')
    elif map_list[current_row+2][current_col]== 'O':
        map_list[current_row+2][current_col] = '0'
        map_list[current_row+1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list,'s')
    else:
        success=show.show_fail(map_list)

    return map_list, success

def push_right(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row][current_col+2] == ' ':
        map_list[current_row][current_col+2] = 'o'
        map_list[current_row][current_col+1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list,'d')
    elif map_list[current_row][current_col+2]== 'O':
        map_list[current_row][current_col+2] = '0'
        map_list[current_row][current_col+1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list,'d')
    else:
        success = show.show_fail(map_list)

    return map_list, success


# 0을 o과 O으로 분리하는 움직임일 때.
def take_out_up(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row-2][current_col] == ' ':
        map_list[current_row-2][current_col]='o'
        map_list[current_row-1][current_col]='P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 'w')
    elif map_list[current_row-2][current_col] == 'O':
        map_list[current_row-2][current_col] = '0'
        map_list[current_row-1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 'w')
    else:
        success = show.show_fail(map_list)

    return map_list, success
        
def take_out_left(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row][current_col-2] == ' ':
        map_list[current_row][current_col-2]='o'
        map_list[current_row][current_col-1]='P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 'a')
    elif map_list[current_row][current_col-2] == 'O':
        map_list[current_row][current_col-2] = '0'
        map_list[current_row][current_col-1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 'a')
    else:
        success = show.show_fail(map_list)

    return map_list, success

def take_out_down(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row+2][current_col] == ' ':
        map_list[current_row+2][current_col]='o'
        map_list[current_row+1][current_col]='P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 's')
    elif map_list[current_row+2][current_col] == 'O':
        map_list[current_row+2][current_col] = '0'
        map_list[current_row+1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 's')
    else:
        success = show.show_fail(map_list)

    return map_list, success
    
def take_out_right(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row][current_col+2] == ' ':
        map_list[current_row][current_col+2]='o'
        map_list[current_row][current_col+1]='P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 'd')
    elif map_list[current_row][current_col+2] == 'O':
        map_list[current_row][current_col+2] = '0'
        map_list[current_row][current_col+1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show.show_success(map_list, 'd')
    else:
        success = show.show_fail(map_list)

    return map_list, success


# 플레이어가 있던 자리가 원래 구멍이었는지 아닌지에 따라 플레이어가 해당 자리에서 이동했을 때 해당 위치 정보(' ' or 'O') 표시.
def treat_hole(map_list, hole_loc, current_row, current_col): 
    if [current_row, current_col] in hole_loc:
        map_list[current_row][current_col] = 'O'
    else:
        map_list[current_row][current_col] = ' '

    return map_list[current_row][current_col]


# map 정보를 커맨드에 따라 갱신.
def update_map(map_list, command, hole_loc): 

    current_row = locate_player(map_list)[0]
    current_col = locate_player(map_list)[1]
    success = True

    if command=='w' or command=='W':
        if map_list[current_row-1][current_col] == ' ' or map_list[current_row-1][current_col] == 'O': # 공백일 경우 P 위치 변경
            map_list = move_up(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row-1][current_col] == 'o':
            map_list, success = push_up(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row-1][current_col] == '0':
            map_list, success = take_out_up(map_list, current_row, current_col, hole_loc)
        else:
            success = show.show_fail(map_list)
            
    elif command=='a' or command== 'A':
        if map_list[current_row][current_col-1] == ' ' or map_list[current_row][current_col-1] == 'O':
            map_list = move_left(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row][current_col-1] == 'o':
            map_list, success = push_left(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row][current_col-1] == '0':
            map_list, success = take_out_left(map_list, current_row, current_col, hole_loc)
        else:
            success = show.show_fail(map_list)
            
    elif command=='s':
        if map_list[current_row+1][current_col] == ' ' or map_list[current_row+1][current_col] == 'O':
            map_list = move_down(map_list, current_row, current_col, hole_loc)    
        elif map_list[current_row+1][current_col] == 'o':
            map_list, success = push_down(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row+1][current_col] == '0':
            map_list, success = take_out_down(map_list, current_row, current_col, hole_loc)
        else:
            success = show.show_fail(map_list)
            
    elif command=='d' or command == 'D':
        if map_list[current_row][current_col+1] == ' ' or map_list[current_row][current_col+1] == 'O':
            map_list = move_right(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row][current_col+1] == 'o':
            map_list, success = push_right(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row][current_col+1] == '0':
            map_list, success = take_out_right(map_list, current_row, current_col, hole_loc)
        else:
            success = show.show_fail(map_list)

    return map_list, success