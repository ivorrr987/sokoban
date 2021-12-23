import processing
import main

origin = processing.open_file("maps.txt") # maps.txt에 저장된 정보를 가져옴.
maps_str = processing.divide_stages(origin) # '====='를 기준으로 스테이지 별로 분할.

stages = processing.set_stages(maps_str) # 각 스테이지 지도 정보를 2차원 배열 형태로 저장

main.start_game(stages)
