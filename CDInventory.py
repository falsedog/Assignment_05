#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# Rain Doggerel, 2022-Nov-13, adapted in my work from Assignment04 re: loading
# Rain Doggerel, 2022-Nov-12, change to dicts + deletion section
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#

# Declariables
strChoice = '' # User input
delChoice = '' # Deletion choice
lstTbl = []  # list of dicts to hold data
dictRow = {"ID":"","Title":"","Artist":""}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

print('The CD Inventory\n')

while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break

    if strChoice == 'l':
        lstTbl = [] # Probably would be ideal to let the user know this overwrites existing work
        with open(strFileName,'r') as inventoryRead: 
            for line in inventoryRead.readlines():
                tempLoadList = line.rstrip().split(',') #To keep the append arguments clea(r/n)er
                lstTbl.append({"ID":int(tempLoadList[0]),"Title":tempLoadList[1],"Artist":tempLoadList[2]})

    elif strChoice == 'a':
        # 2. Add data to the table (list of dicts) each time the user wants to add data
        strID = input('Enter an ID: ')
        # Might should try to catch failures of int inputs here
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dictRow = {"ID":intID, "Title":strTitle, "Artist":strArtist}
        lstTbl.append(dictRow)

    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID \tCD Title \tArtist')
        for row in lstTbl:
            print(str(row['ID']) + " \t" + row['Title'] + " \t" + row['Artist'])

    elif strChoice == 'd':
        print('Delete which ID entry?')
        delChoice = input()
        for row in lstTbl:
            if row['ID'] == int(delChoice):
                lstTbl.remove(row)
                print('Found it and removed it')
                break
        else: # Hmm a bit surprised this seems to work like I hoped...
            print('No such ID found')
            
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w') # Must become write or saves and loads become cancerous
        strRow = '' # Clear for potential repeated saves
        for row in lstTbl: # I think I don't prefer this way, but I didn't want to change it too too much
            strRow += str(row['ID']) + ',' + row['Title'] + ',' + row['Artist'] + '\n'
        objFile.write(strRow)
        objFile.close()
    
    else:
        print('Please choose either l, a, i, d, s or x!')
