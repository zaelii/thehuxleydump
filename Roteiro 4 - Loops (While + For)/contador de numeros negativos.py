num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

neg_count = 0

for num in range(1,4+1):
    if num1 <= 0:
        num1 - num1 + 1
        neg_count += 1
    if num2 <= 0:
        num2 - num2 + 1
        neg_count += 1
    if num3 <= 0:
        num3 - num3 + 1
        neg_count += 1
    if num4 <= 0:
        num4 - num4 + 1
        neg_count += 1
    if num5 <= 0:
        num5 - num5 + 1
        neg_count += 1
    num += 1

print(neg_count)
