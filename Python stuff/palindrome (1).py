
#palindrion e hint go to strings 1,, they behave like lists. that means you can do for loops, for loop over sa string? each character 1 by 1. 
#second thing -- when you add 2 strings together, if str 1 + str 2 -- hello world versus world hello
#google 2 pointer ont pointer at the start other at the end.twosome  reverse the sring if theyre the same thing reverse also another way
# if arr[left] = arr[right]
#look up how .join works
check = True
bird = input("Please enter your word. ").strip().lower()
bird =  bird.split()
bird = "".join(bird)
left = 0
right = len(bird) - 1
while left < right and check == True:
    if bird[left] == bird[right]:
        left = left + 1
        right = right - 1
    else:
        check = False
if check == True:
    print("this is a palindrome!")