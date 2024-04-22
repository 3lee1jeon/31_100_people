import random


# 중복 없느 1~100 숫자가 들어간 랜덤 박스 리스트 생성
def random_boxes():
    # 1부터 100까지의 숫자로 이루어진 리스트 생성
    numbers = list(range(1, 101))

    # numbers 리스트에서 중복 없이 100개의 숫자를 랜덤배치하는 새로운 리스트 생성
    random_numbers = random.sample(numbers, 100)

    return random_numbers


def random_prisoners():
    numbers = list(range(1, 101))

    random_prisoners = random.sample(numbers, 100)

    return random_prisoners


def random_choice(prisoners, random_box_numbers):

    for i in range(len(prisoners)):
        choice = list(range(1, 50 + 1))
        choice_list = random.sample(choice, 50)
        for j in range(len(choice_list)):

            # print(choice)
            # print(choice_list)

            if prisoners[0] != random_box_numbers[choice_list[j]]:
                return False

    return True


print(random_choice(random_prisoners(), random_boxes()))
