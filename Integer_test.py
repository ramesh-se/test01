_author_ = 'Ramesh'

## Using Int
"""
def Integer_fun(a, b):
    # Write your code here
    c = int(a)
    d = int(b)
    type(a)
    type(b)
    print(c)
    print(d)
    type(c)
    type(d)

"""

# Using Int Operations
"""
def find(num1, num2, num3):

    bResult1 = bool(num1<num2 and num2>=num3)
    bResult2 = bool(num1>num2 and num2<=num3)
    bResult3 = bool(num3==num1 and num1!=num2)
    print(bResult1,bResult2,bResult3)
"""
# Using Int Math operations
"""
def Integer_Math(Side, Radius):
    # Write your code here

    Area of Square = a * a
    Volume of Cube = a * a * a
    Are of Cirle = pi * (r * r)
    Volume of Sphere = 4/3 * (pi (r*r*r))

    valPi = 3.14
    valAreaofSquare = pow(Side,2)
    valVolumeofCube = pow(Side,3)
    valRadius = float(Radius)
    sqrRadius = float(pow(valRadius,2))
    cubeRadius = float(pow(valRadius,3))
    valAreaofCircle = round((valPi * sqrRadius),2)
    valVolumeofSphere = round(((4 / 3) * valPi * cubeRadius),2)

    print("Area of Square is", valAreaofSquare)
    print("Volume of Cube is", valVolumeofCube)
    print("Area of Circle is", valAreaofCircle)
    print("Volume of Sphere is", valVolumeofSphere)
"""
## Using float1
"""
def triangle(n1, n2, n3):
    # Write your code here
    import math
    height = float(n1)
    base = float(n2)
    #print(type(height), type(base))
    AreaofTriangle = round((height * base) / 2, 1)
    valofPI = round(math.pi,n3)
    print((AreaofTriangle,valofPI))
    return(AreaofTriangle,valofPI)
"""


## Using float2
"""
def Float_fun(f1, f2, Power):
    # Write your code here
    #fAdd = f1 + f2
    #fSubtract = f1 - f2
    print("#Add",end="\n")
    print(f1 + f2)
    print("#Subtract")
    print(f1 - f2)
    print("#Multiply")
    print(f1 * f2)
    print("#Divide")
    print(f2 / f1)
    print("#Remainder")
    print(f1 % f2)
    print("#To_The_Power_Of")
    fPower = pow(f1,Power)
    print(fPower)
    print("#Round")
    print(round(fPower,4))
"""

# Usage Imports
def calc(c):
    # Write your code here
    import math

    #print((c / (2 * math.pi)))
    fRadius = c / (2 * math.pi)
    rndRadius = round(fRadius,2)
    print(fRadius)
    #
    #print(math.pi * (fRadius ** 2))
    fArea = (math.pi * pow(fRadius,2))
    rndArea = round(fArea,2)
    print(fArea)
    #
    print((rndRadius,rndArea))
    return(rndRadius,rndArea)


#def find(num1, num2, num3):
if __name__ == "__main__":
    #find(10, 7, 8)
    #triangle(9, 5, 4)
    #Float_fun(10.75,5.45,3)
    calc(8)
