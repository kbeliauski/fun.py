"""
Kiryl Beliauski
Sorting, invariants and classes
"""

"""
0
"""

"""
Add pre and post-conditions and loop invariant
to the following code using mathematical notation.
Notice that the input is mutated and that nothing is returned.
Thus the three statements must mention 'lst'

"""

def insert_in_place_mutate(item,lst):
    """
    @requires: lst is an ORDERED list of numbers or strings
               (or anything that can be compared with <) and
               item is an object of the same type
    @ensures: the function adds item to lst in such a way as to maintain order. lst is mutated
    """
    inserted= False
    index = 0
    if lst == [] or item > lst[-1]:
        lst.append(item)
    else:
        #LI: item > lst[index] and index < lst.length
        while not inserted:
            if item <= lst[index]:
                lst.insert(index,item)
                inserted = True
            else:
                index = index + 1

def insert_in_place_return(item,lst):
    """
    @requires: lst is an ORDERED list of numbers or strings
               (or anything that can be compared with <) and
               item is an object of the same type
    @ensures: \result is an ordered list consisting of the elements of lst and item
    """
    mylst = lst[:]
    inserted= False
    index = 0
    if mylst == [] or item > mylst[-1]:
        mylst.append(item)
    else:
        # LI: item > lst[index] and index < lst.length
        while not inserted:
            if item <= mylst[index]:
                mylst.insert(index,item)
                inserted = True
            else:
                index = index + 1
    return mylst



"""
Now implement insertion_sort
"""

