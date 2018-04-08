def get_damage(p, i, j):
    strength = 1
    damage = 0
    for i in range(i, j):
        if p[i] == 'C':
            strength *= 2
        else:
            damage += strength
    return damage

t = int(input())
x = 1
while t:
    t-=1
    d, p = map(str, input().split())
    d = int(d)
    p = list(p)
    damage = get_damage(p, 0, len(p))
    op = 0
    possible = False 
    if damage > d:
        for i in range(0, len(p) - 1): 
            while i >= 0:
                if p[i] == 'C' and p[i+1] == 'S':
                    p[i] = 'S' 
                    p[i+1] = 'C'
                    op += 1
                    i-= 1
                else:
                    break
            if get_damage(p, 0, len(p)) <= d:
                possible = True
                break
    else:
        possible = True

    if possible:
        print("Case #%d: %d" % (x, op))
    else:
        print("Case #%d: IMPOSSIBLE" % x)
    x += 1
