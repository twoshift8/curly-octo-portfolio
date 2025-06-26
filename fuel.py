

def main():
    x = get()
    if x <= 1:
        print("E")
    elif x >= 99:
        print ("F")
    else:
        print(f"{round(x)}%")

def get():
    while True:
        try:
            [a, b]=input("Fraction: ").split("/")
            a = a.strip()
            b = b.strip()
            if a <= b:
                return (float(a) / float(b))*100

        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()

#submit50 cs50/problems/2022/python/fuel
