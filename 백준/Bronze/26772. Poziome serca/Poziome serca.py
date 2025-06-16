n = int(input())

heart_lines = [
    " @@@   @@@ ",
    "@   @ @   @",
    "@    @    @",
    "@         @",
    " @       @ ",
    "  @     @  ",
    "   @   @   ",
    "    @ @    ",
    "     @     "
]

for line in heart_lines:
    output_line = []
    for i in range(n):
        output_line.append(line)
    print(" ".join(output_line))
