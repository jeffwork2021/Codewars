# Grade book
# 
# Complete the function so that it finds the average of the three scores passed 
# to it and returns the letter value associated with that grade.
# Numerical Score 	Letter Grade
# 90 <= score <= 100 	'A'
# 80 <= score < 90 	'B'
# 70 <= score < 80 	'C'
# 60 <= score < 70 	'D'
# 0 <= score < 60 	'F'
# 
# Tested values are all between 0 and 100. Theres is no need to check for 
# negative values or values greater than 100.
def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    if (avg >= 0 and avg < 60):
        return 'F'
    elif (avg >= 60 and avg < 70):
        return 'D'
    elif (avg >= 70 and avg < 80):
        return 'C'
    elif (avg >= 80 and avg < 90):
        return 'B'
    elif (avg >= 90 and avg <= 100):
        return 'A'
    else:
        return 'Unknown'