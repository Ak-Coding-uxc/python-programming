# Recursion ::: 28 march 2026
# function calling itself is called recursion.

### FINBONACCI CODE VISULIZE LINK:- https://staying.fun/en/features/algorithm-visualize?code=8c79b484ec1a2c8b9dc783d26387a92cb032b98bc0247f9b1068cc0d1bbc11f2

# def rec(k):
#     if(k > 10):
#         return 0
#     return k + rec(k + 1)

# # kya galti h isme => koi bhi return nhi kar raha tha base case mein
# s = rec(1)
# print(s)

""" k = 1
sum = 0
while( k < 11):
    sum = sum + k
    print(f'k = {k} and sum = {sum}')
    k = k + 1

print(sum) """

""" 
# factrorial ex;- 5! or |_5 = 5 * 4 * 3 * 2 * 1
num = int(input("Enter number:- "))
fact = 1
for i in range(1,num + 1):
    fact = fact * i
    print(f"fact value => {fact} after i => {i}")

print(fact) """
""" 
for i in range(6): # i start from 0
    print(i) """

""" def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

fact = factorial(5)
print(fact) """
# tc = O(n) , n  , space complexity => o(n)


## Fibonacci using recursion.
# not printing all values just printing what is the 7th element in fibonacci series
def fibo(n): # n = 7
    if(n == 1 or n == 2):
        return 1
    return fibo(n - 1) + fibo(n-2)
    print(n)
    
fib = fibo(7)
print(fib)
