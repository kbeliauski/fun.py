"""
   *****************************
   *HW 6.0_classes_skel.py     *
   *Kiryl Beliauski            *
   *****************************
"""

import math

"""
1
"""
"""
Define a class called 'Backpack'.

A backpack object is characterized by two attributes:  a list of its contents,
and an integer that specifies how many more items can be added to the backpack.
When a backpack is created, it is initially empty (i.e., its contents list is
the empty list) and its remaining capacity is specified as a parameter to the
constructor.  Your backpack definition must have the following methods:
  - an __init__ method that takes a maximum capacity as a parameter
  - a __str__ method that reports how many items are in the backpack and how
    many more can be put in;
  - a method named put_in that has a single parameter; when put_in(x) is
    invoked on a backpack object, x is added to the contents list and the
    remaining capacity is reduced by one.  If the remaining capacity is 0 when
    the method is invoked, this method just returns without doing anything.
  - a method named take_out that has a single parameter; when take_out(x) is
    invoked on a backback object, then if x is in the contents list, it is
    removed and the remaining capacity is increased by one; otherwise the
    contents list and remaining capacity are unchanged.

    For a more interesting backpack, assume that the objects are always strings,
    and that the space that each string takes up is equal to the number of
    characters in the string.
"""
class Backpack:
    def __init__(self,capacity):
        self.contents=[]
        self.capacity = capacity

    def __str__(self):
        return "Backpack: {} items & room for {}".\
          format(len(self.contents),self.capacity)

    def put_in(self,x):
        if len(self.contents) < self.capacity:
            self.contents.append(x)
            self.capacity -= 1
    def take_out(self,x):
        if x in self.contents:
            self.contents.remove(x)
            self.capacity += 1


"""
2
"""
"""
Define a Date class. Its fields should
be month, day and year. Give it an __init__ and
__str__ method.
Define a 'before' function[NOT METHOD]
that takes two dates d1, d2 as input and
returns a boolean: true if d1 comes before d2, otherwise false
"""

class Date:

    months = [0,'jan','feb','mar','april']
    
    
    def __init__(self,x,y,z):
        self.month = x
        self.day = y
        self.year = z

    def __str__(self):
         return Date.months[self.month]+'. '+ str(self.day)+', '+str(self.year)

def before(d1,d2):
    """
    d1,d2: dates
    return:bool - whether or not d1 comes before d2
    """
    if d1.year > d2.year:
        return False
    elif d1.year == d2.year and d1.month > d2.month:
        return False
    elif d1.month == d2.month and d1.day >= d2.day:
        return False
    return True

d1 = Date(1,2,1312)
print(d1)

"""
2.5
"""

#Do the same, but call the class Date1, and include
#'before' as a METHOD
#Then add a test at the end for this method

class Date1:

    def __init__(self, x, y, z):
        self.month = x
        self.day = y
        self.year = z

    def __str__(self):
        return Date.months[self.month] + '. ' + str(self.day) + ', ' + str(self.year)

    def before(self,d):
        """
        d: Date1
        return:bool - whether or not d1 comes before d2
        """
        if self.year <d.year:
            return True
        elif self.year == d.year:
            if self.month < d.month:
                return True
            else:
                if self.day < d.day:
                    return True
        return False

    def __lt__(self,d):
        return self.before(d)

    def __eq__(self,d):
        return self.year == d.year and self.month == d.month and self.day == d.day

    
    
d1 = Date1(1,1,1111)
d2 = Date1(1,1,1900)

print(d1 < d2)
print(d1 == d2)

if d1 < d2:
     print("HI")

    

"""
3
"""

"""
Define a 'Drink_machine' class to
implement a coke/pepsi machine

fields: two ints: cokes, pepsis
that keep track of the number of cokes/pepsis in the machine

add methods to remove a coke or a pepsi

if out of drink print: "out of coke" or
"out of pepsi"

methods:
  __str___
  remove_coke
  remove pepsi
"""

class Drink_machine:
    def __init__(self,c,p):
        self.cokes = c
        self.pepsis = p

    def __str__(self):
        return "["+self.cokes*'c'+" : "+self.pepsis*'p'+"]"

    def remove_coke(self):
        if self.cokes > 0:
            self.cokes -= 1
        else:
            print( "out of coke")

    def remove_pepsi(self):
        if self.pepsis > 0:
            self.pepsis -= 1
        else:
            print( "out of pepsi")

    


print("========= backpack ============")
b = Backpack(4)
b.put_in('book')

print(b,"contents = ", b.contents)
b.put_in('book')
print(b,"contents = ", b.contents)
b.put_in('pencil')
print(b,"contents = ", b.contents)
b.put_in('eraser')
print(b,"contents = ", b.contents)
b.put_in('phone')
print(b,"contents = ", b.contents)
b.take_out('book')
print(b,"contents = ", b.contents)
b.take_out('pencil')
print(b,"contents = ", b.contents)

print( "============ Date ==============")
d1 = Date(3,21,2000)
d2 = Date(4,7,2016)
print(d1,d2,before(d1,d2))
print(d1,d2,before(d2,d1))
print( "============== soft drink machine =============")
m = Drink_machine(1,2)
print(m)
m.remove_coke()
m.remove_pepsi()
print(m)
m.remove_coke()
print(m)
print("=========== test for Date1 class=============")
d1 = Date1(3,21,2000)
print (d1)
d2 = Date1(4,7,2016)
print(d2)
print(d1.before(d2))
print(d2.before(d1))
