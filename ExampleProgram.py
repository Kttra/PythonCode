## Kttra

## Inches to Meters
def inchesToMeters(inches):
    '''Convert inches to meters given inches
    Parameter inches expects number representing inches
    Return result is the conversion of inches to meters'''
    meters_per_in = 0.0254
    result = inches * meters_per_in
    return result

## Pounds to Kg
def poundsToKgs(pounds):
    '''Convert pounds to Kgs
    Parameter pounds expects number representing pounds
    Return result is the conversion of pounds to Kgs'''
    pounds_per_kg = 0.453592
    result = pounds * pounds_per_kg
    return result
 
## Calculate BMI
def bmi(height,weight):
    '''Calculate BMI given weight and height
    Parameter height expects number representing height in meters
    Parameter weight expects number representing weight in Kg
    Return result is the BMI'''
    body_mass_index = weight/(height*height)
    return body_mass_index

## Determine BMI and gives BMI level
def bodyMassIndex():
    '''Calculate BMI given weight and height and gives BMI category'''
    name = input("Please enter the subject's name: ")
    height = float(input("Please enter the subject's height in inches: "))
    weight = float(input("Please enter the subject's weight in pounds: "))
    weight = poundsToKgs(weight)
    height = inchesToMeters(height)
    bmi_person = bmi(height,weight)
    print(name,"has a body mass index of:",bmi_person)
    if bmi_person < 18.5:
        print(name,"is underweight.")
    elif 25 <= bmi_person < 30:
        print(name, "is overweight")
    elif 18.5 < bmi_person < 25:
        print(name, "is normal weight.")
    else:
        print(name, "is obese.")

bodyMassIndex()
