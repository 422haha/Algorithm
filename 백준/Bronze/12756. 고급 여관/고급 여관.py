a_atk, a_hp = map(int, input().split())
b_atk, b_hp = map(int, input().split())

a_turns = (b_hp+a_atk-1)//a_atk
b_turns = (a_hp+b_atk-1)//b_atk

if a_turns < b_turns:
    print("PLAYER A")
elif a_turns > b_turns:
    print("PLAYER B")
else:
    print("DRAW")