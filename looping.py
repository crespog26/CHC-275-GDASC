"""

repitition is the last thing, which we will cover today!
we are interested in repeating code blocks over and over again
consider some task you think should be repeated many times

print(1) repeated 20 times or soemthing is how we would print studf repeatedlty
it just feels wrong??!!!!

is there a way to do this task wihtout writing 100 print statements?

yes there is.

there are 3 ways to repeat a code segment
    - While loops
    - For loops 
    - Recursion 

while (exit condition):
    (repeated block)

exit conditions are conditional statements. so they have to ecaluate to either true or false

routine for a while loop
1) checks exit condition
2) if exit cond is not met then run the code block underneath
3) back to step one
"""

x=1
while x <= 10:
    print(x)
    #we want x to hit the exit conditioin at some point, natural option is to keep adding one to x,, second way is a more silly way 
    #x = x + 1
    x += 1
    

nums = [1,2,3,4,5,6,7,8,9,10]
x = 0
sum = 0
while x < len(nums):
    sum += nums[x]
    x += 1
    
print(f"the sum is {sum}")
    


"""

when soemthing runs forever, the program will eventually halt and throw an error called a "stack overflow"
what is it? 

your computer has a component called the Random Access Memory (ram!!) and it is responsible for holding information coressponding to processes that are running currently
when a python program is ran, what the python interpreter will do is allocate parittions of RAM to 2 different collections

    - Stack
    - Heap

stack is a fixed amount of memory for thigns liek function calls and basic memory assignment. there is a limited amount.
    finite amount of budget
heap is a dynamically amount of memory for things like complex datat structures. you have changing amount of memory budget for your program. 
    blank check of memory

when we ran this code bloc, you should egt a stack overflow eventually

"""

"""

looping statments are useufl for rep4eating a ton of math over and over again. How esle are they ruseful?
f4rom a program desgin standpoint, they also allow us to repeat an entire program until we quit.

There's a boolean data type, we can set variables equal to true or false

"""

check = False
while check == False:
    print("Option one")
    print("Option two")
    print("Option three")
    option = input("Select your option or quit to exit: ")
    if option == "1":
        print("1")
    elif option == "2":
        print("2")
    elif option == "3":
        print("3")
    elif option == "quit":
        check = True