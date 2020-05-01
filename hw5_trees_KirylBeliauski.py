#****************
#* HW 5: problems on recursion + the Tree class
# It's the last lab + extras.
# Kiryl Beliauski
#****************

"""
Problem 0: 5 points
Write a recursive function that given a positive n, 
returns the sum of the first n positive numbers

recursive_sum(n-1) = 1 + 2 + ... + (n-1)
"""

def recursive_sum(n): #1 + 2 + 3 +....+ (n-1) + n
    if n == 0:
        return 0
    else:
        n += recursive_sum(n-1)
    return n

def aux_recursive_sum(counter,n):
    if counter == n:
        return counter
    else:
        sum = aux_recursive_sum(counter+1,n) + counter
    return sum



def recursive_sum2(n):
    return aux_recursive_sum(0,n)

#TESTS
assert recursive_sum(1) == 1
assert recursive_sum(2) == 1+2
assert recursive_sum(10) == (10*(10+1))/2.
assert recursive_sum2(1) == 1
assert recursive_sum2(2) == 1+2
assert recursive_sum2(10) == (10*(10+1))/2.

"""
Problem 1: 5 points
Implement the following recursive algorithm to compute the number of digits of a positive integer:
    # 1. If n < 10 return 1
    # 2. Otherwise, return 1 + the number of digits in n//10
DO NOT convert n to a string and then compute its length!
i.e. return(len(str(n))  VERBOTEN
"""
def digits(n):
    """
    n:int
    return the no. of digits in _n_
    """
    if n < 10:
        return 1
    else:
        return 1 + digits(n//10)

assert digits(8) == 1
assert digits(12345) == 5
assert digits(88888) == 5
assert digits(88) == 2


"""
Write a recursive function to compute the maximum element in a list
done here in case it is useful for the rest of the HW
"""
def max_recur(lst):  #lst[1:]
    if lst == []:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        assert(len(lst)) > 1
        lm = max_recur(lst[1:])
        if lst[0] > lm:
           return lst[0]
        else:
           return lm

#[1,2,4,5,6,7,10]  ---> 1,  max([2,4,5,6,7,10]) ==> 1,10 -->10
#prob(n) -->prob(n-1)-->prob(n-2)-->....prob(0)

assert max_recur([1,2,4,5,6,7,10]) == 10
assert max_recur([10,6,2,1]) == 10
assert max_recur([10,23,8,6,3,15,2,1]) == 23

"""
PROBLEM 2: 10 POINTS
Write a recursive function that return locations
of the first occurrence of item in lst. If the item isn't in lst, return -1.
"""
"""
def my_in(item,lst):
    if lst == []:
        return False
    ...
"""
def find(lst,item):
    if lst == []:
        return -1
    elif lst[0] == item:
        return 0
    else:
        return 1 + find(lst[1:], item)


def my_in(item,lst):
    """
    item,lst
    return:bool = True iff item is in the list
    """
    if lst == []:
        return False
    else:
        return lst[0] == item or my_in(lst[1:])

def find_recur(lst, item):
    if item not in lst:
        return -1
    else:
        return find(lst,item)


assert find_recur([1,2,4,5,6,7,10],1) == 0
assert find_recur([10,6,2,1],1) == 3
assert find_recur([10,23,8,6,3,15,2,1],7) == -1


"""
10 POINTS
Write a recursive function to reverse a list
"""
def reverse(lst):  #hint look at ordered
    if not lst:
        return lst
    else:
        return reverse(lst[1:]) + lst[:1]




assert reverse([1,2,3,4,5,6]) == [6,5,4,3,2,1]

"""
10
Write a recursive function that returns True iff a list is
alternating. If 0 is in the list it is not alternating. 
"""
def is_alternating(lst):
    if lst[0] == 0:
        return False
    elif len(lst) == 1:
        return lst[0]
    else:
        if lst[0] == -1*(is_alternating(lst[1:])):
            return lst[0]
        else:
            return False


assert is_alternating([-1,1,-1,1,-1])
assert is_alternating([1,-1,1,-1])
assert not is_alternating([-1,-1,-1,1,-1])
assert not is_alternating([-1,-1,-1,0,-1])

"""
30 POINTS
Write a recursive function that returns a list of all binary strings of length  n
"""
def add0(lst):
    """
    lst: a list of strings
    return: a list of every string in lst
    with a '0' tacked on to the end
    """
    if not lst:
        return []
    else:
        return [lst[0] + '0'] + add0(lst[1:])

def add1(lst):
    if not lst:
        return []
    else:
        return [lst[0] + '1'] + add1(lst[1:])


#['000','010','100','110']+['001','0101',etc.]
def binary(n):  #binary(2) ==> ['00','01','10','11']
    if n == 0:
        return ['']
    else:
        return add0(binary(n-1)) + add1(binary(n-1))

print(binary(1))
assert len(binary(1))==2**1
assert len(binary(2))==2**2
assert len(binary(3))==2**3

"""
Use the above function to write a function that returns a list of all binary strings of length <= n
"""
def binary_upto(n):
    if n == 0:
        return ['']
    else:
        return binary_upto(n-1) + binary(n)

    """
    lst = []
    for i in range(n):
        for j in (binary(i)):
            lst.append(j)
    return lst
    """

print(binary_upto(1))
print(binary_upto(2)) #['','0','1','00','01','10','11']
print(binary_upto(3))
"""
30 POINTS
#5 TREE PROBLEM
"""

""" Remember trees? Good! Copy the class definition (with the
constructor) from lecture and write a recursive function that returns
the maximum value of all the elements (integer labels) in a tree. You
can change the type of labels to ints, OR you can keep them as strings
and then remember to convert them to ints.  """

#class Tree(object):  #paste this in
class Tree(object):


    def __init__(self, label, left=None,right=None):
        assert type(left) == Tree or type(left) == type(None)
        assert type(right) == Tree or type(right) == type(None)
        assert type(label) == int

        #self.parent= parent
        self.left = left
        self.right = right
        self.label = label

    def isleaf(self):
        return type(self.left) == type(None) and type(self.right) == type(None)

    def isroot(self):
        return self.parent == type(None)

    def get_label(self):
        return self.label

    def get_children(self):
        ch = []
        if type(self.left) != type(None):
            ch.append(self.left)
        if type(self.right) != type(None):
            ch.append(self.right)

    def tree_max(self):
        """
        returns largest label in tree t
        """
        if self.isleaf():
            return self.get_label()
        else:
            tm = self.get_label()
            if self.left != None:
                tm = max(tm, self.left.tree_max())
            if self.right != None:
                tm = max(tm, self.right.tree_max())
            return tm

    def labs(self):
        """
        return list of labels
        """
        if self is None:
            return []
        elif self.isleaf():
            return [self.label]
        else:
            return [self.label] + self.left.labs() + self.right.labs()

    def less_than(self, val):
        """
        t:Tree with int labels
        return:list of labels < val
        """
        if self is None:
            return []
        elif self.isleaf() and self.get_label() < val:
            return [self.get_label()]
        else:
            num = self.get_label()
            if num < val:
                return [num] + self.left.less_than(val) + self.right.less_than(val)
            else:
                return self.left.less_than(val) + self.right.less_than(val)

    def tree_height(self):
        if self.isleaf():
            return 1
        else:
            th = 0
            if self.left != None:
                th = self.left.tree_height()
            if t.right != None:
                th = max(th, self.right.tree_height())
            return th + 1

    def left_height(self):
        left = 1
        if self == None:
            return 0
        else:
            left = self.left.tree_height()
        return left + 1

    def right_height(self):
        right = 1
        if self == None:
            return 0
        else:
            right = self.right.tree_height()
        return right + 1

    def is_balanced(self):
        left = self.left_height()
        right = self.right_height()

        if left == right or left + 1 == right or left - 1 == right:
            return True
        else:
            return False

    def width(self, num):
        if self == None:
            return 0
        if num == 1:
            return 1
        else:
            return self.left.width(num-1) + self.left.width(num-1)

print("TEST Inclass Method")
print("width")
t2 = Tree(5,Tree(2,None,None),Tree(6,Tree(3,None,None),Tree(1,None,Tree(10,None,None))))
#print(t2.width(2))
assert t2.width(2) == 2

print("Max")
t2 =Tree(5,Tree(2,None,None),Tree(6,Tree(3,None,None),Tree(1,None,Tree(10,None,None))))
print(t2.tree_max())
assert t2.tree_max() == 10

t = Tree(5,Tree(2,None,None),Tree(6,Tree(3,None,None),Tree(1,None,Tree(10,None,None))))
print('height')
print(t.tree_height())

print("balance")
print(t.is_balanced())



def tree_max(t):
    """
    returns largest label in tree t
    """
    if t.isleaf():
        return t.get_label()
    else:
        tm = t.get_label()
        if t.left != None:
            tm = max(tm, tree_max(t.left))
        if t.right != None:
            tm = max(tm, tree_max(t.right))
        return tm



t1 = Tree(5,Tree(2,None,None),Tree(6,None,Tree(1,None,None)))
t2 = Tree(4,Tree(7,None,None),Tree(5,Tree(1,None,None),Tree(1,None,None)))
assert tree_max(t1) == 6
assert tree_max(t2) == 7

#list of labels[5,2,6,1]

def labs(t):
    """
    return list of labels
    """
    if t is None:
        return []
    elif t.isleaf():
        return [t.label]
    else:
        return [t.label] + labs(t.left) + labs(t.right)

print(labs(t1))

"""
Write a function that returns a list with all the elements (labels) less than a given value in a tree
"""
def less_than(t, val):
    """
    t:Tree with int labels
    return:list of labels < val
    """
    if t is None:
        return []
    elif t.isleaf() and t.get_label() < val:
        return [t.get_label()]
    else:
        num = t.get_label()
        if num < val:
            return [num] + less_than(t.left, val) + less_than(t.right, val)
        else:
            return less_than(t.left, val) + less_than(t.right, val)


print(less_than(t1, 4))
assert len(less_than(t1, 4)) == 2
"""
The height of a tree is the maximum number of nodes on a path from the root to a leaf node. Write a function that returns the height of a tree
"""

def tree_height(t):
    if t.isleaf():
        return 1
    else:
        th = 0
        if t.left != None:
            th = tree_height(t.left)
        if t.right != None:
            th = max(th, tree_height(t.right))
        return th + 1

assert tree_height(t1) == 3
"""
A binary tree is said to be "balanced" if both
of its subtrees are balanced and the
height of its left subtree differs from the height of its right
subtree by at most 1.
Write a function that returns True iff  a given
binary tree is balanced.
"""

def left_height(t):
    left = 1
    if t == None:
        return 0
    else:
        left = tree_height(t.left)
    return left + 1



def right_height(t):
    right = 1
    if t == None:
        return 0
    else:
        right = tree_height(t.right)
    return right + 1



def is_balanced(t):
    left = left_height(t)
    right = right_height(t)

    if left == right or left+1 == right or left-1 == right:
        return True
    else:
        return False

"""
6 TREES cont.

Now turn all preceding Tree functions into
methods in the Tree class

"""

#inside the Tree class:
#class Tree(object):

#    def is_balanced(self):



#TESTS
t = Tree(5,Tree(2,None,None),Tree(6,None,Tree(1,None,None)))
assert is_balanced(t)

t = Tree(5,Tree(2,None,None),Tree(6,Tree(3,None,None),Tree(1,None,None)))
assert is_balanced(t)

t = Tree(5,Tree(2,None,None),Tree(6,Tree(3,None,None),Tree(1,None,Tree(10,None,None))))
assert not is_balanced(t)

"""
20
6.5 Define a width method for trees
returns an int
"""
#did it
"""
50
7 PARSING (do this last. Just get started. It will be discussed)
"""
"""
Let arithmetic expressions be defined by

<aexp> := <var> | <num> | <aexp> <op> <aexp>| (<aexp>)| - <aexp>
<op> := + | * | - | / 

examples:  x1, 432, x1 + 432,(432), ((x + balance)/(y - 12))

write the code for a function RPN that
converts arithmetic expressions into
"reverse Polish notation"

((22 + x5)*(x - bal))   ==========>  *(+(22,x5),-(x,bal))
"""

def rpn_heper(aexp):
    result = ''
    aexp = aexp.strip('(')
    aexp = aexp.strip(')')

    if aexp.find('+') > 0:
        idx = aexp.find('+')
        result = "{}({},{})".format('+',aexp[:idx], aexp[idx+1:])
        return result
    if aexp.find('-') > 0:
        idx = aexp.find('-')
        result = "{}({},{})".format('-',aexp[:idx], aexp[idx+1:])
        return result
    if aexp.find('*') > 0:
        idx = aexp.find('*')
        result = "{}({},{})".format('*',aexp[:idx], aexp[idx+1:])
        return result
    if aexp.find('/') > 0:
        idx = aexp.find('/')
        result = "{}({},{})".format('/',aexp[:idx], aexp[idx+1:])
        return result


def rpn(aexp):
    """
    aexp:str = a string containing an arithmatical expression
    return:str = the RPN form of aexp
    """
    result = ''
    if aexp.find('*') > 0:
        idx = aexp.find('*')
        if aexp[aexp.find('*') + 1:].find('*') < 0:
            result = "{}({},{})".format('*', rpn_heper(aexp[:idx]), rpn_heper(aexp[idx + 1:]))
        else:
            idx = aexp[aexp.find('*') + 1:].find('*')
            result = "{}({},{})".format('*', rpn_heper(aexp[:idx]), rpn_heper(aexp[idx + 1:]))

    if aexp.find('/') > 0:
        idx = aexp.find('/')
        if aexp[aexp.find('/') + 1:].find('/') < 0:
            result = "{}({},{})".format('/', rpn_heper(aexp[:idx]), rpn_heper(aexp[idx + 1:]))
        else:
            idx = aexp[aexp.find('/') + 1:].find('/')
            result = "{}({},{})".format('/', rpn_heper(aexp[:idx]), rpn_heper(aexp[idx + 1:]))
    return result

"""
20
8 Evaluating an arithmetical tree

Let t1 be an arithmetical tree: all labels are operators
(one of +,*,/,-) and all leaves are (quoted) ints. For example

t1 = Tree('*',Tree('+',Tree(23,None,None),Tree(5,None,none)),Tree(17,None,None))

which is the result of parsing ((23 + 5) * 17)

t2 = Tree('-',Tree(3,None,None))

Define a function _val_ which takes an arithmetical tree as an argument
and returns the numerical value of the parsed expression.

Ex: val(t1) ==> 476
"""

def val(atr):
    """
    atr:an arithmetical tree
    return: value of the expression it parses
    """
    a = [self.label]
    if self.left != None:
        a += val(self.left)
    if self.right != None:
        a += val(self.right)

    return a

def val_helper(lst):
    exp = ''
    if len(lst)==3:
        exp = '({}{}{})'.format(lst[1],lst[0],lst[2],)
    if len(lst)==7:
        exp = '(({}{}{}){}({}{}{}))'.format(lst[2],lst[1],lst[3],lst[0],lst[5],lst[4],lst[6])
    if len(lst) == 5:
        if lst[1] == '-' or '+' or '*' or '/' :
            exp = '(({}{}{}){}{})'.format(lst[2],lst[1],lst[3],lst[0],lst[4])
        else:
            exp = '({}{}({}{}{}))'.format(lst[1],lst[0],lst[3],lst[2],lst[4])

    return(eval(exp))

"""
50
9 PROP
"""

"""
Define a class of propositions, made up of variables (strings),
the operators 'and','or','implies','not' and parentheses.
"steal" ideas from this week's lecture notes on Trees.

"(X and Y) implies Z"
"""


class Prop(object):
    def __init__(self, oper, var1, var2):
        assert type(oper) == str
        assert type(var1) == str
        assert type(var2) == str
        self.oper = oper
        self.var1 = var1
        self.var2 = var2

    def __str__(self):
        return self.var1 + " " + self.oper + " " +self.var2
