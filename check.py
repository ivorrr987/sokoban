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
    
    for i in range(3):
        if map_list[row+dy[i]][col+dx[i]]=='#' and map_list[row+dy[i+1]][col+dx[i+1]]=='#':
            return False
    
    if map_list[row+dy[3]][col+dx[3]]=='#' and map_list[row+dy[0]][col+dx[0]]=='#':
        return False

    return True

def check_possible(map_list): ## 현재 지도 정보에서 구멍에 들어가지 않은 공 중에 이동이 불가능한 공이 있는지 확인.
    balls = [[i,j] for i in range(len(map_list)) for j in range(len(map_list[0])) if map_list[i][j]=='o']
    
    impossibles =[]
    for ball in balls:
        if check_sides(map_list ,ball[0], ball[1])==False:
            impossibles.append([ball[0], ball[1]])

    return (True, impossibles) if len(impossibles)==0 else (False, impossibles)
