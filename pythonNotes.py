#PRINT() FUNCTION 
#in python to display a message to the console/cmd we use the print() functio. In python 2 print used to be an argument but in python 3 print is a function

print('this is the first print')

#While writing code in python we need to be really carefull with the formatting. In python instaed of {} we use indentations to seperate the code into block like how we use {} to give the instructions on what to do if the 'if' condition is met

#VARIABLES
#We all know what variables are, why i think that, this section need to to written is because how we define variables in python is very weird and new to me.Python like javascript is a dynamically typed language, but when injavascript we need to write 'let' keyword before declaring a vraible literal in python we don't even do that much we just write the name of the varible. This is how we declare a variable in python

#n

# thats it. The rules to name a variable are the same as all the other programming language. we can give 'n' a value as well with assignment operator


#INPUT() FUNCTION
#input function does  what the prompt() does in javascript. It prints the text we give it and takes our input this is how we use input() to give value to a variable

#n=input("what is the value of n ")

#if we now use the print() to print n in the cmd it will first show the prompt we gave n and then display the value we gave to n

#print(n)

#we can also directly put the input() in the print(). In this method the print() method first evaluates the value returned by input() function and then prints the value entered by the user

#print(input("what is your name? "))

# =======================================================
#primitive variables in python 
'''
1)integer
2)floating point number
3)string
4)boolean
5)none
'''
#OPERATORS IN PYTHON 
'''
1) Aritmetic 
    +,-,*,/,%

2)Assignment
    =,+=,-=

    this is the first time i have seen += and -= operators. These are types of assignmet opertors with these you can assign calculated value to a variable. Here is how they work
a=5
a+=9 
    In the above code we assign the value 5 to 'a' then in the second line when we type +=9 what this will do is it will add 9 to the current value of 'a' and then assigns the new value to 'a' 

a-=3
    Similarly the above line first subtracts 3 from the current value of 'a' and then assigns the new value 

3)Comparision 
    ==,>,<,<=,>=!=
    
4)Logical
    and, or , not
'''

# =======================================================
#IF ELSE AND ELIF
'''
Just like every other programming language there exist if,else statement in python, the only thing different is instead of defining  the logic within a pair of {} we use indentations. 

One thing that i have seen is most python programs use 'elif' keyword its just a shorthand for  'else if' even if you write if for defining another condition it still works there was no erroer

#THE :
The : is very important it is used for various purposes but mostly it is used to indicate that there is a start of the coding block.

#THE SYNTAX
the syntax is as follow

if(condition):
    if_statements
elif(condition):
    elif_statements
else:
    else_statements


'''

