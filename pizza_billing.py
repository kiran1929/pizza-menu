print("welcome to CRUNCH IT....")
bill=0
size=input("enter the size of the pizza (S/M/L)")
if size=='s' or size=='S':
    bill=100
    print("small pizza has been added rs:",bill)
    peproni=input("do you want to add peproni (y/n)?")
    if peproni=='y' or peproni=='Y':
        bill+=20
        cheese=input("do you want to add cheese(y/n)?")
        if cheese=='y' or cheese=='Y':
            bill+=30
            print(f"your total bill is {bill} only")
        else:
           print(f"your bill is {bill} only")
    else:
        cheese=input("do you want to add cheese(y/n)?")
        if cheese=='y' or cheese=='Y':
            bill+=30
            print(f"your total bill is {bill} only")
        print(f"your bill is {bill} only")
elif size=='m' or size=='M':
    bill=200
    print("medium pizza has been added rs:",bill)
    peproni=input("do you want to add peproni (y/n)?")
    if peproni=='y' or peproni=='Y':
        bill+=25
        cheese=input("do you want to add cheese(y/n)?")
        if cheese=='y' or cheese=='Y':
            bill+=40
            print(f"your total bill is {bill} only")
        else:
            print(f"your bill is {bill} only")
    else:
        cheese=input("do you want to add cheese(y/n)?")
        if cheese=='y' or cheese=='Y':
            bill+=30
            print(f"your total bill is {bill} only")
        print(f"your bill is {bill} only")
elif size=='l' or size=='L':
    bill=300
    print("large pizza has been added rs:",bill)
    peproni=input("do you want to add peproni (y/n)?")
    if peproni=='y' or peproni=='Y':
        bill+=30
        cheese=input("do you want to add cheese(y/n)?")
        if cheese=='y' or cheese=='Y':
            bill+=50
            print(f"your total bill is {bill} only")
        else:
            print(f"your bill is {bill} only")
    else:
        cheese=input("do you want to add cheese(y/n)?")
        if cheese=='y' or cheese=='Y':
            bill+=30
            print(f"your total bill is{bill} only")
        print(f"your bill is {bill} only")
else:
    print("enter the correct size of the pizza")
