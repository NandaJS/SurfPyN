def get_fname():
    fname=raw_input("Enter first name : ")
    return (fname)

def get_lname():
    lname=raw_input("Enter last name : ")
    return (lname)

def print_name(fname,lname):
    print "Name :",fname.lower(),",", "Sirname :",lname.lower()
    print fname.upper(),lname.upper()
    print "-" * 20
    print fname.title(),",",lname.title()

fname=get_fname()
lname=get_lname()
print_name(fname,lname)
