from Stack00 import Stack

def divideBy2 (decNumber):
    remstack= Stack()

    while decNumber>0:
        rem = decNumber%2 #nilainya 2 kemungkinan yaitu 0 dan 1
        remstack.push(rem)
        decNumber = decNumber//2

    binString=""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString
print(divideBy2(42))
 
