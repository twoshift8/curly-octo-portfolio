
name = input("camelCase: ").strip()
'''
for each character c in the name:
    if c is uppercase:
        add '_' + c.lower() the output
    else:
        add c to the output

then print the output
'''

def snake(name):
    for c in name:
        if c.isupper():
            print("_"+c.lower(), end="")
        else:
            print(c, end="")
    return print()


if __name__ == "__main__":
    snake(name)



#submit50 cs50/problems/2022/python/camel
