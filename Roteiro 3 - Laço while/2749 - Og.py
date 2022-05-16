while True:
    l, r = map(int, input().split())
    
    if l <= 5 and r <= 5 and l > 0 and r > 0:
        count = l + r
        print(count)
    if l == 0 and r == 0:
        break
