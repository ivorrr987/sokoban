# SOKOBAN 게임

(과제로 만들었던 소코반 게임을 조금 다듬었다.)

<https://namu.wiki/w/소코반>
한번쯤 접해봤을만한 간단한 게임이다.

공(박스)를 구멍(목표지점)에 모두 넣는 것을 목표로 한다.
벽 등에 가로막히면 이동할 수 없기 때문에 어느정도 루트를 생각해둘 필요가 있다.

## 게임 방법
- 커맨드를 입력하여 할당된 동작을 수행한다.
  - w : UP
  - a : LEFT
  - s : DOWN
  - d : RIGHT
  - r : RESET
  - q : QUIT 


# 구현 과정 상세 설명


## 1단계
- **step1.py**
### (revision : 2)
#### 1. 제시된 내용을 문자열로 넘겨 처리하는 함수를 작성
- 변수 map_data에 입력하고자 하는 내용을 문자열로 받는다.
#### 2. 2차원 배열로 변환 저장
- 문제에서 제시된 '#:0', 'O:1' 등의 변환 과정은 나중에 stage 지도 정보를 출력할 때 다시 역변환 과정을 거쳐야 하므로 필요없다고 판단, 생략하였다.
- 함수 'divide_stages': "=====\n"로 stage를 구분하여 각 스테이지 별 정보를 list에 저장했다.
- 'save' 함수를 이용해 변수 stage1, stage2에 각각 해당 stage의 지도 정보만을 2차원 배열로 담았다.
#### 3. 출력
- 'get_stage_info'를 이용하여 각 stage 별 정보를 출력
  -  출력되는 정보는 'stage 번호', '지도', '가로 크기', '세로 크기', '구멍 수', '공 수', '플레이어 위치'이다.
  - 스테이지 구분선은 출력하지 않는다.

### (revision : 3)
#### 함수 'step1' 제거

### (revision : 4)
#### step1.py 내의 함수들 funcs.py로 분리.(일부 함수를 다른 step 파일에서도 공유하기 위해)

### (revision : 5)
#### step1.py, funcs.py, README.md 수정

### (revision : 6)
#### README.md 수정

#### 실행 결과
아래 'step1_result.png' 파일 참조

## 2단계
- **step2.py**
### (revision : 7)
#### STEP 1의 stage2 지도 정보를 가져와서 출력
#### 커맨드들을 입력받고 입력받은 순서에 따라 플레이어 이동
- 어떠한 물체에 가로막혀 있는 곳으로는 이동할 수 없음
  - 지도 정보 그대로 유지
  - "명령 수행 불가능"을 메세지로 출력
- 가로막히지 않은 곳(공백)으로는 이동할 수 있음
  - w,a,s,d 각 커맨드에 따라 적절히 이동
- 'q' 입력 시 게임 종료

### (revision : 8)
#### (funcs.py) 함수 'update_map' 코드 순서 수정 

### (revision : 9)
#### README.md 수정

### (revision : 10)
#### 실행 결과 이미지 파일 추가, README.md 수정

### (revision : 11)
#### README.md 누락된 부분 추가

#### 실행 결과 
'step2_result.png' 참조

## 3단계
- **sokoban.py**
### (revision : 12)
#### map.txt 파일 생성 (stage 1~2까지만)
- map.txt의 내용을 문자열로 읽어올 수 있음.
- 해당 map은 문제 링크의 SOKOBAN 게임 스테이지 일부를 참고했음
#### 개별 stage가 완료되면 다음 stage로 넘어감.
#### 시작 시 stage 1의 정보가 출력되고 커맨드를 입력 받음.

### (revision : 13)
#### 'update_map'의 일부 코드를 'just_move'로 분리
- 플레이어가 그냥 이동하는 경우

### (revision : 14)
#### 'funcs.py', 'step3.py', 'README.md' 수정

### (revision : 15)
#### 소코반 게임 기본적 기능 구현 
- 모든 공('o')이 구멍('O') 안으로 들어가면('0') 해당 스테이지 클리어
  - 클리어 시 클리어 메세지 출력
- 첫 시작 시 stage 1의 지도 정보와 'SOKOBAN' 프롬프트 표시
- 'r' 또는 'R' 입력 시 해당 스테이지 초기화
#### 스테이지 중 일부가 클리어가 불가능해 수정함

### (revision : 16)
#### 시작 시 이미 공이 구멍에 들어가 있는 경우에 대응하기 위해 수정

### (revision : 17)
#### 'q' 또는 'Q'로 게임 종료
#### 올바르지 않은 명령어 입력 시 오류 문구 출력. 다시 입력할 수 있음.

