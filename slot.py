import show
import copy

def show_slot(slots, number):
    print(f"\nSlot {number+1}")
    show.show_basic_info(slots[number][0])
    print()
    print("'S(Save)' 혹은 'L(Load)'를 입력하세요 >", end=' ')


def save_slot(map_list, slots, number, log, i):
    slots[number] = copy.deepcopy((map_list, log, i))
    show.show_basic_info(map_list)
    return slots[number]


def load_slot(slots, number):
    show.show_basic_info(slots[number][0])

    return slots[number]