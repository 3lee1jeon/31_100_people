import random

#중복 없느 1~100 숫자가 들어간 랜덤 박스 리스트 생성
def random_boxes():
    # 1부터 100까지의 숫자로 이루어진 리스트 생성
    numbers =list(range(1,101))

    # numbers 리스트에서 중복 없이 100개의 숫자를 랜덤배치하는 새로운 리스트 생성
    random_numbers = random.sample(numbers, 100)

    return random_numbers



def open_box(random_numbers):
    prisoners = list(range(1, 101))  # 1부터 100까지의 죄수 번호 리스트
    attempts = [0] * 100  # 각 죄수의 시행 횟수를 저장할 리스트 초기화
    found = [False] * 100  # 각 죄수가 자신의 번호를 찾았는지 여부를 저장할 리스트 초기화

    for prisoner in prisoners:
        box_number = prisoner  # 첫 번째 박스 번호는 자신의 번호
        while not found[prisoner - 1]:  # 자신의 번호를 찾을 때까지 반복
            attempts[prisoner - 1] += 1  # 시행 횟수 증가
            if attempts[prisoner - 1] > 50:  # 시행 횟수가 50을 초과하면 중단
                break
            box_number = random_numbers[box_number - 1]  # 다음 박스 번호
            if box_number == prisoner:  # 박스 안의 쪽지 번호가 자신의 번호와 일치하면
                found[prisoner - 1] = True  # 자신의 번호를 찾았음을 표시

    return attempts

def result(attempts):
    success = True
    for attempt in attempts:
        if attempt > 50:
            success = False
            break
    return success

random_numbers = random_boxes()
attempts = open_box(random_numbers)
print(f"trial num: {attempts}")
print(f"all success befor 50 times?? {result(attempts)}")
