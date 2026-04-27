arcane = [
    (200, 210, 220),    # 여로
    (210, 220, 225),    # 츄츄
    (220, 225, 230),    # 레헬른
    (225, 230, 235),    # 아르카나
    (230, 235, 245),    # 모라스
    (235, 245, 250),    # 에스페라
]

grandis = [
    (260, 265, 270),    # 세르니움
    (265, 270, 275),    # 아르크스
    (270, 275, 280),    # 오디움
    (275, 280, 285),    # 도원경
    (280, 285, 290),    # 아르테리아
    (285, 290, 295),    # 카르시온
    (290, 295, 300),    # 탈라하트
]


def calc_count(level, region):
    result = []
    for quest, dec1, dec2 in region:
        if level < quest:
            result.append(0)
        elif level < dec1:
            result.append(500)
        elif level < dec2:
            result.append(300)
        else:
            result.append(100)
    return result


l = int(input())

cnt_arcane = calc_count(l, arcane)
cnt_grandis = calc_count(l, grandis)

print(*cnt_arcane)
print(*cnt_grandis)
