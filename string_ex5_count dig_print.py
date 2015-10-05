def get_num():
    number = (input("Enter an integer : "))
    return (number)

def count_dig(num):
    count = len(str(num))
    if count == 1:
        print num+7
    else:
        if count == 2:
            power = str(num ** 5)
            print power[-2:]
        else:
            if count == 3:
                number2 = (input("Enter another integer : "))
                add = str(num + number2)
                print add[-3:]
            else:
                print "Its not a 3 digit number"
        
num = get_num()
count_dig(num)
