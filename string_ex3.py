def get_sentence():
    sent=raw_input("Enter a sentence : ")
    return sent

def function(sent):
    count=len(sent)/2
    print "Last character in this sentence : ", sent[-1]
    print "Last 5 characters in this sentence : ", sent[-5:]
    print "2nd and 5th character in this sentence : ", sent[2],sent[5]
    print "center character in this sentence : ", sent[count-1:count+2]

sent=get_sentence()
function(sent)
