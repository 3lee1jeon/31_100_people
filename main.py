import random

#중복 없느 1~100 숫자가 들어간 랜덤 박스 리스트 생성
def random_boxes():
    # 1부터 100까지의 숫자로 이루어진 리스트 생성
    numbers =list(range(1,101))

    # numbers 리스트에서 중복 없이 100개의 숫자를 랜덤배치하는 새로운 리스트 생성
    random_numbers = random.sample(numbers, 100)

    return random_numbers


print(random_boxes())
