import sys

def matrix_side_complete(m, u, v):
    if m[u-1][v-1] == 1 and m[u][v-1] == 1 and m[u+1][v-1] == 1:
        return True

    return False

t = int(input())
while t:
    t-=1
    a = int(input())
    q = a // 3 + 1
    if q == 7:
        m = [[0]*11 for tu in range(5)]
    else:
        m = [[0]*74 for tu in range(5)]

    u = 3
    v = 3
    while True:
        if matrix_side_complete(m, u, v) == True:
            v+=1
            if v == q + 3:
                v -= 1
        print("%d %d" % (u, v))
        sys.stdout.flush()
        i, j = map(int, input().split())
        if i == j and i == 0:
            break
        m[i][j] = 1
    
