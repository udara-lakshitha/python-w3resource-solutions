# 4. Circle Area Calculator

import math

def calculate_circle_area(radius: float) -> float:
    '''
    This function is calculating the area of a circle for given radius
    '''
    return math.pi * radius ** 2

if __name__ == '__main__':
    user_radius = float(input("Enter the radius: "))
    area = calculate_circle_area(radius = user_radius)
    print(f"The area of the circle is: {area:.2f}")