
while True:
    print("1- Kilogram/gram \n2- Meter/Centimeter")
    try:
        n = int(input("Choose a conversion: "))
        if n==1:
            # kg/gram
            print("1- Kilogram To gram")
            print("2- Gram To Kilogram")
            k = int(input("Choose a conversion: "))
            if k==1:
                kilo = float(input("write the weight in kilogram: "))
                try :
                    print(f"your weight in gram is {kilo*1000}")
                    print(input("\nPress any key to exit..."))
                except:
                    raise Exception("Oh :(( the number/character you entered is out of our support")
            elif k==2:
                gram = float(input("write the weight in gram: "))
                try :
                    print(f"your weight in kilogram is {gram/1000}")
                    print(input("\nPress any key to exit..."))
                except:
                    raise Exception("Oh :(( the number/character you entered is out of our support")
            else:
                print("you choose wrong number :(\nyou return to page one")
                continue
        elif n==2:
            # m/cm
            print("1- meter To centimer")
            print("2- centimeter To meter")
            k = int(input("Choose a conversion: "))
            if k==1:
                meter = float(input("write the number in meter: "))
                try :
                    print(f"your number in centimeter is {meter*100}")
                    print(input("\nPress any key to exit..."))
                except:
                    raise Exception("Oh :(( the number/character you entered is out of our support")
            elif k==2:
                centimeter = float(input("write the number in centimeter: "))
                try :
                    print(f"your number in meter is {centimeter/1000}")
                    print(input("\nPress any key to exit..."))
                except:
                    raise Exception("Oh :(( the number/character you entered is out of our support")
            else:
                print("you choose wrong number :(\nyou return to page one")
                continue
    except:
        raise Exception
    break

print("Oh :(( the number/character you entered is out of our support\nif you want convertion, please run program again")
print(input("\nPress any key to exit..."))
