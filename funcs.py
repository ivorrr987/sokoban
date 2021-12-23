import copy


def divide_stages(origin): # "====="로 stage 구분
    
    maps_str=origin.split("=====\n")

    return maps_str


def save(map_str): # 문자열 'stage_info'를 list로 변환하여 필요한 값만 저장
    
    map_str= map_str.split("\n")
    map_list= []
    for info in map_str:
        if 'Stage' not in info and info!='':
            map_list.append(list(info))
    
    return map_list


# map.txt 파일에서 문자열을 읽어옴
def open_file():
    with open("map.txt") as maps_file:
        origin = maps_file.read()
    
    return origin


# 문자열로 저장된 각 스테이지 정보를 2차원 배열로 변환.
def set_stages(maps_str):
    stages=[]

    for i in range(len(maps_str)):
        stages.append(save(maps_str[i]))

    return stages    


def locate_player(map_list): ## 플레이어 위치 확인
    
    for i in range(len(map_list)):
        if 'P' in map_list[i]:
            row = i
            col = map_list[i].index('P')
    
    return [row, col]


def count_ball(map_list): # 공의 개수 
    count=0
    for i in range(len(map_list)):
        count+= map_list[i].count('o')
    
    return count


def count_hole(map_list): # 구멍 개수
    count=0
    for i in range(len(map_list)):
        count+= map_list[i].count('O')
    
    return count


def show_basic_info(map_list): # 지도 데이터만 출력

    print()
    for row in map_list:
        print(''.join(row))
    

def show_additional_info(map_list): # 가로 크기, 구멍 수 등 추가적인 정보 출력

    print()
    print("가로 크기 :", len(map_list[0]))
    print("세로 크기 :", len(map_list))
    print("구멍 수 :", count_hole(map_list))
    print("공의 수 :", count_ball(map_list))
    print(f"플레이어 위치 : ({locate_player(map_list)[0]+1}, {locate_player(map_list)[1]+1})")


def get_stage_info(map_list, num): # 실제로 stage 정보를 출력하는 부분
    
    print(f"<<Stage {num}>>")
    show_basic_info(map_list)
    show_additional_info(map_list)


def input_command(): # 커맨드를 입력받아 알파벳만 list 변수에 저장 후 return
    print("SOKOBAN>", end=' ')
    commands = list(input().replace(" ",''))
    
    return commands


# 명령 수행이 불가할 시 맵 데이터와 에러 메세지 출력   
def show_fail(map_list):
    show_basic_info(map_list)
    print("[해당 명령을 수행할 수 없습니다]")

    return False


# 명령 수행에 성공했을 시 지도 정보와 메세지 출력
def show_success(map_list, command):
    show_basic_info(map_list)
    if command=='w':
        print("[w : 위쪽으로 이동합니다]")
    elif command=='a':
        print("[a : 왼쪽으로 이동합니다]")
    elif command=='s':
        print("[s : 아래쪽으로 이동합니다]")
    else:
        print("[d : 오른쪽으로 이동합니다]")
        

#이동하고자 하는 위치가 공백이거나 빈 구멍일 경우
def move_up(map_list, current_row, current_col, hole_loc):
    map_list[current_row-1][current_col] = 'P'
    map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
    show_success(map_list, 'w') 

    return map_list

def move_left(map_list, current_row, current_col, hole_loc):
    map_list[current_row][current_col-1] = 'P'
    map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
    show_success(map_list, 'a')

    return map_list

def move_down(map_list, current_row, current_col, hole_loc):
    map_list[current_row+1][current_col] = 'P'
    map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
    show_success(map_list, 's')

    return map_list

def move_right(map_list, current_row, current_col, hole_loc):
    map_list[current_row][current_col+1] = 'P'
    map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
    show_success(map_list, 'd')

    return map_list


# 플레이어가 있던 자리가 원래 구멍이었는지 아닌지에 따라 플레이어가 해당 자리에서 이동했을 때 해당 위치 정보(' ' or 'O') 표시.
def treat_hole(map_list, hole_loc, current_row, current_col): 
    if [current_row, current_col] in hole_loc:
        map_list[current_row][current_col] = 'O'
    else:
        map_list[current_row][current_col] = ' '

    return map_list[current_row][current_col]


# 플레이어가 이동하고자 하는 위치에 공이 놓여있어서 공을 밀어야 할 경우
def push_up(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row-2][current_col] == ' ':
        map_list[current_row-2][current_col] = 'o'
        map_list[current_row-1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 'w')
    elif map_list[current_row-2][current_col]== 'O':
        map_list[current_row-2][current_col] = '0'
        map_list[current_row-1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 'w')
    else:
        success = show_fail(map_list)

    return map_list, success