def insertion_sort(lst):
    """
    @requires: lst is a list of numbers or strings (or
    anything that can be compared with <)  
    @ensures: \result is an ordered list consisting of the elements of lst
    """
    for i in range(1, len(lst)):
        key = lst[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position

        j = i - 1
        # LI: j>0 and key < i in lst[i:key]
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return  lst


print(insertion_sort([4.5,7.9,0,2,5,6.1,3,4.6,2]))

"""
1
"""

"""
Define a time class with all the methods that were discussed in the lecture (you can just copy them from the lecture). In addition, implement the special methods for comparing times. Add pre and post conditions to all the methods.

Note that the correspondence between operator symbols and method names is as follows: x<y calls x.__lt__(y),
x<=y calls x.__le__(y),

x==y calls x.__eq__(y),
 x!=y and x<>y call x.__ne__(y),
  x>y calls x.__gt__(y),
   and x>=y calls x.__ge__(y)

"""


class Time(object):
    def __init__(self, hour, min, sec):
        """
        @requires: hours,mins,secs are positive integers and 0<=mins,secs<60
        @ensures: constructs a Time object
        """
        self.hour = hour
        self.min = min
        self.sec = sec

    def __str__(self):
        #reqires: none
        #ensures: returns string when printed
        return str(self.hour) + ":" + str(self.min) + "::" + str(self.sec)

    def __lt__(self, other):
        """
        @requires: other is an object of type Time
        @ensures: \result is True iff self comes before other
        """
        return self.hour < other.hour or \
               self.hour == other.hour and self.min < other.min or \
               self.hour == other.hour and self.min == other.min and self.sec < other.sec

    def __eq__(self, t):
        # reqires: other time
        # ensures: true if self == t
        return self.hour == t.hour and \
               self.min == t.min and \
                self.sec == t.sec


    def __ne__(self, t):
        # reqires: other time
        # ensures: true if self != t
        return self.hour != t.hour and \
               self.min != t.min and \
               self.sec != t.sec

    def __gt__(self, t):
        # reqires: other time
        # ensures: true if self > t
        return self.hour > t.hour or \
               self.hour == t.hour and self.min > t.min or \
               self.hour == t.hour and self.min == t.min and self.sec > t.sec

    def __le__(self, other):
        """
        @requires: other is an object of type Time
        @ensures: \result is True iff self does not come after other
        """
        return not self.__gt__(other)

    def __ge__(self, other):
        # reqires: other time
        # ensures: true if self >= t
        return not self.__lt__(other)


t1 = Time(3, 50, 20)
t2 = Time(3, 55, 20)
print(t1 < t2)

t1 = Time(3, 55, 20)
t2 = Time(3, 55, 20)
print(t1 < t2)
print(t1 <= t2)



"""
Now complete the class definitions below (implement the methods and write pre and post conditions)
"""


class Event(object):
    def __init__(self, name, time):
        """
        @requires: name is a string and time is a Time object
        @ensures: constructs an Event object
        """
        self.name = name
        self.time = time

    def __str__(self):
        # reqires: none
        # ensures: returns string when printed
        return "At " + str(self.time) + " --> " + self.name

    def __eq__(self, other):
        """
        @requires: other is an object of type Event
        @ensures: \result is True iff self and other have the same name and time
        """
        return self.name == other.name and self.time == other.time

    def __ne__(self, other):
        # reqires: other event
        # ensures: true if self == other
        return self.name != other.name and self.time != other.time

    def __lt__(self, other):
        # reqires: other event
        # ensures: true if self < other
        return (self.time < other.time) or \
               (self.time == other.time and self.name < other.name)

    def __gt__(self, other):
        # reqires: other event
        # ensures: true if self > other
        return (self.time > other.time) or \
               (self.time == other.time and self.name > other.name)

    def __le__(self, other):
        # reqires: other event
        # ensures: true if self <= other
        return not self.__gt__(other)

    def __ge__(self, other):
        # reqires: other event
        # ensures: true if self >= other
        return not self.__lt__()


class Sched(object):
    def __init__(self, event_list):
        """
        @requires: event_list is a list of Events
        @ensures: constructs am Sched object
        """
        self.event_list = event_list

    def __str__(self):
        # reqires: none
        # ensures: returns string when printed
        "this is your schedule"

    def sort(self):
        # reqires: none
        # ensures: return sorted event list
        self.event_list = insertion_sort(self.event_list)

    def print_agenda(self):
        # reqires: none
        # ensures: prints each event with time
        for event in self.event_list:
            print("At " + str(event.time) + " --> " + str(event.name))


s = Sched([Event("dentist", Time(3, 50, 20)), Event("meeting", Time(2, 30, 00)), \
           Event("COMP211_sec1", Time(5, 25, 10)), Event("COMP211_sec2", Time(5, 25, 10))])
s.print_agenda()

# this should print:
# At 2:30::0 --> meeting
# At 3:50::20 --> dentist
# At 5:25::10 --> COMP211_sec1
# At 5:25::10 --> COMP211_sec2



"""
2
"""

"""
Define a complex numbers class. The class must contain two data attributes: the real and imaginary part of the complex number. In addition, we would like to add, subtract, multiply, and divide complex numbers.
"""


class Complex():
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        self.real += other.real
        self.imag += other.imag

    def __sub__(self, other):
        self.real -= other.real
        self.imag -= other.imag

    def __mul__(self, other):
        self.real = self.real * other.real - self.imag * other.imag
        self.imag = self.imag * other.real + self.real * other.imag

    def __div__(self, other):
        self.real = (self.real * other.real + self.imag * other.imag)/(other.real**2 + other.imag**2)
        self.imag = (self.imag * other.real - self.real * other.imag)/(other.real**2 + other.imag**2)


"""
3
"""

"""
Implement two functions, one that prints a complex number and one that parses a string to a complex number.    
    Here are some examples to illustrate how your methods are expected to work:

        >>> to_str(Complex(2,3))
        2 + 3i

        >>> to_str(Complex(2.5,1))
        2.5 + i

        >>> to_str(Complex(2,0))
        2

        >>> to_str(Complex(0,3))
        3i

        >>> to_str(Complex(2,-3))
        2 - 3i

The function from_str is expected to be capable of parsing strings of the forms above (e.g. "2+3i", "2-i" ,etc)
The more user-friendly your methods are, the more points you will get.

You also need to complete the pre and post conditions to your functions.

"""


def to_str(number):
    """
    @requires: number is an object of type Complex
    @ensures: \result is a string representing number
    """
    imag = ''
    real = ''
    if number.imag > 0:
        if number.imag == 1:
            imag = ''
        else:
            imag = '+' + str(number.imag)

    elif number.imag < 0:
        if number.imag == -1:
            imag = '-'
        else:
            imag = str(number.imag)
    if number.real != 0:
        real = str(number.real)

    if number.imag == 0:
        return real
    else:
        return real + imag + 'i'


def from_str(s):
    """
    @requires: s is a string representing a complex number
    @esnsures: \result is an object of type Complex obtained by parsing s
    """
    if s == 'i':
        return Complex(0, 1)
    elif s == '-i':
        return Complex(0, -1)
    elif ((s[0] == '-') or (type(s[0]) == int)) and (('+' not in s[1:]) or ('-' not in s[1:])) and (s[-1] != 'i'):
        return Complex(s, 0)
    elif (('+' not in s) or (s[0] == '-')) and (('+' not in s[1:]) and ('-' not in s[1:])) and (type(s[0]) != int):
        return Complex(0, s[:-1])
    elif (len(s) > 2) and (s[0].isnumeric() or s[0] == '-'):
        if '+' in s:
            if len(s[s.find('+') + 1:-1]) == 0:
                return Complex((s[:s.find('+')]), 1)
            else:
                return Complex(s[:s.find('+')], s[s.find('+') + 1:-1])
        if '-' in s:
            if len(s[s.find('-') + 1:-1]) == 0:
                return Complex((s[:s.find('-')]), -1)
            else:
                return Complex(s[:s.find('-')], s[s.find('-') + 1:-1])


print(to_str(Complex(3, 2)))
print(to_str(Complex(-3, -1)))
print(to_str(Complex(3, -1)))
print(to_str(Complex(-3, 1)))
print(to_str(Complex(1, 0)))
print(to_str(Complex(0, 1)))
print(to_str(Complex(0, -1)))
print(to_str(Complex(-1, 0)))

print(to_str(Complex(3.234, 2.24)))
print(to_str(Complex(-3.14, -1.24)))
print(to_str(Complex(3.15, -1.16)))
print(to_str(Complex(-3.87, 1.787)))
print(to_str(Complex(3.4, 0)))
print(to_str(Complex(0, 4.2)))
print(to_str(Complex(0, -5.6)))
print(to_str(Complex(-1.5, 0)))

c = from_str("3+2i")
print(c.real, c.imag)
c = from_str("3+i")
print(c.real, c.imag)
c = from_str("3-i")
print(c.real, c.imag)
c = from_str("2i")
print(c.real, c.imag)
c = from_str("i")
print(c.real, c.imag)
c = from_str("-i")
print(c.real, c.imag)
c = from_str("-1")
print(c.real, c.imag)

c = from_str("3.4+2.13i")
print(c.real, c.imag)
c = from_str("3.345+i")
print(c.real, c.imag)
c = from_str("3.56-i")
print(c.real, c.imag)
c = from_str("2.78i")
print(c.real, c.imag)
c = from_str("i")
print(c.real, c.imag)
c = from_str("-i")
print(c.real, c.imag)
c = from_str("-1.35")
print(c.real, c.imag)



