t = int(input())
x = 1
while t:
    t-=1
    n = int(input())
    N = map(int, input().split())
    N = list(N)
    even = []
    odd = []
    for i in range(n):
        if i % 2 == 0:
            even.append(N[i])
        else:
            odd.append(N[i])

    N.sort()
    prob = True 
    ind = 0
    even.sort()
    odd.sort()
    print(odd)
    print(even)
    print(N)
    for i in range(n):
        if i % 2 == 0:
            if N[i] != even[i//2]:
                prob = False
                ind = i
                break
        else:
            if N[i] != odd[i//2]:
                prob = False
                ind = i
                break
    if not prob:
        print("Case #%d: %d" % (x, ind))
    else:
        print("Case #%d: OK" % x)

    x+=1
