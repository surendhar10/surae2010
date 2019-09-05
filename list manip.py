list=[]
a=True
while(a):
    print("1-INSERTION")
    print("2-DELETION")
    print("3-UPDATION")
    print("4-SEARCHING")
    a=int(input("choose any one manipulation:"))
    if(a==1):
        print("5-INSERTION AT FIRST")
        print("6-INSERTION AT LAST")
        print("7-INSERTION AT SPECIFIC POSITION")
        b=int(input("choose any one:"))
        if(b==5):
            element=int(input("enter a element:"))
            list.insert(0,element)
            print("the value is inserted at first")
            print(list)
        if(b==6):
            element=int(input("enter a element:"))
            list.append(element)
            print("the value is inserted at last")
            print(list)
        if(b==7):
            index=int(input("enter a index:"))
            element=int(input("enter a element:"))
            list.insert(index,element)
            print("the value is inserted at specific position")
            print(list)
    if(a==2):
        element=int(input("enter a element to delete:"))
        list.remove(element)
        print("the value is deleted")
        print(list)
    if(a==4):
        element=int(input("enter a value to search:"))
        if(element in list):
            print("the value is available in list")
        else:
            print("the value is unavailable")
    if(a==3):
        c=int(input("enter a value to update:"))
        if(c in list):
            d=int(input("enter a new value "))
            for i in range(0,len(list)):
                if(list[i]==c):
                    list[i]=d
                    print("the value is updated")
                    print(list)
                    
