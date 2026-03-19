""" 
Name: Gabby Crespo
Section: 275-02
Description: Lab 4 
"""

import math


"""
Function Name: getList
Parameters: none
Return Type: List
Description: Prompts user to fill in an empty list until they are satisfied 
"""
def getList():
    nums = []
    print("Enter a list of integers or 'w' to end the list")
    check = True
    while check:
        tomato = input("Enter an integer: ")
        if tomato == 'w':
            check = False
        else:
            num = int(tomato)
            nums.append(num)
    return nums

""" 
Function Name: printMenu
Parameters: none
Return Type: none
Description: Prints menu for statistics calculator
"""
def printMenu():
    print("Please choose an option.")
    print("1. Min")
    print("2. Max")
    print("3. Mean")
    print("4. Median")
    print("5. Clear List")
    print("0. Exit")
  

"""
Function Name: getMean
Parameters: List
Return Type: Float
Description: Calculates the mean for the list and returns the value 
"""
def getMean(userList):
    if len(userList) == 0:
        return 0
    total = 0
    for num in userList:
        total = total + num
    mean = total / len(userList)
    return mean

"""
Function Name: getMedian
Parameters: List
Return Type: Float
Description: Calculates the median for the list and returns the value  
"""
def getMedian(userList):
    if len(userList) == 0:
        return 0
    sortedlist = sorted(userList)
    n = len(sortedlist)
    if n % 2 == 1:
        median = sortedlist[n // 2]
    else:
        mid1 = sortedlist[n //2 - 1]
        mid2 = sortedlist[n // 2]
        median = (mid1 + mid2) / 2
    return median
""" 
Function Name: getMin
Parameters: List
Return Type: Float
Description: Finds the minimum of the unsorted list
"""
def getMin(userList):
    if len(userList) == 0:
        return 0
    min = userList[0]
    i = 1
    while i < len(userList):
        if userList[i] < min:
            min = userList[i]
        i = i + 1
    return min

""" 
Function Name: getMax
Parameters: List
Return Type: Float
Description: Finds the maximum of the unsorted list
"""
def getMax(userList):
    if len(userList) == 0:
        return 0
    max = userList[0]
    i = 1
    while i < len(userList):
            if userList[i] > max:
                max = userList[i]
            i = i + 1
    return max
""" 
Function Name: getStdDev
Parameters: List
Return Type: none
Description: Calculates the population Standard Deviation of a list
"""
def getStdDev(userList):
    if len(userList) == 0:
        return 0
    mean = getMean(userList)
    n = len(userList)
    SSE = 0
    for x in userList:
        SSE += (x - mean) ** 2
    variance = SSE / n
    std_dev = math.sqrt(variance)
    return std_dev


def main():
    print("Welcome to the List Statistics Calculator")
    my_list = getList()
    boogie = True
    while boogie:
        printMenu()
        option = input("Please enter your choice, or 0 to exit: ")
        if option == '0':
            boogie = False
        elif option == '1':
            print("The minimum value is", getMin(my_list))
        elif option == '2':
            print("The maximum value is:", getMax(my_list))
        elif option == '3':
            print("The mean value is:", getMean(my_list))
        elif option == '4':
            print("The median value is:", getMedian(my_list))
        elif option == '5':
            print("Clearing current list...")
            my_list = getList()
        else:
            print("Please try again/")



if __name__ == "__main__":
    main()


mylist = [17,64,16,71,13,92,97,98,31,60,83,2,84,68,62,22,24,76,95,55,6,59,10,29,35,85,26,4,1,53,12,61,20,77,89,5,94,74,25,81,70,82,73,18,15,46,69,3,87,66,23,80,42,21,7,65,9,0,36,96,52,79,32,39,1,33,40,50,14,48,45,51,27,34,30,100,88,9,63,86,19,78,54,47,57,49,67,91,56,44,58,72,43,38,11,37,75,4,28,99,8,93]
print("Standard Deviation:", getStdDev(mylist))