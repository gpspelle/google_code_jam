import sys

def answer(number):

    print(number)
    sys.stdout.flush()
    judge = input()

    if judge == 'CORRECT':
        return 0
    elif judge == 'TOO_SMALL':
        return -1 
    elif judge == 'TOO_BIG':
        return 1

t = int(input())

while t > 0:
    A, B = map(int, input().split())
    N = int(input())
   
    while N > 0:  
        medium = (A + B) // 2 
        judge = answer(medium)

        #print(judge, file=sys.stderr)
        
        if judge == 0:
            break
        elif judge == -1:
            A = medium
            A +=1
        elif judge == 1:
            B = medium

        N-=1


    t-=1
