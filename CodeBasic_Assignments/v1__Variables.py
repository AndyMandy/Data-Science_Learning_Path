'''

Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see.


break=5
  File "<stdin>", line 1
    break=5
         ^
SyntaxError: invalid syntax

#Answer: This happened because break is reserved keyword in python.

'''

'''
Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables

Answer:
'''

birthYear = 1997
currentYear = 2021
myAge = currentYear - birthYear
print(myAge)

'''
Store your first, middle and last name in three different variables and then print your full name using these variables
'''

firstName="Monkey"
middleName="D."
lastName="Luffy"
print(firstName+" "+middleName+" "+lastName)

'''
Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue


Answer: All except record1 and record_one
'''