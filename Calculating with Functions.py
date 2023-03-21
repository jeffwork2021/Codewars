# This time we want to write calculations using functions and get the results. 
# Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
#
# Requirements:
#
#     There must be a function for each number from 0 ("zero") to 9 ("nine")
#     There must be a function for each of the following mathematical 
# operations: plus, minus, times, divided_by
#     Each calculation consist of exactly one operation and two numbers
#     The most outer function represents the left operand, the most inner 
# function represents the right operand
#     Division should be integer division. For example, this should return 2, 
# not 2.666666...:
#
# eight(divided_by(three()))
def zero(s=''): return eval(f'0 {s}')
def one(s=''): return eval(f'1 {s}')
def two(s=''): return eval(f'2 {s}')
def three(s=''): return eval(f'3 {s}')
def four(s=''): return eval(f'4 {s}')
def five(s=''): return eval(f'5 {s}')
def six(s=''): return eval(f'6 {s}')
def seven(s=''): return eval(f'7 {s}')
def eight(s=''): return eval(f'8 {s}')
def nine(s=''): return eval(f'9 {s}')

    
def plus(s=''): return f'+{s}'
def minus(s=''): return f'-{s}'