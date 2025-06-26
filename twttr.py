
def main():
    twttr = input("Input: ")
    vowels = "AEIOUaeiou"
    filtered = ""

    for c in twttr:
        if not c in vowels:
            filtered += c

    print("Output:", filtered)


if __name__ == "__main__":
    main()

#submit50 cs50/problems/2022/python/twttr
