'''

1. Question: After flipping a coin 10 times you got this result,
    result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
    Using for loop figure out how many times you got heads

'''

result = ["heads", "tails", "tails", "heads", "tails", "heads", "heads", "tails", "tails", "tails"]

timesHead = 0
key = "heads"

for i in result:
    if key == i:
        timesHead = timesHead + 1

print("Head appeared "+str(timesHead)+" times in result")

'''

Question 2: Print square of all numbers between 1 to 10 except even numbers

'''

for num in range(1, 11):
    if num % 2 != 0 or num == 1:
        print(num*num)


'''

Question: Your monthly expense list (from Jan to May) looks like this,

expense_list = [2340, 2500, 2100, 3100, 2980]

Write a program that asks you to enter an expense amount and program should tell you in which month that expense 
occurred. If expense is not found then it should print that as well.

'''

expense_list = [2340, 2500, 2100, 3100, 2980]
listOfMonth = ["Jan", "Feb", "Mar", "Apr", "May"]

token = input("Please enter expense amount to search")
token = int(token)
foundFlag = 0
for i in range(len(expense_list)):
    if expense_list[i] == token:
        print("This was expense of month: ", listOfMonth[i])
        foundFlag = 1
        break


if foundFlag == 0:
    print("This expense was not found in the list")



'''

Question:Write a program that prints following shape

*
**
***
****
*****
'''

print("\nExercise pattern 1\n")

for rows in range(1, 6):
    s = ''
    for col in range(rows):
        s = s+'*'
    print(s)

print("\nExercise pattern 2\n")

for rows in range(1, 6):
    s=''
    spaces = 5-rows
    for col in range(spaces):
        s = s + ' '
    for col in range(rows):
        s = s + '*'
    print(s)
