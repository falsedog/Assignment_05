#------------------------------------------#
# Title: CDInventory.py
# Desc: Script CDINventory to store CD Inventory data
# Change Log: (Who, When, What)
# Rain Doggerel, 2022 Nov 06, Finishing
# Rain Doggerel, 2022 Nov 02, Scaffolding
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#
import sys
if len(sys.argv) > 1:
    filename = sys.argv[1] # Allow a filename to be passed for funsies
else:
    filename = 'CDInventory.txt'
    
# This is 'if file doesn't exist then create it'
with open(filename,'a') as existenceTouch:
    existenceTouch.write('')

# Initialize some things mostly to just stave off warnings
newCDtitle = 'Untitled'
newCDartist = 'Unknown Artist'
menuChoice = '5'

# To justify having save happen under a separate interaction
# we try to keep the inventory in memory this way
cdInventory = []
with open(filename,'r') as inventoryRead: 
    for line in inventoryRead.readlines():
        cdInventory.append(line.rstrip().split(','))
print(type(cdInventory))
print(cdInventory)
print('Length ' + str(len(cdInventory)))

while True: #It's a nicer program as a loop
# 1. Display menu allowing the user to choose: 'Add CD', 'Display Current Inventory', 'Save Inventory to file' and 'exit'
    # Considering clearing the screen here but apparently I'd have 
    # to do some OS specific things so maybe I won't
    print('Let\'s inventory your CDs. Make a choice:')
    print('1. Add CD 2. Display Current Inventory 3. Save 4. Exit')
    menuChoice = input()
    print() # Separating next display from input for increased clarity

# 2. Add data to the table (2d-list) each time the user wants to add data
    if menuChoice == '1':
        newCDtitle = input('Hey what\'s the album titled? ')
        newCDartist = input('And what cool band did this album? ')
        cdIndex = str(len(cdInventory) + 1) # Very important cast for fixing type errors
        cdInventory.append([cdIndex,newCDtitle,newCDartist])
        print(cdInventory[int(cdIndex) - 1]) # And uncast lol

# 3. Display the current data to the user each time the user wants to display the data
    elif menuChoice == '2':
        i = 0
        while i < len(cdInventory):
            print(str(cdInventory[i][0]) + '\tAlbum: ' + cdInventory[i][1] + '\tArtist: ' + cdInventory[i][2])
            i = int(i) + 1 # Why this has to be type cast here I can't fathom

# 4. Save the data to a text file CDInventory.txt if the user chooses so
    elif menuChoice == '3':
        # Considered append but if I'm writing trash data it's not much
        # worse to be appending it than overwriting
        with open(filename,'w') as inventoryWrite:
            gonnaWrite = '' # Cleaning for future saves
            i = 0
            while i < len(cdInventory):
                gonnaWrite += ','.join(cdInventory[i])
                gonnaWrite += '\n'
                i = i + 1
            inventoryWrite.write(gonnaWrite)

# 5. Exit the program if the user chooses so.
    elif menuChoice == '4':
        break
    else:
        print('Hm that choice wasn\'t valid, let try again')
        continue
