def shout(word="yes"):
    return word.capitalize()+"!"

#print shout()

scream = shout
print scream()

del shout
#try:
    #print shout()
#except NameError, e:
    #print e

#print scream()

###################################

def talk():
    def whisper(word="yes"):
        return word.lower() + "..."

    print whisper()

#talk()

#try:
#        print whisper()
#except NameError, e:
#        print e
        #outputs : "name 'whisper' is not defined"*
        #Python's functions are objects'

##################################

def getTalk(kind="shout"):
    def shout(word="yes"):
        return word.capitalize() + "..."

    def whisper(word="yes"):
        return word.lower() + "..."

    if kind == "shout":
        return shout
    else:
        return whisper

talk0 = getTalk
print "print talk0"
print talk0()

talk = getTalk()
print "print talk"
print talk

print "print talk() "
print talk()

print "print getTalk("+ "whisper" +")() "
print getTalk("whisper")()
