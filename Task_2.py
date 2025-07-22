import math
def Calc(n):
    squrt = math.sqrt(n)
    loga = math.log(n)
    sine = math.sin(n)
    return f"Square root: {squrt} \nLogarithm: {loga} \nSine: {sine}"

print(Calc(int(input("Enter the number: "))))
