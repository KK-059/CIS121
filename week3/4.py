age=int(input('Enter your age:'))
goal=input('Enter your Athleticism:')
if age>=20 and age<40:
    if goal=='below average':
        print ('resting heartrate is 73-93')
    elif goal=='above average':
        print('resting heart rate is is 47-72')
elif age>=40 and age<60:
    if goal=='below average':
        print ('resting heartrate is 72-94')
    elif goal=='above average':
        print('resting heart rate is is 46-71')
elif age>=45 and age<70:
    if goal=='below average':
        print ('resting heartrate is 71-97')
    elif goal=='above average':
        print('resting heart rate is is 45-70')



