dct = {
    "CU": "see you",
    ":-)": "I’m happy",
    ":-(": "I’m unhappy",
    ";-)": "wink",
    ":-P": "stick out my tongue",
    "(~.~)": "sleepy",
    "TA": "totally awesome",
    "CCC": "Canadian Computing Competition",
    "CUZ": "because",
    "TY": "thank-you",
    "YW": "you’re welcome",
    "TTYL": "talk to you later"
}

while True:
    n = input()
    if n == "TTYL":
        print(dct[n])
        break
    if n in dct:
        print(dct[n])
    else:
        print(n)