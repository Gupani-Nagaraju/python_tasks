message = "This is a Global variable"

def modify_list(lst):
    print("List before Modifications", lst)
    lst.append(199)
    print("List After Modifications", lst)
    
def modify_tuple(tup):
    print("Tuple before Modifications", tup)
    try:
        tup[1] = 199
    except TypeError :
        print("I told you already Tuple cannot be modified")
    print("Result after experiments on tuple",tup)


def slicing():
    message = "This is for Slicing"
    print(message)
    print(message[:3])
    print(message[::-1])
    
def scoping():
    message = "This is a Local message"
    print(message)

lst = list(map(int, input("Enter your input seperated by spaces").split()))

tap = tuple(map(int, input("Enter your input seperated by spaces").split()))

modify_list(lst)

modify_tuple(tap)

slicing()

scoping()