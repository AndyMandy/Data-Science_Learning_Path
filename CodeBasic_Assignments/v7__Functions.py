'''

Question: Write a function called calculate_area that takes base and height as an input and returns and area of a
triangle. Equation of an area of a triangle is,

area = (1/2)*base*height

Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape
type it will calculate area. Equation of rectangle's area is,

rectangle area=length*width
'''


def calculate_area(base, height, shape='triangle'):
    if shape == 'rectangle':
        area = base * height
    elif shape == 'triangle':
        area = (1/2)*base*height
    return area


dim1 = int(input('Please input dimension 1 of object'))
dim2 = int(input('Please input dimension 2 of object'))
shapeOfObject = input('Please mention shape of an object')

areaOfObject = calculate_area(dim1, dim2, shapeOfObject)
print(areaOfObject)


'''

Question: Write a function called print_pattern that takes integer number as an argument and prints following pattern
if input number is 3,
*
**
***

'''

num = input('Please enter number of lines in pattern')
num = int(num)
for rows in range(1, num+1):
    s = ''
    for star in range(rows):
        s = s + '*'
    print(s)