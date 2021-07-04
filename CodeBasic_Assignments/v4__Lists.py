'''

1. Let us say your expense for every month are listed below,
    January - 2200
    February - 2350
    March - 2600
    April - 2130
    May - 2190

    Create a list to store these monthly expenses and using that find out,

        1. In Feb, how many dollars you spent extra compare to January?
        2. Find out your total expense in first quarter (first three months) of the year.
        3. Find out if you spent exactly 2000 dollars in any month
        4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
        5. You returned an item that you bought in a month of April and
           got a refund of 200$. Make a correction to your monthly expense list
           based on this

'''

listOfExpense = [['January', 'February', 'March', 'April', 'May'], [2200, 2350, 2600, 2130, 2190]]

print('In Feb, you spent $ '+str(listOfExpense[1][1]-listOfExpense[1][0])+' extra compare to January')
print('Total expenses :$ '+str(sum(listOfExpense[1])))
print('Did I spent exact $2000 in any month? ', (2000 in listOfExpense[1]))
listOfExpense[0].append('June')
listOfExpense[1].append(1980)
listOfExpense[1][3] = listOfExpense[1][3] - 200
print('Expenses of April after returning $200 are: $ ', listOfExpense)

'''
2. You have a list of your favourite marvel super heroes.

Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

'''

heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print(len(heroes))
heroes.append('Black Panther')
heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
heroes.insert(3, 'Black Panther')
heroes[1:3] = ['doctor strange']
heroes.sort()
print(heroes)