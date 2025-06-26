
num=input("Expression: \n").strip()

def main():
    x, y, z = num.split(" ")
    first = (float(x))
    second = (float(z))
    if y == "-":
        return first-second
    elif y == "+":
        return first + second
    elif y == "/":
        return first/second
    elif y == "*":
        return first*second


def deci():
    print(f"{main():.1f}")

deci()

#check50 cs50/problems/2022/python/interpreter
