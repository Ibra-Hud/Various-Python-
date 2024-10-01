import csv

file = open("Districts.csv")



def loadData(choice):
    if choice == 1:
        print(displayCounties())
        return loadData(int(input('Enter Menu Choice: ')))
    elif choice == 2:
        print(displayDistricts())
        return loadData(int(input('Enter Menu Choice: ')))
    else:
        print('Good Bye')

def showMenu():
    print('1) Counties')
    print('2) Districts')
    print('3) Quit')

def displayCounties():
    counties = []
    for line in file:
        counties.append(line[0])
    return counties

def displayDistricts():
    districts = []
    for line in file:
        districts.append(line[1])
        districts.append(line[2])
        districts.append(line[3])
    return districts

showMenu()
loadData(int(input('Enter Menu Choice: ')))
displayCounties()

