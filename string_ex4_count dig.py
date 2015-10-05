def get_num():
    number = (input("Enter an integer : "))
    return number

def count_dig(num):
    print "Number of digits in this number is : ", len(str(num))

num = get_num()
count_dig(num)

          
