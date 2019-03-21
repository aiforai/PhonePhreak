#PhonePreak by CyberA
#Generates Random Phone Numbers based on area code
'''
- v1: Functional Programming, currently supports N.American Telephone Standard only.
'''

import random

def ask_areacode():
    areacode = input("Define your area-code: ")
    return areacode

def first_three():
    #print(random.randint(111,999))
    return random.randint(111,999)
def last_four():
    return random.randint(1111,9999)

def phone_number():
    firstThree = first_three()
    lastFour = last_four()
    areaCode = ask_areacode()
        
    if(areaCode == "666"):
        print("I'm not sure Satan will like that.")
    elif(areaCode == "555"):
        print("555 WE TIP!")
    elif (areaCode == "404"):
        print("NOT FOUND.")
    elif (areacode == "800"):
        print("Thank you for calling Microsoft Tech Support, this is [REDACTED] Speaking.")

    print(areaCode + "-"+str(firstThree)+"-"+str(lastFour))

        
phone_number()
runner = input("Generate again? ")
while(runner != "NO" or runner != "no" or runner != "n" or runner != "N" or runner!="No"):
    if(runner == "YES" or runner == "yes" or runner == "y" or runner == "Y" or runner=="Yes"):
        phone_number()
        runner = input("Generate again? ")
        
    else:
        break
    


    
