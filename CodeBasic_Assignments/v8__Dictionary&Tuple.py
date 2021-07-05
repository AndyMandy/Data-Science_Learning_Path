'''

================== Problem Statement 1 ======================

'''
population = {'China': 143, 'India': 136, 'USA': 32, 'Pakistan': 21}

'''

i. Using above create a dictionary of countries and its population
ii. Write a program that asks user for three type of inputs
a. print: if user enter print then it should print all countries with their population in this format,
    china==>143
    india==>136
    usa==>32
    pakistan==>21
    
b. add: if user input add then it should further ask for a country name to add. If country already exist in our dataset
    then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new
    country/population in our dictionary and print it
c. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove
    it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
d. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print
    population of that country.
    
'''

print('we have population data of several countries. Here are the commands that you can try \n'
      'a. print: to print data set \n'
      'b. add: to let you add new data set \n'
      'c. remove: to remove existing countries data set \n'
      'd. query: to get the data of specific country \n')

command = input('please give a command')


def search_country(country_name):
    for i in population:
        if i == country_name:
            return 1


if command == 'print':
    for key in population:
        print(key+' ==> '+str(population[key]))
elif command == 'add':
    newCountry = input('Which country data you want to add?')
    isFound = search_country(newCountry)
    if isFound != 1:
        newPopulation = input('Please enter population')
        population[newCountry] = newPopulation
        print('New Data set: ', population)
    else:
        print('Data for this country is already present in data set')
elif command == 'remove':
    toBeDeleted = input('Which country you want to remove?')
    isFound = search_country(toBeDeleted)
    if isFound == 1:
        del population[toBeDeleted]
        print('New Data set: ', population)
    else:
        print('No such country found in data set')
elif command == 'query':
    toBeFetched = input("Which country's population you want?")
    isFound = search_country(toBeFetched)
    if isFound == 1:
        print(str(population[toBeFetched])+' Cr.')
    else:
        print('No such country found in data set')


'''
=================== Problem Statement 2 ======================
'''

Stock = {
    'info': [600, 630, 620],
    'ril': [1430, 1490, 1567],
    'mtl': [234, 180, 160]
}

'''
Write a program that asks user for operation. Value of operations could be,
    print: When user enters print it should print following,
        info ==> [600, 630, 620] ==> avg:  616.67
        ril ==> [1430, 1490, 1567] ==> avg:  1495.67
        mtl ==> [234, 180, 160] ==> avg:  191.33
    add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list
    (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your 
    dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
'''

print('we have data set of stocks. Here are the commands that you can try \n'
      'a. print: to print data set \n'
      'b. add: to let you add new data set \n'
      )

userInput = input('Please give an input: ')


def search_stock(new_stock):
    for i in Stock:
        if i == new_stock:
            return 1


if userInput == 'print':
    for key in Stock:
        print(key + ' ==> ' + str(Stock[key]) + ' ==> Avg: ' + str(round(sum(Stock[key]) / len(Stock[key]), 2)))
elif userInput == 'add':
    newTicker = input('Which ticker you want to add? ')
    isFound = search_stock(newTicker)
    if isFound != 1:
        stockNumber = int(input('Please provide number of stock values: '))
        newStockData = []
        for stock in range(1, stockNumber+1):
            ele = int(input())
            newStockData.append(ele)
        Stock[newTicker] = newStockData
    print(Stock)
