def get_fname():
    fname=raw_input("Enter 1st name : ")
    return fname

def get_lname():
    lname=raw_input("Enter last name : ")
    return lname

def get_initial(fname,lname):
    count=len(lname)
    for i in range(count): 
        print fname[:-i],lname[:-i]
          
fname=get_fname()
lname=get_lname()
get_initial(fname,lname)


