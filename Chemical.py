#This is my 1st program
def take_input():
    level = (input("Enter the current level of ethenol in the tank:"))
    return level

def action(level):
    if level>(900.0/100)*80:
        print "close the valve"
    else:
        if level<(900.0/100)*20:
            print "buy more liquid"
        else:
            print "level of ethenol in the tank is",level
    
level=take_input()
action(level)
