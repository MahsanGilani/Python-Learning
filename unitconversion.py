import os
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("************ Main Page ************")
    print("1- Kilogram/gram \n2- Meter/Centimeter")
    try:
        n = int(input("Choose a conversion: ").strip())
        if n == 1:
            # kg/gram
            os.system('cls' if os.name == 'nt' else 'clear')
            print("************ Second Page ************")
            print("1- Kilogram To gram")
            print("2- Gram To Kilogram")
            k = int(input("Choose a conversion: ").strip())
            if k == 1:
                try:
                    
                    kilo = float(input("write the weight in kilogram: ").strip())
                    
                    print(f"your weight in gram is {kilo*1000}")
                    # print(input("\nPress any key to exit..."))
                    break
                except:
                    
                    print(
                        "Oh :(( the number/character you entered is out of our support")
            elif k == 2:
                try:
                    gram = float(input("write the weight in gram: ").strip())
                    print(f"your weight in kilogram is {gram/1000}")
                    # print(input("\nPress any key to exit..."))
                    break
                except:
                    print(
                        "Oh :(( the number/character you entered is out of our support")
            else:
                print("you choose wrong number :(\nyou return to page one")
                continue
        elif n == 2:
            # m/cm
            os.system('cls' if os.name == 'nt' else 'clear')
            print("************ Second Page ************")
            print("1- meter To centimer")
            print("2- centimeter To meter")
            k = int(input("Choose a conversion: ").strip())
            if k == 1:
                try:
                    meter = float(input("write the number in meter: ").strip())
                    print(f"your number in centimeter is {meter*100}")
                    # print(input("\nPress any key to exit..."))
                    break
                except:
                    print(
                        "Oh :(( the number/character you entered is out of our support")
            elif k == 2:
                try:
                    centimeter = float(
                        input("write the number in centimeter: ").strip())
                    print(f"your number in meter is {centimeter/100}")
                    # print(input("\nPress any key to exit..."))
                    break
                except:
                    print(
                        "Oh :(( the number/character you entered is out of our support")
            else:
                print("you choose wrong number :(\nyou return to page one")
                continue
        else:
            print("ummmmmmmm, you write wrong\nBack to Page 1")
            continue
    except:
        print("ummmmmmmm, you write wrong\nif you want convertion, please run program again")
        break

# print("Oh :(( the number/character you entered is out of our support\nif you want convertion, please run program again")
print(input("\nPress any key to exit..."))