def push_left(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row][current_col-2] == ' ':
        map_list[current_row][current_col-2] = 'o'
        map_list[current_row][current_col-1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 'a')
    elif map_list[current_row][current_col-2]== 'O':
        map_list[current_row][current_col-2] = '0'
        map_list[current_row][current_col-1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 'a')
    else:
        success = show_fail(map_list)

    return map_list, success

def push_down(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row+2][current_col] == ' ':
        map_list[current_row+2][current_col] = 'o'
        map_list[current_row+1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list,'s')
    elif map_list[current_row+2][current_col]== 'O':
        map_list[current_row+2][current_col] = '0'
        map_list[current_row+1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list,'s')
    else:
        success =show_fail(map_list)

    return map_list, success

def push_right(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row][current_col+2] == ' ':
        map_list[current_row][current_col+2] = 'o'
        map_list[current_row][current_col+1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list,'d')
    elif map_list[current_row][current_col+2]== 'O':
        map_list[current_row][current_col+2] = '0'
        map_list[current_row][current_col+1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list,'d')
    else:
        success = show_fail(map_list)

    return map_list, success


# 0을 o과 O으로 분리하는 움직임일 때.
def take_out_up(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row-2][current_col] == ' ':
        map_list[current_row-2][current_col]='o'
        map_list[current_row-1][current_col]='P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 'w')
    elif map_list[current_row-2][current_col] == 'O':
        map_list[current_row-2][current_col] = '0'
        map_list[current_row-1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 'w')
    else:
        success = show_fail(map_list)

    return map_list, success
        
def take_out_left(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row][current_col-2] == ' ':
        map_list[current_row][current_col-2]='o'
        map_list[current_row][current_col-1]='P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 'a')
    elif map_list[current_row][current_col-2] == 'O':
        map_list[current_row][current_col-2] = '0'
        map_list[current_row][current_col-1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 'a')
    else:
        success = show_fail(map_list)

    return map_list, success

def take_out_down(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row+2][current_col] == ' ':
        map_list[current_row+2][current_col]='o'
        map_list[current_row+1][current_col]='P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 's')
    elif map_list[current_row+2][current_col] == 'O':
        map_list[current_row+2][current_col] = '0'
        map_list[current_row+1][current_col] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 's')
    else:
        success = show_fail(map_list)

    return map_list, success
    
def take_out_right(map_list, current_row, current_col, hole_loc):
    success = True
    if map_list[current_row][current_col+2] == ' ':
        map_list[current_row][current_col+2]='o'
        map_list[current_row][current_col+1]='P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 'd')
    elif map_list[current_row][current_col+2] == 'O':
        map_list[current_row][current_col+2] = '0'
        map_list[current_row][current_col+1] = 'P'
        map_list[current_row][current_col] = treat_hole(map_list, hole_loc, current_row, current_col)
        show_success(map_list, 'd')
    else:
        success = show_fail(map_list)

    return map_list, success


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
            success = show_fail(map_list)
            
    elif command=='a' or command== 'A':
        if map_list[current_row][current_col-1] == ' ' or map_list[current_row][current_col-1] == 'O':
            map_list = move_left(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row][current_col-1] == 'o':
            map_list, success = push_left(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row][current_col-1] == '0':
            map_list, success = take_out_left(map_list, current_row, current_col, hole_loc)
        else:
            success = show_fail(map_list)
            
    elif command=='s':
        if map_list[current_row+1][current_col] == ' ' or map_list[current_row+1][current_col] == 'O':
            map_list = move_down(map_list, current_row, current_col, hole_loc)    
        elif map_list[current_row+1][current_col] == 'o':
            map_list, success = push_down(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row+1][current_col] == '0':
            map_list, success = take_out_down(map_list, current_row, current_col, hole_loc)
        else:
            success = show_fail(map_list)
            
    elif command=='d' or command == 'D':
        if map_list[current_row][current_col+1] == ' ' or map_list[current_row][current_col+1] == 'O':
            map_list = move_right(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row][current_col+1] == 'o':
            map_list, success = push_right(map_list, current_row, current_col, hole_loc)
        elif map_list[current_row][current_col+1] == '0':
            map_list, success = take_out_right(map_list, current_row, current_col, hole_loc)
        else:
            success = show_fail(map_list)

    return map_list, success


def show_stage_info(map_list, num): # 스테이지 번호와 지도 정보 출력
    print(f"Stage {num}")
    show_basic_info(map_list)


def save_hole_loc(map_list): # 스테이지 시작 시 구멍의 위치를 저장
    hole_loc = [[i,j] for i in range(len(map_list)) for j in range(len(map_list[0])) if map_list[i][j]=='O' or map_list[i][j]=='0']
    
    return hole_loc


# 아직 실행되지 않은 commands가 있어도 모든 공이 구멍에 들어가면 해당 stage 종료
def is_all_in(map_list):
    check = True
    for row in map_list:
        if 'o' in row:
            check = False
            break

    return check


