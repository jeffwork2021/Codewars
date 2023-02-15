# This kata is about multiplying a given number by eight if it is an even 
# number and by nine otherwise.
def simple_multiplication(number) :
    return (9 if number % 2 == 1 else 8) * number
