def trouble_sort(N):
    done = False
    while not done:
        done = True
        for i in range(0, len(N) - 2):
            if N[i] > N[i+2]:
                done = False
                N[i] += N[i+2]
                N[i+2] = N[i] - N[i+2]
                N[i] -= N[i+2]

t = int(input())
x = 1
while t:
    t-=1
    n = int(input())
    N = map(int, input().split())
    N = list(N)
    trouble_sort(N)
    prob = False
    ind = 0

    for i in range(0, len(N) - 1):
        if N[i] > N[i+1]: 
            ind = i
            prob = True
            break

    if prob:
        print("Case #%d: %d" % (x, ind))
    else:
        print("Case #%d: OK" % x)

    x+=1
