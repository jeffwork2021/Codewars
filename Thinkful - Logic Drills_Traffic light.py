# Description:
# 
# You're writing code to control your town's traffic lights. You need a 
# function to handle each change from green, to yellow, to red, and then to # 
# green again.
# 
# Complete the function that takes a string as an argument representing the 
# current state of the light and returns a string representing the state the 
# light should change to.
# 
# For example, when the input is green, output should be yellow.
def update_light(current):
    lights = ['green', 'yellow', 'red']
    return lights[(lights.index(current)+1)%3]

print(update_light('green'))
print(update_light('yellow'))
print(update_light('red'))