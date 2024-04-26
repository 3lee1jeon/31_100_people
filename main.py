# 수정된것 바로 pull request 되는 확인해보자
import random

#중복 없느 1~100 숫자가 들어간 랜덤 박스 리스트 생성
def random_boxes():
    # 1부터 100까지의 숫자로 이루어진 리스트 생성
    numbers =list(range(1,101))

    # numbers 리스트에서 중복 없이 100개의 숫자를 랜덤배치하는 새로운 리스트 생성
    random_numbers = random.sample(numbers, 100)

    return random_numbers


print(random_boxes())

# 전략 없는 경우
def no_strategy(random_boxes):
    pass

# 전략 있는 경우
def strategy(random_boxes):
    pass


# 전략 있음 임의 함수 명 : staraegy()
def calculate_prob(n):
    success_no_strategy = 0
    success_strategy = 0
    
    for _ in range(n):
        random_boxes = random_boxes()

        if no_strategy(random_boxes):
            success_no_strategy += 1 
        if strategy(random_boxes):
            success_strategy += 1

    no_strategy_prob = success_no_strategy / n
    strategy_prob = success_strategy / n

    return {"no_strategy": no_strategy_prob, "strategy": strategy_prob}
