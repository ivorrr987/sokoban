import copy
import move
import show
import check
import processing
import slot

# 명령어에 따라 동작 수행
def exec_commands(map_list, map_list_init, commands, hole_loc, log, slots, i):
    move_commands = ['w', 'W', 'a', 'A', 's', 'd', 'D'] # 이동 관련된 명령어들. 'S'는 저장용으로 써야 하기 때문에 제외.

    while len(commands)>0: # 입력받은 명령어들을 순차적으로 처리
        if check.is_all_in(map_list): # 대기 중인 명령어가 있더라도 현재 스테이지를 깰 수 있는 상태면 바로 완료.
            return map_list, log, False, i

        if commands[0] in move_commands:
            map_list, success = move.update_map(map_list, commands[0], hole_loc)
            if success==True:
                print(f"(턴수: {len(log)})") # 턴수 출력
                log[len(log)] = map_list # 로그 생성
            commands.pop(0)
            
        elif commands[0] == 'r' or commands[0] == 'R': # 매 스테이지 시작마다 복사해두었던 지도 정보를 이용해 초기화 명령 실행.
            map_list= copy.deepcopy(map_list_init)
            show.show_basic_info(map_list)
            log.clear() # log를 초기화 (+턴수 초기화 효과)
            log = {0 : map_list}
            print("r: 지도를 리셋합니다")
            commands.pop(0)

        elif commands[0] == 'c':
            if check.check_possible(map_list)[0]:
                print("이동이 불가능한 공이 없습니다.")
            else: 
                print("이동이 불가능한 공이 있습니다. 리셋 혹은 종료를 권합니다")
                print("해당 공의 좌표는 다음과 같습니다")
                print(check.check_possible(map_list)[1])
            commands.pop(0)
        
        elif commands[0] == 'q' or commands[0] == 'Q': # 'quit' 명령어 입력 시 게임 종료.
            return map_list, log, True, i

        elif 49<= ord(commands[0]) and ord(commands[0])<=53: # 1~5의 숫자가 입력되었을 때
            slot.show_slot(slots, int(commands[0])-1)
            command = input()

            if command == 'S':
                slots[int(commands[0])-1] = copy.deepcopy(slot.save_slot(map_list, slots, int(commands[0])-1, log, i))
            elif command == 'L':
                map_list, log, i = slot.load_slot(slots, int(commands[0])-1)
            else:
                print("잘못된 입력입니다")
            
            commands.pop(0)

        else : # 올바른 명령이 아닐 시, 아무 동작 없이 command만 지움.
            print("올바른 명령이 아닙니다")
            commands.pop(0)
            
    return map_list, log, False, i


def input_command(): # 커맨드를 입력받아 알파벳만 list 변수에 저장 후 return
    print("SOKOBAN>", end=' ')
    commands = list(input().replace(" ",''))
    
    return commands


def finish_game():
    print("축하합니다. 모든 스테이지를 완료하셨습니다")


# 게임 시작
def start_game(stages):
    i=0

    slots = [[stages[0], {} , 0]]*5
    while i<len(stages):
    # for i in range(len(stages)): # 스테이지1부터 마지막 스테이지까지. 스테이지 지도 정보는 map.txt 내용 수정하여 설정할 수 있음.
        show.show_stage_info(stages[i], i+1) # 각 스테이지 정보 표시
        stage_init = copy.deepcopy(stages[i])
        hole_loc = processing.save_hole_loc(stage_init)
        
        log = {0 : stages[i]} # 턴수 출력과 추후 'undo' 명령을 위해
        quit = False
        while check.is_all_in(stages[i])==False and quit==False: ## 스테이지를 깰 때까지 반복. 'quit' 명령어 입력 시 스테이지 및 게임 종료.
            commands = input_command()
            stages[i], log, quit, i = exec_commands(stages[i], stage_init, commands, hole_loc, log, slots, i)
            
        if quit:
            print("게임을 종료합니다")
            break
        else:
            print(f"\n<Stage {i+1} Clear>\n")

        i+=1
    if quit==False:
        finish_game()
