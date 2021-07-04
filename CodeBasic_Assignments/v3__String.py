'''

1. Create 3 variables to store street, city and country, now create address variable to store entire address. Use two
 ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a
 that the street, city and country prints in a separate line


'''

street = 'Hudson St.'
city = 'New York'
country = 'USA'

print(street+', '+city+', '+country)

'''
2. Create a variable to store the string "Earth revolves around the sun"
   Print "revolves" using slice operator
   Print "sun" using negative index

'''

statement = 'Earth revolves around the sun'
print(statement[6:13])
print(statement[-3:])

'''

3. Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y
fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

'''

x = 5
y = 2
print('I eat '+str(x)+' veggies and '+str(y)+' fruits daily')
