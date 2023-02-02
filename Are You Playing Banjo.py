# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# 
# The function takes a name as its only argument, and returns one of the following strings:
# 
# name + " plays banjo" 
# name + " does not play banjo"
# 
# Names given are always valid strings.
def are_you_playing_banjo(name):
    return "{} plays banjo".format(name) if name[0:1].upper() == "R" else "{} does not play banjo".format(name)