
# Get which way the bus goes.
print('Choose which way the bus goes:')
print ('1. Kontula\n2. Mellunmäki')
choice = input()

def choices():
    if choice == 1:
        print("22")
        oneway()
    elif choice == 2:
        print("11")
        otherway()

if choice == "1" or choice == "2":
    # execute CallApi.py
    choices()
    print('nice')
else:
    print('Please press 1 or 2')
    
def oneway():
    print("Kontula")


def otherway():
    print("Mellunmäki")

