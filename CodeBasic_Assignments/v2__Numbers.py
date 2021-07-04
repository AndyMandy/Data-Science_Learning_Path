'''

Question: You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and
print it.

'''

fieldLength = 92
fieldWidth = 48.8

print(round(fieldLength * fieldWidth, 2))

'''

Question: You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20
dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

'''

noOfChipsPackets = 9
eachPacketPrice = 1.49
pricePaid = 20

print("Money that you will get back is: $", pricePaid-(noOfChipsPackets*eachPacketPrice))

'''

Question: You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 
500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python 
(Hint: Use power operator ** to find area of a square)

'''

lengthOfBathroom = 5.5
areaOfBathroom = 5.5**2

costPerSquareFeet = 500

print("Total Cost: Rs", areaOfBathroom*costPerSquareFeet)

'''

Question: Print binary representation of number 17

'''

num = 17
print("Binary representation of 17 is:",format(num, 'b'))