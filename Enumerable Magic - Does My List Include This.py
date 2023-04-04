# Create a method that accepts a list and an item, and returns true if the item 
# belongs to the list, otherwise false.
def include(arr,item):
    try:
        return arr.index(item) > -1
    except ValueError:
        return False
    