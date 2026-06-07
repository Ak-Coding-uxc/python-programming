* tree and graph is used when we have to form hieraricaly dataset.

# array, linked list, stack, queue => are linear data structure.
- means data or elemenets  store one by one or in sequece.
- traversing in linear direction

# Tree and grapah => are non - linear data structure.
- Not have linear traversing. means not in sequence.
- have multiple root to travel.

In data sturcture top element is called root and other are called leaf
because tree forming is start from root.( just rotate the tree bro , you find that root in upper.)
- same level nodes are siblings.
- upper node is parent node and lower node is called child node. 
- tree feature is we can go from top to bottom, but we cannot go from bottom to top.
means parent to child is allow but child to parent is not allowed , we have to use stack to recursion for child to parent.
-- very important is recursion and traversing here for backtrack. 
- tree can have any child :- 0 , 1 ... any.

* Types of node in tree
Top node is called root node where tree is start building.
Middle nodes are called Intermediate nodes.
Last nodes are called leaf nodes.

* use case
- where maintain hierarchy
ex:- family tree, ceo - managers -- employs

# Types of tree
1) Binary tree:- Maximum child are 2; 0 , 1 and 2 child are allowed.
2) Binary search tree(very important):- max 2 child.0,1,2 child only. left subtree small than root, right subtree values are bigger than root value.( dubara dekhna padega.)
3) Strict Binary Tree:- Max 2 child, strict -> only 0 or 2 child are allowed 
, 1 child is not allowed, exactly 0 or 2 child of node are allowed. Not have any restrictions like BST. This also called FULL BT.
4) Complete BT :- max 2 child. But not strictly can be 0 1 or 2 child , 
if enter new node go in right side if space is availabe only and previous level must be full if want to go in next level. First start with left side to insert value.
5) skew BT:- Ya toh left mein element aayege(left skew tree) ya right side only(right skew tree) . only 1 node in each level is allowed.
6) Degenerated tree:- zig-zag . only 1 node in each level is allowed.
7) extended BT:- tree ko strict ya complete bt tree banana dummy node jodh kar.
etc types of tree also
M-WAY TREE HAVE MULITPLE CHILDERS
# Binany Tree Representations:-
1) Array
2) Linked list


Rule for array:-
1. store first level 0 element then level 1 elements the n level 2 then so on
2. First store left element then right elements. (l to r)

problem is kaun kiska child ye pata nhi chal pata
use mathemathics here :- 
{(index)*2 + 1} => Left child index
{(index)*2 + 2} => Right child index
idher index uska aayega jiska child dekhna chahte ho tum.
q) if have child index then how you gonna find out parent node index.
- left child = (index)*2 + 1 
  parent = (index - 1) / 2
- right child = (index) *2 + 2
  parent
for ex:-
left child index => 5
parent of left child (5 - 1)/ 2 =?4 / 2 => 2 

right child index => 6
parent of right child => (6 - 2) / 2 => 4 / 2 => 2

another prob :- if ek parent ke pass 2 child h orr ek ke paas nhi h
toh fir dummy nodes banani padegi orr isko complete binary treee banana padega. unke index ko empty chood sakte h.


# llnked list representations:-

:- First study doubly linked list in detail for tree.

-> previous poiter , data , next pointer
-> same this code is used here
-> just change the name :- left pointer , data , right pointer
left pointer point left tree
right pointer point right node 
if not have any child then None hi rehne dege
use recursion here.







