def bmi_calc():
    unit = input(' (M)etric or (I)mperial? ')
    if unit.upper() == "I":                             #Imperial Calculations
        weight = float(input('How much do you weigh in lbs? '))
        Height = float(input('How tall are you in inches? '))
        bmi = 703 * weight / Height ** 2
    elif unit.upper() == "M":                            #Metric Calculations
        weight = float(input('How much do you weigh in Kgs? '))
        Height = float(input('How tall are you in meters? '))
        bmi = weight / Height ** 2
    else:
        print('Please put either "M" or "I" to choose which unit you want')
        bmi_calc()
    return bmi

                                                    #this function classifies the different bmi ratings
def bmi_rate(bmi):
    status = ""
    if bmi <= 18.4:
        status = 'under weight'
    elif bmi >= 18.5 and bmi <= 24.9:
        status = 'normal'
    elif bmi >= 25 and bmi <= 29.9:
        status = 'over weight'
    elif bmi >= 30 and bmi < 34.9:
        status = 'obesity (class 1)'
    elif bmi >= 35 and bmi <= 39.9:
        status = 'obesity (class 2)'
    else:
        status = 'obesity (class 3)'
    print(f"Your BMI is {bmi} which means you are {status}")

bmi_rate(bmi_calc())