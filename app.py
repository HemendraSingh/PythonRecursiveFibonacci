def RecursiveFibonacci(n,fibLst = [],seed1=0,seed2=1,cntr=2):
    if cntr == 2: 
        if n > 2:
            fibLst.append(0)
            fibLst.append(1)
        elif n == 2:
            fibLst.append(0)
            fibLst.append(1)
            return
        elif n == 1:
            fibLst.append(0)
            return
        else:
            return
    
    nextnum = seed1 + seed2
    fibLst.append(nextnum)
    seed1 = seed2
    seed2 = nextnum
    cntr= cntr + 1
    
    if n != cntr:
        RecursiveFibonacci(n,fibLst,seed1,seed2,cntr)

    return fibLst

if __name__ == "__main__":
    n = int(input())
    fibLstRecur = RecursiveFibonacci(n)
    print(fibLstRecur)
