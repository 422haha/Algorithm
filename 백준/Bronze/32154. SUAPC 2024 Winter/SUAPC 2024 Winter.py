arr = [
    ["A", "B", "C", "D", "E", "F", "G", "H", "J", "L", "M"],
    ["A", "C", "E", "F", "G", "H", "I", "L", "M"],
    ["A", "C", "E", "F", "G", "H", "I", "L", "M"],
    ["A", "B", "C", "E", "F", "G", "H", "L", "M"],
    ["A", "C", "E", "F", "G", "H", "L", "M"],
    ["A", "C", "E", "F", "G", "H", "L", "M"],
    ["A", "C", "E", "F", "G", "H", "L", "M"],
    ["A", "C", "E", "F", "G", "H", "L", "M"],
    ["A", "C", "E", "F", "G", "H", "L", "M"],
    ["A", "B", "C", "F", "G", "H", "L", "M"],
]

n = int(input())
res = arr[n - 1]
print(len(res))
print(" ".join(res))