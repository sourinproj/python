import math

def isperfectsquare(x):
    s = int(math.sqrt(x))
    return s*s == x
    
def isFibonacci(n):
    
    return isperfectsquare(5*n*n + 4) or isperfectsquare(5*n*n - 4)
    
llimit=int(input("enter the llimit :"))
ulimit=int(input("enter the ulimit :"))
for i in range(1,21):
    if (isFibonacci(i) == False):
        print(i,"is not a Fibonacci Number")