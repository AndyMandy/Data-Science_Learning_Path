'''

Using following list of cities per country,
    india = ["mumbai", "banglore", "chennai", "delhi"]
    pakistan = ["lahore","karachi","islamabad"]
    bangladesh = ["dhaka", "khulna", "rangpur"]

    i. Write a program that asks user to enter a city name and it should tell
       which country the city belongs to
'''

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

cityName = input('Enter the name of city your city')

if cityName in india:
    print('You are Indian!')
elif cityName in pakistan:
    print('You are Pakistani')
elif cityName in bangladesh:
    print('You are Bangladeshi')
else:
    print("I don't know which country you belong to!")


'''
# ii. Write a program that asks user to enter two cities and it tells you if 
they both are in same country or not. For example if I enter mumbai and chennai,
it will print "Both cities are in India" but if I enter mumbai and dhaka it 
should print "They don't belong to same country"
'''

city1 = input('Please enter names of the first city')
city2 = input('Please enter names of the second city')

if city1 in india and city2 in india:
    print('Both cities are in India')
elif city1 in pakistan and city2 in pakistan:
    print('Both cities are in Pakistan')
elif city1 in bangladesh and city2 in bangladesh:
    print('Both cities are in Bangladesh')
else:
    print("They don't belong to same country")

'''
=========================================================================

2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal

'''

sugarLevel = input('Enter your fasting sugar level')
sugarLevel = int(sugarLevel)

if sugarLevel < 80:
    print('Sugar level is low')
elif sugarLevel > 100:
    print('Sugar level is high')
else:
    print('Sugar level is normal')
