import math
radius = int(input('Enter the radius of circle:'))
def area(radius):
    circle_area = math.pi*radius**2
    return circle_area
print(area(radius))