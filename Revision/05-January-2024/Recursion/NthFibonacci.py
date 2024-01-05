def nthFibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nthFibonacci(n-1) + nthFibonacci(n-2)

print(nthFibonacci(5))

def nthFibonacci(n,memoization={1:0,2:1}):
    if n in memoization:
        return memoization[n]
    else:
        memoization[n] = nthFibonacci(n-1,memoization) + nthFibonacci(n-2,memoization)
        return memoization[n]

print(nthFibonacci(5))