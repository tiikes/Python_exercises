import math
radius = 8
def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

area = calculate_circle_area(radius)
print(area)