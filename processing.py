def divide_stages(origin): # "====="로 stage 구분
            
    return origin.split("---\n")


def save(map_str): # 문자열 'stage_info'를 list로 변환하여 필요한 값만 저장
    
    map_str= map_str.split("\n")
    map_list= []
    for info in map_str:
        if 'Stage' not in info and info!='':
            map_list.append(list(info))
    
    return map_list


# map.txt 파일에서 문자열을 읽어옴
def open_file(filename):
    with open(filename) as maps_file:
        origin = maps_file.read()
    
    return origin


# 문자열로 저장된 각 스테이지 정보를 2차원 배열로 변환.
def set_stages(maps_str):
    stages=[]

    for i in range(len(maps_str)):
        stages.append(save(maps_str[i]))

    return stages    


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


def save_hole_loc(map_list): # 스테이지 시작 시 구멍의 위치를 저장
    hole_loc = [[i,j] for i in range(len(map_list)) for j in range(len(map_list[0])) if map_list[i][j]=='O' or map_list[i][j]=='0']
    
    return hole_loc