'''
================================  MODULES  =============================
Modules are independent python programs. They are separate python files which can be imported within another python program. Modules are used when writing the code within a single file becomes inefficient as the volume is too large. We seperate the code with in multiple files and then export the functionalities defined in each file to where it is necessary. We do this in react all the time, but it can also be used to import python libraries and programs whichare available to us online to use in our code. 

One of the common example is Random module. It is used to produce random numbers with a given range. Its like the random() function in jaascript.

to import random we need to write the following line of code on the very top of the file

    import random

    random_int=random.randint(1,10)
    print(random_int)

The above written line of code will print a random integer from 1 to 10 

    random_float=random.random()
This line of code will give a random floating point number between 0.0 to 0.999999

'''
'''
==============================  LISTS  =============================
Arrays in python are called list. In terms of how they work they are similar to array objects in javascript. They are used to hold a collection of data and just like in javascript they can hold data of different kinds. This is how you define a list

    listName=[item1,item2,item3]

Index of a list starts with 0 (obviously). There exist predefined functions in python to list manipulation just like in js. Some of them are

1)append():-append() function is like the push() method in js. It adds the item we pass as its parameter at the very last of the list

    syntax:- listName.append(item)

2)extend():- extend() method is very intresting as it allows us to add multiple item to the end of the list. Its sort of like concat but here its not taking two arrays and returning a new one but instead adding the items of one array at the end of another

    syntax:- listName.extend([item1,item2])

3)insert():- insert() method takes two parameters ,first is the index of the position where we would like to insert a new item , second is the item that needs to be inserted

    syntax:-listName.extend(2,item)

4)remove():- remove() method takes a value as a parameter, it removes the first item fromthe list whose value is the same as the parameter

    syntax:- listName.remove(x)

5)pop():- just like in js pop() method removes the last element from the list. In python the 
pop() can also be used to remove any element by passing the index of that elementas a parameter. It returns the element that has been removed

    syntax:-listName.pop()  this removes the last lelement
    syntax:-listName.pop([2]) this removes the element at the index 2

6)clear():- clear() method removes all the items froma list

======================================= SPLIT() =================================
split() method is very unique, it is a string method we can use to create lists. We pass a character as a parameter to it , the spilt finction takes the charater and divides the string into peices upto that character and creates a new list

string1="hello,my,name,is,ubaid"
list1=string1.split(",")
print(list1)

output>> ["hello","my","name","is","ubaid"]

======================================= LOOPS =================================
We know what loops are, the concept is the same for pyhton the thing problematic is the syntax.
Lets start with something easier to understand.

    1)forIn loop
        The for-In loop is the for-Of loop in javascript. We can use for-In loop to iterate over an array. Here is an example

            fruitArray=['apple','orange','banana']
            for(fru in fruitArray):
                print(fru)

        Now how do we use for-In when we within a specific range. The following is an example.

            for n in range(0,10):
                print(n)

        The above code will give the initial value of 0 to n and will print it 10 times while incrementing it by 1 after each iteration

        How the for loop works in python is very different from it works in C. unlike other programming languages, the for loop does not iterate over a set of instructions with a specified halting conditions, it iterates over an iterable object like list or string
    
THE RANGE FUNCTION
    The range function is very helpful, it returns an object that behaves like a list. It is not a list but behaves like a list, it is an object which returns a succesive items of the desired sequence

    It can take three parameters first is the initial value second is the non-inclusive end point of the list and the third is the how much does the initial value increase by after each loop. Out of these the only compulsary one is the non-inclusive end point.

        for n in range(10):
            print(n)

    This will print the sequence from 0 to 9. It seems like the the defualt increment value is 1 and the default initial value is 0

    Now if we put an initial value this is what the code looks like 

        for n in range(2,5)
            print(n)

    This will print the sequence from 2-4 

    Now mentioning an increment rate the unction looks as follow

        for n in range(2,20,2)

    this print the sequence 
        2 4 6 8 10 12 14 16 18 20

    you can print in reverse from higher to lower value but then it is mandatory to put the negative decrement value,if you don't your for loop will just be ignored  

======================================= MATCH =================================
The match statement is the switch statement of python. 
    syntax:-
        match (cond):
            case 1:
                output 1
            case 2:
                output 2
            case 3:
                output 3 
            case _:
                default
            
======================================= FUNCTION =================================
The syntax to defining a fuction is as follow

    def function_name(parameter):
        function body


'''
'''
======================================= DICTIONARIES =================================
Dictionaries in python are a collection of key value which are used to store iterable data. They look similar to an object literal from JS. Each element in a dictionary is identified by its key. They are mutable collection of key value pairs and unlike arrays they are not ordered thus they are indexed by keys.

    dictA={
        key1:value1,
        key2:value2
    }

The string 'dict' is a keyword which represents the dictionary class in python.

to initialize a dictionary we can either use the syntax usedabove or use dict class
    
    dictA=dict(name='ubaid',age:23)

        or

    dictA=dict([(name,"ubaid"),(age,23)])

to access dictionary values we make use of the keys

    print(dictA[name])

we can also use .get() method as it can return a default value if the value we are looking for does not exist

    print(dictA.get(name,"not found"))

to modify a dictionary

1)to add new value 

    dictA[newKey]=newValue
    dictA["cgpa"]=8.2

2)to update an existing value

        dictA["age"]=24

there also exists the update method

    dictA({"newkey":"newalue","oldkey":"updatedValue"})

to remove an item from the dictionary 

1)del keyword

        del dictA["name"]

2).pop() method: it returns the value associated with the removed key

    dictA.pop("age")

3).clear() method: it removes all the items from the dictionary

    dictA.clear()

some commonly used dictionary methods

1)keys():returns a view object containing all the keys

2)values():returns a view object conataining all the values

3)items():returns a view object containing key-value pairs as tuples

5)copy():return a shallow copy of dictionary

loops with dictionary

for key in dictA:
    print(key)

this will always iterate over keys of the dictionary
'''

'''
==========================================
INDEX
1)print,input,vraible--------line 1
2)types of variables and operators in python I-----------------line 30
3)if, else,elif-----------------line 62 
4)modules, random module--------------line 85
5)lists and list methods I--------------line 104
6)split() making lists from strings------135
7)loops,range()----------------144
8)match statement-----------------191
9)Dictionaries-----------------212


'''