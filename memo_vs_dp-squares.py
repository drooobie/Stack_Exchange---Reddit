from time import time
from Decorators import memo

@memo
def T(n):
    if n==0:  return 0
    return min( T(n-i*i) for i in xrange(int(n**.5),0,-1) ) + 1


def DP(n):
    T = [0]*(n+1)
    for i in xrange(1, n+1):
        T[i] = min ( T[i-x*x] for x in xrange(1,int(i**.5)+1) ) + 1
    return T


print '       n     DP   Memo'
for n in [100, 1000, 10000, 100000, 1000000]:
    toc,_,tic = time(), DP(n), time()
    toc2,_,tic2 = time(), T(n), time()
    T.m.clear()
    print str(n).rjust(8), str(tic-toc)[:6], str(tic2-toc2)[:6]