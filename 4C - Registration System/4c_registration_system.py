v = {}
s_n = set()
n = int(input())

for _ in range(n):
    r = input()
    if r in v:
        print(r + str(v[r]))
        v[r] += 1
    else:
        print("OK")
        v[r] = 1
    
    