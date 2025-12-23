prices = {
    "Paper": 57.99,
    "Printer": 120.50,
    "Planners": 31.25,
    "Binders": 22.50,
    "Calendar": 10.95,
    "Notebooks": 11.20,
    "Ink": 66.95
}

res = 0.0
while True:
    item = input().strip()
    if item == "EOI":
        break
    if item in prices:
        res += prices[item]

print(f"${res:.2f}")