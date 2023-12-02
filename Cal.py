#Paul Lichtenwalner
#plichtenwalner1@student.gsu.edu    palichtenwalner@gmail.com
#CSC 1301   CRN 91957
#Create a Calendar for an inputted month and year
#Input a month and year (Command line input)
#Output a correctly formatted calendar

def formatTop():
    monthLength = len(monthStr)
    yearLength = len(yearStr)
    numSpaces = (20 - (monthLength + yearLength)) // 2
    for i in range(0, numSpaces):
        print(" ", end = '')
    print(monthStr, yearStr)

def formatDays():
    print('Su Mo Tu We Th Fr Sa')

def printDays():
    if(dayOfWeek == 0):
        nextDate = 8
        print(' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7')
    elif(dayOfWeek == 1):
        nextDate = 7
        print('  ', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6')
    elif(dayOfWeek == 2):
        nextDate = 6
        print('  ', '  ', ' 1', ' 2', ' 3', ' 4', ' 5')
    elif(dayOfWeek == 3):
        nextDate = 5
        print('  ', '  ', '  ', ' 1', ' 2', ' 3', ' 4')
    elif(dayOfWeek == 4):
        nextDate = 4
        print('  ', '  ', '  ', '  ', ' 1', ' 2', ' 3')
    elif(dayOfWeek == 5):
        nextDate = 3
        print('  ', '  ', '  ', '  ', '  ', ' 1', ' 2')
    elif(dayOfWeek == 6):
        nextDate = 2
        print('  ', '  ', '  ', '  ', '  ', '  ', ' 1')
    if(monthNum == 1 or monthNum == 3 or monthNum == 5 or monthNum == 7
       or monthNum == 8 or monthNum == 10 or monthNum == 12):
        totalDays = 31
    elif(monthNum == 4 or monthNum == 6 or monthNum == 9 or monthNum == 11):
        totalDays = 30
    elif(monthNum == 2):
        if(yearNum % 100 == 0):
            if(yearNum % 400 == 0):
                totalDays = 29
            else:
                totalDays = 28
        elif(yearNum % 4 == 0):
            totalDays = 29
        else:
            totalDays = 28
    count = 1
    for i in range(nextDate, totalDays + 1):
        if(count % 7 == 0):
            if(nextDate < 10):
                print('', nextDate, '')
            elif(nextDate >= 10):
                print(nextDate)
        else:
            if(nextDate < 10):
                print('', nextDate, '', end = '')
            elif(nextDate >= 10):
                print(nextDate, '', end = '')
        nextDate = nextDate + 1
        count = count + 1
            
import sys

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
monthNum = int(sys.argv[1])
monthStr = months[monthNum - 1]
yearNum = int(sys.argv[2])
yearStr = str(yearNum)
formatTop()
formatDays()
from datetime import date
dayOne = date(yearNum, monthNum, 1)
dayOfWeek = (dayOne.weekday() + 1) % 7
printDays()