"""
1. Make a list of all numbers from 2 to n.
 [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ……., n]
2. Starting from 2, delete all of its multiples in the list, except itself.
 [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,……., n]
3. Repeat the step 2 till square root of n.
    For 3 –  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20……., n]
    For 5 – [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20……., n]
    Till sqrt(n)
The remaining list only contains prime numbers.
"""
import math
def count_primes(num):
    lis = []
    for i in range(2,num+1):
        lis.append(i)
    #print(lis)
    i=2
    while i<= int(math.sqrt(num)):
        if i in lis:
            for j in range(2*i,num+1,i):
                if j in lis :
                    lis.remove(j)
        i+=1
    return lis

lis=count_primes(100)
print(lis)
