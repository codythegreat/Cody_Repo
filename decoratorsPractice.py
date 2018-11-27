#! python3
# This is a file that I will use to practice decorators.

# DEFINITION:
#	Decorators provide a simple syntax for calling higher-order functions
#	They are functions that take another function to extend the function
#	you are working on without actually modifying code.

# To begin, first we need to understand that functions are first-class
# objects. This means that functions can be passed around in a similar
# manner to that of an object. functions can also be arguments.

cody = 'Cody'

def say_hello(name):
	return(f'hello {name}.')

def say_hi_to_cody(say_hi_to):
	return say_hi_to(cody)

print(say_hi_to_cody(say_hello))

# notice that we passed in the function without the parenthesis. This 
# means that we passed a reference of the function. We specify the arg
# inside of the function at (cody).

# note that we can also have functions inside of other functions:

def parent():
	print('Parent function.')

	def child1():
		print('Chlid1 function.')

	def child2():
		print('Child2 function.')

	child1()
	child2()

parent()

# note that these functions only exist inside of the parent function, and
# the order in which they are listed doesn't matter. 

# note that python does allow you to return functions as return values:

def parent2(num):

	def child1():
		print('child1')

	def child2():
		print('child2')

	if num == 1:
		return child1

	if num == 2:
		return child2

	else:
		print('invalid entry.')

parent2(1)
parent2(2)
parent2(4538)

# Notice that we are returning the child functions without parenthesis.
# there are references to the functions. We could then make another 
# function that will call these functions directly:

first = parent2(1)

first()

# Now we can make our own decorator; note the following example:

def masterFunc(func):
	def wrapper():
		print('says something')
		func()
		print('says something again')
	return wrapper

def say_Cody():
	print('Cody')

say_Cody = masterFunc(say_Cody)

say_Cody()

# We are now pointing the say_Cody function towards the wrapper of our 
# masterFunc function. inside that function we are calling the say_Cody
# function. We are decorating our say_Cody function by wrapping it and 
# modifying its behavior.

# so how is this useful? note the following example:

cody = 4

def overdue_book_checker(func):
	def wrapper():
		if cody > 5:
			print('Too many books are overdue to rent another.')
		else:
			func()
	return wrapper

def rent_book_for_cody():
	print('Cody has rented Moby Dick.')

rent_book_for_cody = overdue_book_checker(rent_book_for_cody)

rent_book_for_cody()

# in this example we added functionality to the rent_book_for_cody funct.
# we defined a wrapper that will check to see how many books cody has 
# rented. if the number exceeds five, then we will not let cody rent a 
# book. 

# the code above is fairly clunky, so what we will do instead is use the
# @ symbol to designate a decorator to use, and python will do the rest of
# the work for us!

codyM = 10

def overdue_book_checker2(func):
	def wrapper():
		if codyM > 5:
			print('Too many books are overdue to rent another.')
		else:
			func()
	return wrapper

@overdue_book_checker2
def rent_book_for_cody2():
	print('Cody has rented Moby Dick.')

rent_book_for_cody2()

# the addition of the simple @overdue_book_checker2 does all of the work
# of the code in the first example. 

# a common practice is to have your decorators in a module, and then 
# importing the decorators as you need them

# You'll also see the name wrapper a lot for inner functions. This is okay
# so long as we give a meaningful name to the outer function containing 
# the decorator.

# Now lets say that you have a function that takes arguments, yet you want
# to use a generic decorator on it. You could do the following:

def do_twice(func):
	def wrapper_do_twice(*args, **kwargs):
		func(*args, **kwargs)
		func(*args, **kwargs)
	return wrapper_do_twice

# We can use the *args and **kwargs to specify the function to take any 
# amount of arguments and keyword arguments (including none). This will
# the above decorator to work with nearly any function.

# note that if you need your wrapper to return something when used, you
# will have to add the following line:	return func(*args, **kwargs)

# one of the features of python is that each function and object knows 
# what it is. This changes when you begin adding decorators to functions.
# to fix the information of decorated functions we can add the following 
# line outside the wrapper function:	@functools.wraps(func)
#										(note: import functools first)

# note the following example of a real world use of a decorator:

import functools
import time

def timer(func):
	@functools.wraps(func)
	def wrapper_timer(*args, **kwargs):
		start = time.time()
		value = func(*args, **kwargs)
		end = time.time()
		difference = end - start
		print(f'function was completed in {round(difference, 2)} seconds.')
		return value
	return wrapper_timer

@timer
def add_some_amounts():
	time.sleep(1.4)
	return (456581687+45837487684+137879+8768415884) 

print(add_some_amounts())

# here we have created a decorator function that will time a function to 
# see how long it takes for that function to execute its code. Note that
# we can recycle this decorator to be used on other functions.

# now we will create a debug decorator that will print the arguments a 
# function is called with as well as its return value:

def debug(func):
	@functools.wraps(func)
	def wrapper_debug(*args, **kwargs):
		args_repr = [repr(a) for a in args]
		kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
		signature = ', '.join(args_repr + kwargs_repr)
		print(f'calling {func.__name__}({signature})')
		value = func(*args, **kwargs)
		print(f'{func.__name__!r} returned {value!r}')
		return value
	return wrapper_debug

@debug
def function1(number, number2):
	new_num = 0
	for i in range(number):
		new_num += number2^i
	print(new_num)
	return new_num

function1(69, 234)

# here we create a debug function. You can see how this could be very
# useful when working with code that is now behaving the way that you 
# want it to.

# you could also build a decorator that slows code down. Say you have code
# that you want to observe piece by piece, but it is running too fast. We
# could simple sleep the code for few seconds