# 서로 마주보는 두 방향이 뚫려있는지 검사('상-하', '좌-우')
def check_sides(map_list, row, col):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    symbols = [' ', 'O', 'P']
    
    if map_list[row+dy[0]][col+dx[0]] in symbols and map_list[row+dy[2]][col+dx[2]] in symbols:
        return True
    elif map_list[row+dy[1]][col+dx[1]] in symbols and map_list[row+dy[3]][col+dx[3]] in symbols:
        return True

    return False

def check_possible(map_list): ## 현재 지도 정보에서 구멍에 들어가지 않은 공 중에 이동이 불가능한 공이 있는지 확인.
    balls = [[i,j] for i in range(len(map_list)) for j in range(len(map_list[0])) if map_list[i][j]=='o']
    
    impossibles =[]
    for ball in balls:
        if check_sides(map_list ,ball[0], ball[1])==False:
            impossibles.append([ball[0], ball[1]])

    return (True, impossibles) if len(impossibles)==0 else (False, impossibles)


def show_slot(slots, number):
    print(f"Slot {number+1}")
    print(slots[number])
    print()
    print("'S(Save)' 혹은 'L(Load)'를 입력하세요 >", end=' ')


def save_slot(map_list, slots, number):
    slots[number] = map_list
    return slots[number]


def load_slot(slots, number):
    show_basic_info(slots[number])

# 명령어에 따라 동작 수행
def exec_commands(map_list, map_list_init, commands, hole_loc, log, slots):
    move_commands = ['w', 'W', 'a', 'A', 's', 'd', 'D'] # 이동 관련된 명령어들. 'S'는 저장용으로 써야 하기 때문에 제외.

    while len(commands)>0: # 입력받은 명령어들을 순차적으로 처리
        if is_all_in(map_list): # 대기 중인 명령어가 있더라도 현재 스테이지를 깰 수 있는 상태면 바로 완료.
            return map_list, log, False

        if commands[0] in move_commands:
            map_list, success = update_map(map_list, commands[0], hole_loc)
            if success==True:
                print(f"(턴수: {len(log)})") # 턴수 출력
                log[len(log)] = map_list # 로그 생성
            commands.pop(0)
            
        elif commands[0] == 'r' or commands[0] == 'R': # 매 스테이지 시작마다 복사해두었던 지도 정보를 이용해 초기화 명령 실행.
            map_list= copy.deepcopy(map_list_init)
            show_basic_info(map_list)
            log.clear() # log를 초기화 (+턴수 초기화 효과)
            log = {0 : map_list}
            print("r: 지도를 리셋합니다")
            commands.pop(0)

        elif commands[0] == 'c':
            if check_possible(map_list)[0]:
                print("이동이 불가능한 공이 없습니다.")
            else: 
                print("이동이 불가능한 공이 있습니다. 리셋 혹은 종료를 권합니다")
                print("해당 공의 좌표는 다음과 같습니다")
                print(check_possible(map_list)[1])
            commands.pop(0)
        
        elif commands[0] == 'q' or commands[0] == 'Q': # 'quit' 명령어 입력 시 게임 종료.
            return map_list, log, True

        # elif 1<= int(commands[0]) and int(commands[0])<=5:
        #     show_slot(slots, int(commands[0])-1)
        #     command = input()
        #     if command == 'S':
        #         slots[int(commands[0])-1] = save_slot(map_list, slots, int(commands[0])-1)
        #     elif command == 'L':


        else : # 올바른 명령이 아닐 시, 아무 동작 없이 command만 지움.
            print("올바른 명령이 아닙니다")
            commands.pop(0)
            
    return map_list, log, False


def finish_game():
    print("축하합니다. 모든 스테이지를 완료하셨습니다")


# 게임 시작
def start_game(stages):
    for i in range(len(stages)): # 스테이지1부터 마지막 스테이지까지. 스테이지 지도 정보는 map.txt 내용 수정하여 설정할 수 있음.
        show_stage_info(stages[i], i+1) # 각 스테이지 정보 표시
        stage_init = copy.deepcopy(stages[i])
        hole_loc = save_hole_loc(stage_init)
        
        log = {0 : stages[i]} # 턴수 출력과 추후 'undo' 명령을 위해
        quit = False
        slots = [None]*5
        while is_all_in(stages[i])==False and quit==False: ## 스테이지를 깰 때까지 반복. 'quit' 명령어 입력 시 스테이지 및 게임 종료.
            commands = input_command()
            stages[i], log, quit=exec_commands(stages[i], stage_init, commands, hole_loc, log, slots)
            
        if quit:
            print("게임을 종료합니다")
            break
        else:
            print(f"\n<Stage {i+1} Clear>\n")

    if quit==False:
        finish_game()



