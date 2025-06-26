
def main():
    cart = get_item()
    for item in cart:
        print(cart[item], item)

def get_item():
    cart = {}
    while True:
        try:
            item = input().strip().upper()
            if item.isalpha():
                if item in cart:
                    cart[item] += 1
                else:
                    cart[item]=1
        except ValueError:
            pass
        except EOFError:
            break
        else:
            pass
    return cart

if __name__=="__main__":
    main()

#check50 cs50/problems/2022/python/grocery
