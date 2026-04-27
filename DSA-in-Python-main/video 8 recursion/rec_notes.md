# Recursion ::: 28 march 2026
# function calling itself is called recursion.

EX:-
def abc():
    -------code--
        abc()

use for when particular code repeat.

for loop , while loop ==> This is called iterative code
* This iterative code can convert in recursion.

how to find recursion is used => If code is repeated

# solve problem in small small parts
# like 1 , 1 + 2 , 1 - 3 , 1 - 4......

## 12:00 minute bookmark

=> used for => jaha same kaam repeat ho raha h,
badi problem ko chota karke solve kar sakte h 

### How to write code of recursion
1 => Pata hona chahiye problem kaha se start ho rahi h , also called base case
2 => logic , joh kaam karna h uske liye kya code lagega ,
3 => treminating , end pata hona chahiye
f1 -> f2 - f3..... fn

====>1) very important here is __Base case__
=> base case is joh problem li uska sabse chota case jiska answer pehle se pata  , issse hi terminating condition banegi
2) 2nd main thing is logic. 

ex:- factorial
->base case is 1.
->logic case is :- 
fact(5) = 5 * fact(4) // fact(n) = n * fact(n-1)


## At the time of written code
-> First important thing is to write base case after define the funciton.Because without it can trap in infinite loop. , This is terminating condition.
ex:-
    if n == 0 or n == 1:
        return 1
    # this is the termnating condition or base case

-> recursion / logic
ex:- return n * factorial(n - 1)

### My homework is to write fibonacci series using recursion.
n = 7
0 1 1 2 3 5 8.....( then 7 starting numbers print.)
need base case







