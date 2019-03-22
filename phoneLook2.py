import random
areacode = input("Define your area-code: ")
howmany = (int(input("Specify generation amount: ")))

def generator():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1)) #billions
    return areacode + '-' + n[3:6] + '-' + n[6:]
for i in range(howmany):
    print(generator())
runner = input("Generate again? ")

while(runner != "NO" or runner != "no" or
      runner != "n" or runner != "N" or runner!="No"):
    if(runner == "YES" or runner == "yes" or runner == "y" or runner == "Y" or runner=="Yes"):
        for i in range(howmany):
            print(generator())
        runner = input("Generate again? ")
    else:
        print("Logging off.")
        break


    
