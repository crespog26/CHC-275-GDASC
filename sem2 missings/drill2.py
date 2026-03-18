



try:
    def makeList():
        nums = []
        going = True

        while going:
            quack = input("Enter a number or 'stop' to finish:" )
            if quack == "stop":
                going = False
            else:
                num = int(quack)
                nums.append(num)
        return nums
    list1 = makeList()
    print("First list:", list1)
    list2 = makeList()
    print("First list:", list2)
except Exception as e:
    print("An error occurred:", e)