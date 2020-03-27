import sys
randomList = ["a",0,2]

for entry in randomList:
    try:
        print("the entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops",sys.exc_info()[0],"occured.")
        print("Next entry.")
print("The reciprocal of",entry,"is",r)