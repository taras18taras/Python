# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.
from string import Template
def say_hi(name, age):
    """
        Hi!
    """
    return"Hi. My name is {} and I'm {} years old".format(name, age)
    #return "Hi. My name is Alex and I'm 32 years old"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    #print(say_hi("Alex", 32))
    print("Hi. My name is {} and I'm {} years old".format('Oleg', 52))
   # print(say_hi("Frank", 68))
    say_hi1 = "Hi. My name is {} and I'm {} years old".format
    print(say_hi1('Taras',23))
   # help(str.format)



def say_hi1(name, age):
    """
        Hi!
    """
    t = Template("Hi. My name is $name and I'm $age years old")
    return t.substitute(name=name, age=age)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi1("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi1("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')



def say_hi2(name, age):
    return "Hi. My name is " + name + " and I'm " + str(age) + " years old"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi2("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi2("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')




def say_hi3(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"
print(say_hi3("Alex", 32))