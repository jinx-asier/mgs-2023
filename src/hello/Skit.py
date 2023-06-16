
# to solve quadratic equations
import math


# defines the function
def Quad(a, b, c):
    # does the quadratic equation - because of the '±' there has to be two separate equations
    print({(-b + math.sqrt(b**2 - 4 * a * c))/(2 * a),
           (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)})


# calls the function
Quad(int(input("a here>>>")), int(input("b here>>>")), int(input("c here>>>")))
