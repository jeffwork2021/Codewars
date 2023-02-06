# Write function bmi that calculates body mass index (bmi = weight / height**2).
# 
# if bmi <= 18.5 return "Underweight"
# 
# if bmi <= 25.0 return "Normal"
# 
# if bmi <= 30.0 return "Overweight"
# 
# if bmi > 30 return "Obese"
def bmi(weight, height):
    val = weight / height**2
    if val <= 18.5:
        return "Underweight"
    elif val <= 25.0:
        return "Normal"
    elif val <= 30.0:
        return "Overweight"
    elif val > 30:
        return "Obese"
    else:
        return ""

