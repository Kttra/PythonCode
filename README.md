# PythonCode
Python code reference. An overview of Python. 

## Strings & Printing
In Python, a string is a sequence of characters. Strings are enclosed in either single quotes ('...') or double quotes ("..."). To print a string in Python, you can use the print() function. For example, print("Hello, World!") will output Hello, World! to the console. Below are some examples of using strings and printing.

```python
print("Hello World")
phrase = "Hello"
phrase[0] #H
phrase.index("e") #2
phrase.isupper() #false
print(phrase + " world") #hello world 
len(phrase)	#5
phrase.lower() #hello
phrase.upper() #HELLO
phrase.replace("hello", "test") #replaces 'hello' with 'test'
print(str(5) + " is my favorite number") #5 is my favorite number
```

## Variables & Data Types
A variable is a name that refers to a value. Variables are created when they are first assigned a value. Python has several built-in data types, including numbers, strings, lists, tuples, and dictionaries. Unlike other programming languages, you do not need to declare the data type for the variable.

```python
character_name = “John”
character_age = 35
print(“A man named” + character_name + “,”)
print(“He was” + character_age)
```

## Input
The below code prompts the user to enter their name, then it reads the input, and prints a greeting with their name.

```python
name = input("Enter your name: ")
print("Hello " + name + "!")
```

## List
List are used to used to store collections of data. List items are ordered, changeable, and allow duplicate values. Lists are created using square brackets.

```python
friends = [“Kevin”, 2, False]
friends = [“Kevin”, “Karen”, “Jim”]
print(friends);
print(friends[-1]) #Jim
print(friends[1:]) #[‘Karen’, ‘ Jim’]
friends = [“Kevin”, “Karen”, “Jim”, “Oscar”, “Toby”]
print(friends[1:3]) #[‘Karen’, ‘ Jim’]

friends = [“Kevin”, “Karen”, “Jim”, “Oscar”, “Toby”]
lucky_numbers = [4,8,15,16,23,42]
friends.extend(lucky_numbers) #Combines them
friends.extend(Creed) #Appends Creed
friends.insert(1, “Kelly”) #would add Kelly before Karen
friends.remove(“Jim”) #Removes Jim
friends.clear() #Clears list []
friends.pop() #Removes the last element from the list
friends.index(“Kevin”) #Tells the index of Kevin
friends.index(‘Mike”) #Error, mike not in the list
friends.count(“Jim”) #Says how many times Jim appears in the list
friends.sort() #Sorts the list in Accending order
friends2 = friends.copy #copies friends without ref
```

## Tuples
Tuples are another built-in data type in Python used to store collections of data. Tuples are immutable, meaning that once they are created, their contents cannot be changed. Tuple items are ordered, unchangeable, and allow duplicate values.

```python
coordinates = (4, 5)
coordinates[1] = 10 #error, tuples are inmutable
print(coordinates[1]) #5
coordinates = [(4, 5), (6, 7), (80, 34)] #List of Tuples
```

## Functions/Def
A function/def is a block of code that performs a specific task. It is defined using the def keyword followed by the function name and parentheses. Input parameters can be placed within these parentheses. 

```python
def say_hi(name, age):
	 print(“Hello “ + name + “, you are” + age )

say_hi(“Mike”, “35”)
```
It is possible to return a value in a function. When a return statement is executed, the function is terminated immediately and the value specified in the return statement is returned to the caller.

```python
def cube(num):
	return num*num*num
cube(4) #64
```

## If Statements
If statements are used to execute a block of code based on a specified condition. An if statement contains a boolean condition where the condition returns a Boolean value (True or False). If the condition is True, then the code inside the if statement is executed. If the condition is False, then the code inside the if statement is skipped.

```python
is_male = True
is_tall = False
if is_male or is_tall:
	print("You are  a male or tall or both")
elif is_male and not(is_tall):
	print("You are a short male")
elif not(is_male) and is_tall:
	print("You are not a male but you are tall")
else:
	print("You are not a male")
#You are  a male or tall or both is the result
```

## Dictionaries
A dictionary is a collection of key-value pairs. Each key is associated with a value, and you can use the key to access the corresponding value. Dictionaries are similar to lists, but instead of using an index to access an element, you use a key.

```python
monthConversions = {
	"Jan" : "January", # left side doesn’t need to be a spring
	"Feb" : "February",
	"Mar" : "March",
	"Apr" : "April",
	"May" : "May",
	"Jun" : "June",
	"Jul" : "July",
	"Aug" : "August",
	"Sep" : "September",
	"Oct" : "October",
	"Nov" : "November",
	"Dec" : "December",
}
print(monthConversions["Mar"])
print(monthConversions.get("Mar"))
print(monthConversions.get("Lov", "Not a valid key")) #Returns Not a valid key since Lov is not present
```
