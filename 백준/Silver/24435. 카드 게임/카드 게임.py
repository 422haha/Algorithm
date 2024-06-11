import sys
from itertools import permutations


def get_largest_smaller_number(bob_cards, alice_cards):
    # Bob이 만들 수 있는 두 수
    bob_num1 = int("".join(bob_cards))
    bob_num2 = int("".join(bob_cards[::-1]))

    # Bob이 만들 수 있는 두 수 중 큰 수를 bob_max로 설정
    bob_min = min(bob_num1, bob_num2)

    n = len(alice_cards)
    alice_cards_sorted = sorted(alice_cards, reverse=True)  # 내림차순으로 정렬

    largest_smaller_number = ""

    # n 자리 수에서 1자리 수까지 하나씩 줄여가며 가능한 수를 확인
    for size in range(n, 0, -1):
        perm = permutations(alice_cards_sorted, size)
        for p in perm:
            alice_num = int("".join(p))
            if alice_num < bob_min:
                if largest_smaller_number == "" or alice_num > int(largest_smaller_number):
                    largest_smaller_number = "".join(p)
        if largest_smaller_number:
            break

    return largest_smaller_number


t = int(sys.stdin.readline().rstrip())
for tc in range(1, t+1):
    n = int(sys.stdin.readline().rstrip())
    bob_cards = list(sys.stdin.readline().rstrip())
    alice_cards = list(sys.stdin.readline().rstrip())
    result = get_largest_smaller_number(bob_cards, alice_cards)
    print(result)