# Complete the function which returns the weekday according to the input number:
#
#     1 returns "Sunday"
#     2 returns "Monday"
#     3 returns "Tuesday"
#     4 returns "Wednesday"
#     5 returns "Thursday"
#     6 returns "Friday"
#     7 returns "Saturday"
#     Otherwise returns "Wrong, please enter a number between 1 and 7"

def whatday(num):
    a = ["Sunday", "Monday", "Tuesday", 
         "Wednesday", "Thursday", "Friday", "Saturday"]
    return a[num-1] if 8 > num > 0 \
                    else "Wrong, please enter a number between 1 and 7"
