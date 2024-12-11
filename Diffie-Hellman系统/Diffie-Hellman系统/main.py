import random


#平方—乘法，最后返回结果
def MRF(b,n,m):
    
        a=1
        x=b;y=n;z=m
        binstr = bin(n)[2:][::-1]	#通过切片去掉开头的0b，截取后面，然后反转
        for item in binstr:
                if item == '1':
                        a = (a*b)%m
                        b = (b**2)%m
                elif item == '0':
                        b = (b**2)%m
        return a
    
#素性检验
def MillerRabin(n):
                            #利用Miller-Rabin算法检验生成的奇数是否为素数
    m=n-1
    k=0
    a=random.randint(2,n)   #闭区间
    b = MRF(a,m,n)
    if(b==1):
        return 1
    while(m%2==0):
        m=m//2
        k=k+1
    b = MRF(a,m,n)         #b=a**m%n
    if(b==1):
        return 1  
    for i in range(k):
        if(b==n-1):
            return 1
        else:
            b=b*b%n
    return 0

#生成大素数，20次MillerRabin算法缩小出错的概率
def BigPrime():
    Min = 10**11;Max = 10**15;p = 0
    while(1):
        p = random.randrange(Min,Max,1)
        for i in range(20):
            if MillerRabin(p)==0:
                break
            elif i==19:
                return p
            
def gcd(a,b):  
        if a%b == 0:
                return b
        else :
                return gcd(b,a%b)
                
#快速幂取模
def mod_fast(x, n, Mod):
    res = 1
    x %= Mod
    while n != 0:
        if n & 1:                      #取n的2进制的最低位
            res = (res * x) % Mod
        n >>= 1                        #相当于n//2 
        x = (x * x) % Mod
    return res


