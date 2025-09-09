"""
What is python?
    - python is a programming language
A set of syntax and protocols in your instructions in for your computer to follow

Python is a command line program
    -HWeen you download python off the internet, you're downloading what is actually called the phython interpreter
    
    -THe onterpreter's role on your computer
        -it looks at .py files, and line by line convert valid python syntax into machine code
        
    Python is an interpreted language
        - We just poin t the interpreter at a phython file and it
        ll run the code
        
    - Compiled languages
        -c. cc. java, c++,
        Call the compiler onm your code file, and itll get compiled into an exectuable file that you run
        
    The first thing that is opf importance to us are variables.
    
    Variables caryy three properties:
        - The name of the variable
        - Its data type
        - Its attribute <= the actual data itself
        
    A variable is just a named place on your computer's RAM that stores information
    
    
"""

x = 5
#^ This is a variable
#<name of your variable> = <attribute>

print(x)

"""
    Data Types
    
        - Numbers 
        - Strings of Text
        
    There are two datatypes for numbers
        - Integer: a whole number, including 0 and negative numbers
        - Float: floating point number, pi
        
"""

y=10
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**2)

"""
Sometuimes when we are manipulating numebrs. we want t oworkkl withn the results again later on.
All we did was print the results of our arithmetic.
The python interpreter is not actually that smart. it doesn't remember what it prints, So in order for python to remember what it did, you need to save it back intoa nother variable
"""

sum=x+y
print(sum)

"""
sum is a named place in memory
on the left side of the equal sign, we are declaring a variable,
on the right hand side, substitute the value of sum into where called it
"""
sum = sum + 20
print(sum)

"""
in other programming languages you have a data type specigically for single characters of text

"""

name = "garchomp"
print(name)

"""
what if i want to say "my name is"

    fstring: format string aand it lets speicfy placehodler values in strings so you cna drop in varioables
"""

print(f"garchomp garchomp {name}")
print(f"the sum of x and y is {sum}")