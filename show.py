import processing
import move

def show_basic_info(map_list): # 지도 데이터만 출력

    print()
    for row in map_list:
        print(''.join(row))
    

def show_additional_info(map_list): # 가로 크기, 구멍 수 등 추가적인 정보 출력

    print()
    print("가로 크기 :", len(map_list[0]))
    print("세로 크기 :", len(map_list))
    print("구멍 수 :", processing.count_hole(map_list))
    print("공의 수 :", processing.count_ball(map_list))
    print(f"플레이어 위치 : ({move.locate_player(map_list)[0]+1}, {move.locate_player(map_list)[1]+1})")


def get_stage_info(map_list, num): # 실제로 stage 정보를 출력하는 부분
    
    print(f"<<Stage {num}>>")
    show_basic_info(map_list)
    show_additional_info(map_list)


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


def show_stage_info(map_list, num): # 스테이지 번호와 지도 정보 출력
    print(f"Stage {num}")
    show_basic_info(map_list)