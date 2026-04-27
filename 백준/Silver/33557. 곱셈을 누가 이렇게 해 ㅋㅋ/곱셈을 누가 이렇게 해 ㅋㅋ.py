for _ in range(int(input())):
    a_str, b_str = input().split()
    A_int = int(a_str)
    B_int = int(b_str)
    len_a = len(a_str)
    len_b = len(b_str)
    n = max(len_a, len_b)
    if len_a < n:
        a_str = " "*(n-len_a)+a_str
    if len_b < n:
        b_str = " "*(n-len_b)+b_str

    wrong = ""
    for i in range(n):
        a_digit = a_str[i] if a_str[i] != " " else None
        b_digit = b_str[i] if b_str[i] != " " else None
        if a_digit is not None and b_digit is not None:
            wrong += str(int(a_digit)*int(b_digit))
        elif a_digit is not None:
            wrong += a_digit
        elif b_digit is not None:
            wrong += b_digit

    normal = A_int * B_int

    if int(wrong) == normal:
        print("1")
    else:
        print("0")