### (revision : 18)
#### 턴수를 출력할 수 있게 함.
- 딕셔너리를 사용해서 턴수를 출력하고 STEP4 'undo' 명령에도 대응할 수 있게 함.
  - 매 스테이지마다 턴수 초기화.
  - 'reset' 명령 시 턴수 초기화.
  - 다만 이동이 불가할 때도 턴수가 증가하는 문제가 있음.(개선 요망)

### (revision : 19)
#### 이동이 불가할 때는 턴수가 증가하지 않도록 함.

### (revision : 20)
#### 실행 결과 이미지 파일(3개) 추가

### (revision : 21)
#### 이미지 파일(1개) 추가
#### 올바르지 않은 명령어 입력 시 무한 반복되는 문제 해결

#### 실행 결과
- step3_result1.png
- step3_result2.png
- step3_result3.png
- step4_result4.png


## 4단계
- **sokoban.py**
### (revision : 22)
#### (개인적으로 구현해 본 추가 기능)
- 'c'를 입력하면 절대로 이동이 불가능한 공이 있는지, 있다면 그 좌표는 어딘지 출력해주는 기능
  - ~~공을 기준으로 맞닿은 두 방향의 조합('up-left', 'left-down', 'down-right', 'right-up') 중 어느 한 조합이라도 막혀있다면 해당 공은 절대 움직일 수 없다.~~ -> *revision 23에서 수정*
    - ~~즉 서로 마주보는 두 방향 중 최소 하나가 뚫려 있지 않다면 해당 공은 절대 움직일 수 없다.~~ 
      - 지도 데이터에서 'o'인 지점을 찾고 모든 'o'에 대해 이동 가능 여부를 파악한다.
      - 파악 후 만약 하나라도 이동 불가능한 점이 존재한다면 그 점의 좌표를 표시한다.
      - 구멍에 들어가지 않은 공('o') 중 최소 하나가 이동이 불가능하다는 건 결국 해당 시점부터 아무리 턴을 써도 스테이지 클리어가 불가능하다는 뜻이므로 종료 혹은 리셋을 권한다. 

### (revision : 23)
#### step3.py를 sokoban.py로 이름 변경.
#### funcs.py 에 모든 함수가 모여 있는 것은 가독성을 해친다고 판단하여 기능별로 파일을 나누고 연관된 파일들끼리 import 수정.
- step1.py, step2.py는 funcs.py의 함수들을 끌어다 쓰도록 그대로 유지.
- **[funcs.py 분할 정보]**
- check.py
  - `is_all_in`
  - `check_sides`
  - `check_possible`
- main.py
  - `exec_commands`
  - `input_command`
  - `finish_game`
  - `start_game`
- move.py
  - `locate_player`
  - `move_up`
  - `move_left`
  - `move_down`
  - `move_right`
  - `push_up`
  - `push_left`
  - `push_down`
  - `push_right`
  - `take_out_up`
  - `take_out_left`
  - `take_out_down`
  - `take_out_right`
  - `treat_hole`
  - `update_map`
- processing.py
  - `divide_stages`
  - `save`
  - `open_file`
  - `set_stages`
  - `count_ball`
  - `count_hole`
  - `save_hole_loc`
- show.py
  - `show_basic_info`
  - `show_additional_info`
  - `get_stage_info`
  - `show_fail`
  - `show_success`
  - `show_stage_info`
#### 'c' 커맨드
- revision 21에서 논리적 오류가 있는 부분을 수정
  - 절대로 공이 이동할 수 없는 경우는 맞닿은 두 면이 벽일 때.
    - 그 외의 경우에 대해 이동 가능 여부를 판단하려면 보다 복잡한 로직이 필요할 것 같아 생략.
    - 실행 결과 -> step4_result1.pngㅢ 파일

### (revision : 24)
#### slot.py에 'S(Save)', 'L(Load)' 관련한 함수 저장
- 1~5 숫자 입력 시 해당 슬롯 현 저장값 출력
  - 해당 슬롯은 stage1의 초기 지도값, {} (log 저장용), 0 (스테이지 저장용) 으로 초기화되어 있음.
  - 'S'를 눌러 현재 지도 정보를 해당 슬롯에 저장할 수 있음. (진행 중이던 log, 스테이지 번호도 함께 저장됨)
  - 'L'를 눌러 해당 슬롯 정보를 현재 지도에 불러와서 이어 플레이할 수 있음.

#### 기타 코드 수정.

### (revision : 25)
#### README.md 수정
