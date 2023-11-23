import math 
def possible(board,n):
    k= n%8
    while k<64:
        if k!=n and board[k] == 1:
            return False
        k+=8
    k=8*(n//8)
    for i in range(0,8):
        if k!=n and board[k] == 1:
            return False
 #przekatna 1
    k=n
    while k>=0:
        if k!=n and board[k] == 1:
            return False
        k-=9

    k=n
    while k<64:
        if k!=n and board[k] == 1:
            return False
        k+=9
       k=n
#przekatns 2
    while k>=0:
        if k!=n and board[k] == 1:
            return False
        k-=7
    k=n
    while k<64:
        if k!=n and board[k] == 1:
            return False
        k+=7
    return True
def rec(board,n,res,sq):
   # print(board,n,res,sq)
    if n==8:
        return 1
    if sq==64:
        return 0
    for i in range(sq, 64):
        if n==1:
            print(i)
        if possible(board,i):
            board[i]=1
            res+=rec(board,n+1,res,i+1)
            board[i]=0
    
    return res
    
board = [0]*64
print(math.log2(rec(board,0,0,0)))
