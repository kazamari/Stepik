'''
You are given a description of a pyramid made of cubes in the XML format.
The cubes can be of three colors: red (red), green (green) and blue (blue).
We know the color of each cube, and the cubes, located directly under it.

Example:
    <cube color="blue">
      <cube color="red">
        <cube color="green">
        </cube>
      </cube>
      <cube color="red">
      </cube>
    </cube>

Let us introduce the concept of a value for the cubes. The top cube, corresponding to the root of the XML document, has
a value of 1. The cubes, located right below it, have a value of 2. The cubes below these ones have a value of 3.
And so on.

The value of a color equals to the sum of values of all cubes of this color.

Output the three space-separated numbers: the values of red, green and blue colors.

Sample Input:
    <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

Sample Output:
    4 3 1
'''

# Posted from PyCharm Edu
from xml.etree import ElementTree

def count_value(color, elem, value=1):
    res = 0
    if elem.tag == 'cube' and \
        'color' in elem.attrib.keys() and \
        color == elem.attrib['color']:
        res += value
    for el in elem:
        res += count_value(color, el, value+1)
    return res

xml = input()
root = ElementTree.ElementTree(ElementTree.fromstring(xml)).getroot()
print(count_value('red', root), count_value('green', root), count_value('blue', root))


