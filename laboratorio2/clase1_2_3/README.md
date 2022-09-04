# :book: Colections

- **List** is a collection which is ordered and changeable. Allows duplicate members.

- **Tuple** is a collection which is ordered and unchangeable. Allows duplicate members.

- **Set** is a collection which is unordered, unchangeable(1), and unindexed. No duplicate members.

- **Dictionary** is a collection which is ordered(2) and changeable. No duplicate members.

(1)Set items are unchangeable, but you can remove and/or add items whenever you like.

(2)As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

---
---

# :star2: List :star2:

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets.


- Create a list:
```Python
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

---

## 📋 Definition

->>> List Items are **ordered**, **changeable**, and **allow duplicate values**. 

1. **ORDERER**:

List items are indexed, the first item has index [0], the second item has index [1] etc.

When we say that lists are ordered, it means that the items have a defined order, and that order will not change. If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.

2. **CHANGEABLE**:

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

3. **ALLOW DUPLICATAES VALUES**:


```Python
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
```

---

->>> List Length: To determine how many items a list has, use the len() function:

```Python
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```

---

->>> List Items - Data Types: can be of any data type.

```Python
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
```

A list with strings, integers and boolean values: 
```Python
list1 = ["abc", 34, True, 40, "male"]
```

---

## 📋 Type

->>> type(): from Python's perspective, lists are defined as objects with the data type 'list':

```Python
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # <class 'list'>
```

---

## 📋 Constructor

->>> The list() Constructor: it is also possible to use the list() constructor when creating a new list.

```Python
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
```

---

## 📋 Access Items

->>> Access Items: List items are indexed and you can access them by referring to the index number:

```Python
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # print the second item
```

- Note: The first item has index 0.

- Negative Indexing, means start from the end : -1 refers to the last item, -2 refers to the second last item etc.

```Python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```

---

## 📋 Range of Indexes

->>> Range of Indexes : you can specify a range of indexes by specifying where to start and where to end the range. When specifying a range, the return value will be a new list with the specified items.

```Python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # Return the third, fourth, and fifth item
```

- Note: The search will start at index 2 (included) and end at index 5 (not included).

- Remember that the first item has index 0.

- By leaving out the start value, the range will start at the first item

- By leaving out the end value, the range will go on to the end of the list

- Range of Negative Indexes: Specify negative indexes if you want to start the search from the end of the list:

```Python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # This example returns the items from "orange" (-4) to, but NOT including "mango" (-1)
```

---

## 📋 Check if Item Exists

->>> Check if Item Exists: To determine if a specified item is present in a list use the in keyword

Check if "apple" is present in the list:

```Python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

---

## 📋 Change Item Value

->>> Change Item Value: To change the value of a specific item, refer to the index number:

```Python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # change the second item
print(thislist)
```

->>> Change a Range of Item Values : To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

```Python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] # Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
print(thislist)
```

->>> If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly

```Python
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] # Change the second value by replacing it with two new values
print(thislist)
```

- Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

->>> If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly

```Python
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] # Change the second and third value by replacing it with one value:
print(thislist)
```

---

## 📋 Insert Items

To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

```Python
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # Insert "watermelon" as the third item
print(thislist)
```

- Note: As a result of the example above, the list will now contain 4 items.

---

## 📋 Add List Items

### Append Items

To add an item to the end of the list, use the **append()** method:

```Python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
```

### Insert Items

To insert a list item at a specified index, use the **insert()** method.

The insert() method inserts an item at the specified index:

```Python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") # Insert an item as the second position
```

-Note: As a result of the examples above, the lists will now contain 4 items.

### Extend List

To append elements from another list to the current list, use the **extend()** method.

```Python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # Add the elements of tropical to thislist
```

## Add Any Iterable

The **extend()** method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

```Python
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']
```

---

## 📋 Remove List Items

### Remove Specified Item

The **remove()** method removes the specified item.

```Python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # Remove "banana"
print(thislist)
```

### Remove Specified Index

The **pop()** method removes the specified index.

```Python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # remove the second item
print(thislist)
```

- If you do not specify the index, the pop() method removes the last item.

```Python
thislist = ["apple", "banana", "cherry"]
thislist.pop()
```

## del

The **del** keyword also removes the specified index

```Python
thislist = ["apple", "banana", "cherry"] # remove the first item
del thislist[0]
```

- The del keyword can also delete the list completely.
```Python
thislist = ["apple", "banana", "cherry"]
del thislist  # delete the entire list
```

## Clear the List

The **clear()** method empties the list. The list still remains, but it has no content.

```Python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
```

---

## 📋 Loop Lists

- You can loop through the list items by using a for loop:

```Python
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
```

## Loop Through the Index Numbers

You can also loop through the list items by referring to their index number. Use the range() and len() functions to create a suitable iterable

```Python
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):  # Print all items by referring to their index number
  print(thislist[i])
# [0, 1, 2] 
```

### Using a While Loop

You can loop through the list items by using a **while** loop.

Use the **len()** function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.

```Python
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
```

### Looping Using List Comprehension

List Comprehension offers the shortest syntax for looping through lists:

```Python
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
```

---

## 📋 List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

```Python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```

With list comprehension you can do all that with only one line of code:

```Python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
```

->> Syntax: ```newlist = [expression for item in iterable if condition == True]```

The return value is a new list, leaving the old list unchanged.

->>> Condition : the condition is like a filter that only accepts the items that valuate to True.

```Python
newlist = [x for x in fruits if x != "apple"] # only accept items that are not apple
```

The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

The condition is optional and can be omitted.

With no if statement ```newlist = [x for x in fruits]```

---

## 📋 Iterable

The iterable can be any iterable object, like a list, tuple, set etc.

```Python
newlist = [x for x in range(10)] # You can use the range() function to create an iterable
```

```Python
newlist = [x for x in range(10) if x < 5] # with a condition. Accept only numbers lower than 5
```

Expression:

The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
```Python
newlist = [x.upper() for x in fruits] # Set the values in the new list to upper case

newlist = ['hello' for x in fruits] # Set all values in the new list to 'hello'
```

The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

```Python
newlist = [x if x != "banana" else "orange" for x in fruits] # Return "orange" instead of "banana"
```

The expression in the example above says: "Return the item if it is not banana, if it is banana return orange".

---

## 📋 Sort List Alphanumerically

- List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

```Python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] # Sort the list alphabetically
thislist.sort()
```

```Python
thislist = [100, 50, 65, 82, 23] # Sort the list numerically
thislist.sort()
```

- To sort descending, use the keyword argument reverse = True

```Python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
```

```Python
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
```

- Customize Sort Function: You can also customize your own function by using the keyword argument key = function. The function will return a number that will be used to sort the list (the lowest number first):

Sort the list based on how close the number is to 50
```Python
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # [50, 65, 23, 82, 100]
```

- Case Insensitive Sort: by default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

```Python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # ['Kiwi', 'Orange', 'banana', 'cherry']
```

Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

```Python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']
```

- Reverse Order: What if you want to reverse the order of a list, regardless of the alphabet? The **reverse()** method reverses the current sorting order of the elements.

```Python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() # ['cherry', 'Kiwi', 'Orange', 'banana']
print(thislist) 
```

---

## 📋 Copy Lists


- You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy()


```Python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # ["apple", "banana", "cherry"]
```


- Another way to make a copy is to use the built-in method **list()**.

```Python
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) # ["apple", "banana", "cherry"]
```

---

## 📋 Join Lists

Here are several ways to join, or concatenate, two or more lists in Python.

- One of the easiest ways are by using the + operator.
```Python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3]
```

- Another way to join two lists is by appending all the items from list2 into list1, one by one:
```Python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) # ['a', 'b', 'c', 1, 2, 3]
```

- Or you can use the **extend()** method, which purpose is to add elements from one list to another list:

```Python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) # ['a', 'b', 'c', 1, 2, 3]
```

---

## 📋 List Methods

| Method | Description 
| -- | -- |
| append() | Adds an element at the end of the list |
| clear() | Removes all the elements from the list |
| copy() | Returns a copy of the list |
| count() | Returns the number of elements with the specified value |
| extend() | Add the elements of a list (or any iterable), to the end of the current list |
| index() | Returns the index of the first element with the specified value |
| insert () | Adds an element at the specified position |
| pop() | Removes the element at the specified position |
| remove() | 	Removes the item with the specified value |
| reverse() | Reverses the order of the list |
| sort() | Sorts the list |

---
---

# :star2: Tuples :star2:

##  ▶️ Definition

- Tuples are used to store multiple items in a single variable.

- Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

- A tuple is a collection which is ordered and unchangeable.

- Tuples are written with round brackets ``` ( )```.

```Python
thistuple = ("apple", "banana", "cherry")
print(thistuple) # ('apple', 'banana', 'cherry')
```

##  ▶️ Characteristics:

### Tuple Items

- Tuple items are **ordered**, **unchangeable**, and **allow duplicate values**.

-Tuple items are indexed, the first item has index ```[0]```, the second item has index ```[1]``` etc.

### Ordered

- When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

### Unchangeable

- Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

### Allow Duplicates

- Since tuples are indexed, they can have items with the same value:

```Python
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) # ('apple', 'banana', 'cherry', 'apple', 'cherry')
```
---

##  ▶️ Tuple Length

- To determine how many items a tuple has, use the **len()** function:

```Python
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple)) # 3
```
---

##  ▶️ Create Tuple With One Item

- To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

Example : One item tuple, remember the comma:

```Python
thistuple = ("apple",)
print(type(thistuple)) # <class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) # <class 'str'>

```

---

##  ▶️ Tuple Items - Data Types

- Tuple items can be of any data type:

Example: **String**, **int** and **boolean** data types:


```Python
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1) # ('apple', 'banana', 'cherry')
print(tuple2) # (1, 5, 7, 9, 3)
print(tuple3) # (True, False, False)
```

- A tuple can contain **different data types**:

Example: A tuple with strings, integers and boolean values:

```Python
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1) # ('abc', 34, True, 40, 'male')
```
---

##  ▶️ type()

- From Python's perspective, tuples are defined as objects with the data type 'tuple': ```<class 'tuple'>```

```Python
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # <class 'tuple'>
```

Example: What is the data type of a tuple?

```Python
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # <class 'tuple'>
```

---

##  ▶️ The tuple() Constructor

- It is also possible to use the tuple() constructor to make a tuple.

- Example: Using the ```tuple()``` method to make a tuple:

```Python
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple) # ('apple', 'banana', 'cherry')
```

---

## ▶️  Python - Access Tuple Items

### Access Tuple Items

- You can access tuple items by referring to the index number, inside square brackets:

```Python
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # banana
```

## Negative Indexing
Negative indexing means start from the end.

```-1``` refers to the last item

```-2``` refers to the second last item etc.

```Python
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # cherry
```

## Range of Indexes

- You can specify a range of indexes by specifying where to start and where to end the range.

- When specifying a range, the return value will be a new tuple with the specified items.

```Python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # ('cherry', 'orange', 'kiwi')

#This will return the items from position 2 to 5
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
```

- By leaving out the start value, the range will start at the first item:

```Python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) # ('apple', 'banana', 'cherry', 'orange')
```

- By leaving out the end value, the range will go on to the end of the list:

```Python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) # ('cherry', 'orange', 'kiwi', 'melon', 'mango')
```
## Range of Negative Indexes

- Specify negative indexes if you want to start the search from the end of the tuple:

- Example: This example returns the items from index -4 (included) to index -1 (excluded)

```Python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # ('orange', 'kiwi', 'melon')

#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
```
## Check if Item Exists

- To determine if a specified item is present in a tuple use the in keyword:

```Python
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
# Yes, 'apple' is in the fruits tuple  
```

---

## ▶️  Update Tuples

- Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

- But there are some workarounds

### Change Tuple Values

- Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

- But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

```Python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) # ("apple", "kiwi", "cherry")
```

### Add Items

- Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

1. **Convert into a list**: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

- Example: Convert the tuple into a list, **add// "orange", and **convert** it back into a tuple:

```Python
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple) # ('apple', 'banana', 'cherry', 'orange')
```

2. **Add tuple to a tuple** : You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

- Example: Create a new tuple with the value "orange", and add that tuple:

```Python
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) # ('apple', 'banana', 'cherry', 'orange')
```

- Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

### Remove Items

Note: You cannot remove items in a tuple.

- Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

- Example: Convert the tuple into a list, remove "apple", and convert it back into a tuple:

```Python
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple) # ('banana', 'cherry')
```

- Or you can delete the tuple completely:

Example: The del keyword can delete the tuple completely:

```Python
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exist
```
"""
Traceback (most recent call last):
  File "demo_tuple_del.py", line 3, in <module>
    print(thistuple) #this will raise an error because the tuple no longer exists
NameError: name 'thistuple' is not defined
"""
  
---

## ▶️ Unpack Tuples
  
###   Unpacking a Tuple

- When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

- Example: Packing a tuple:

```Python
fruits = ("apple", "banana", "cherry") # ('apple', 'banana', 'cherry')
```

 - But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

Example: Unpacking a tuple:

```Python
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green) # apple
print(yellow) # banana
print(red)   # cherry
```

- Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

### Using Asterisk ```*```
  
- If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

- Example: Assign the rest of the values as a list called "red":  

```Python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) # apple
print(yellow) # banana
print(red)   # ['cherry', 'strawberry', 'raspberry']
```

- If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

Example: Add a list of values the "tropic" variable:  

```Python
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green) # apple
print(tropic) # ['mango', 'papaya', 'pineapple']
print(red)  # cherry
```
  
---

## ▶️  Loop Tuples
  
###  Loop Through a Tuple

- You can loop through the tuple items by using a for loop.

- Example: Iterate through the items and print the values: 

```Python
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
# apple
# banana
# cherry  
```

### Loop Through the Index Numbers

- You can also loop through the tuple items by referring to their index number.

- Use the ```range()``` and  ```len()``` functions to create a suitable iterable.

Example: Print all items by referring to their index number:

```Python
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
# apple
# banana
# cherry  
```  

### Using a While Loop
  
- You can loop through the list items by using a while loop.

- Use the ```len()``` function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.

- Remember to increase the index by 1 after each iteration.

- Example: Print all items, using a while loop to go through all the index numbers:  
  
```Python
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
# apple
# banana
# cherry                         
``` 
                         
---

## ▶️ Join Tuples
                         
### To join two or more tuples you can use the + operator:

- Example: Join two tuples:
                         
```Python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) #   ('a', 'b', 'c', 1, 2, 3)                      
```  

### Multiply Tuples
                         
- If you want to multiply the content of a tuple a given number of times, you can use the * operator:

- Example: Multiply the fruits tuple by 2:

```Python
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```
                         
---

## ▶️   Tuple Methods    
                         
Python has two built-in methods that you can use on tuples.
                         
| Method | Description |
| ------ | ----------- | 
| count() | 	Returns the number of times a specified value occurs in a tuple |
|  index() | Searches the tuple for a specified value and returns the position of where it was found |                        

  
---
---

# :star2: Sets :star2:

## :basecamp:  Definition
                         
- Sets are used to store multiple items in a single variable.

- Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

- A set is a collection which is unordered, unchangeable*, and unindexed.                         

*Note: Set items are unchangeable, but you can remove items and add new items.*    

- Sets are written with curly brackets.

Example: Create a Set:   
                         
```Python
thisset = {"apple", "banana", "cherry"}
print(thisset) #   {'banana', 'cherry', 'apple'}                       
```  
                         
*Note: Sets are unordered, so you cannot be sure in which order the items will appear.*
                         
---
                         
## :basecamp: Set Items
                         
- Set items are unordered, unchangeable, and do not allow duplicate values.

### Unordered
                         
- Unordered means that the items in a set do not have a defined order.

- Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

### Unchangeable
                         
- Set items are unchangeable, meaning that we cannot change the items after the set has been created.

*Once a set is created, you cannot change its items, but you can remove items and add new items*.                   
                         
### Duplicates Not Allowed

- Sets cannot have two items with the same value.

- Example: Duplicate values will be ignored: 
                         
```Python
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)   #    {'banana', 'cherry', 'apple'}                   
```                          

---
                         
## :basecamp: Get the Length of a Set

### To determine how many items a set has, use the len() function.

Example: Get the number of items in a set:

```Python
thisset = {"apple", "banana", "cherry"}
print(len(thisset))  # 3                       
``` 

###   Set Items - Data Type
                         
- Set items can be of any data type:

- Example: String, int and boolean data types: 
                         
```Python
set1 = {"apple", "banana", "cherry"} 
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} 
print(set1) #  {"apple", "banana", "cherry"} 
print(set2) # {1, 5, 7, 9, 3}
print(set3)   # {True, False, False}                        
```

- A set can contain different data types:

Example: A set with strings, integers and boolean values:     

```Python
set1 = {"abc", 34, True, 40, "male"} #   {True, 34, 40, 'male', 'abc'}
print(set1)                         
```

## type()
                         
- From Python's perspective, sets are defined as objects with the data type 'set':  ```<class 'set'>```                        
- Example: What is the data type of a set?

```Python
myset = {"apple", "banana", "cherry"}
print(type(myset)) # <class 'set'>
```   

## The set() Constructor
  
It is also possible to use the set() constructor to make a set.

Example: Using the set() constructor to make a set:  

```Python
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)  # {'banana', 'cherry', 'apple'}
# Note: the set list is unordered, so the result will display the items in a random order.  
```
  
---
                         
## :basecamp: Access Set Items

- You cannot access items in a set by referring to an ```index``` or a key.

- But you can loop through the set items using a ```for``` loop, or ask if a specified value is present in a set, by using the ```in``` keyword.

- Example: Loop through the set, and print the values:  
```Python
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# banana
# apple
# cherry  
```
  
- Example: Check if "banana" is present in the set:  
```Python
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # True
```

### Change Items
  
Once a set is created, you cannot change its items, but you can add new items.  
  
--- 

## :basecamp: Add Set Items

*Once a set is created, you cannot change its items, but you can add new items*.
  
- To add one item to a set use the ```add()``` method.

- Example: Add an item to a set, using the ```add()``` method:  

```Python
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)  # {'orange', 'banana', 'cherry', 'apple'}
```

### Add Sets
  
- To add items from another set into the current set, use the update() method.

- Example: Add elements from tropical into thisset:  
```Python
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
  
print(thisset)  # {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}
``` 
  
### Add Any Iterable

- The object in the ```update()``` method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

- Example: Add elements of a list to at set:  

```Python
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) # {'banana', 'cherry', 'apple', 'orange', 'kiwi'}
```
  
---
  
## :basecamp: Remove Set Items

- To remove an item in a set, use the ```remove()```, or the ```discard()``` method.

Example: Remove "banana" by using the ```remove()``` method:
  
```Python
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) # {'cherry', 'apple'}
```  

*Note: If the item to remove does not exist, remove() will raise an error*.
 
- Example: Remove "banana" by using the ```discard()``` method:  
  
```Python
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) # {'apple', 'cherry'}
```  

*Note: If the item to remove does not exist, discard() will NOT raise an error*.

- You can also use the ```pop()``` method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

- The return value of the ```pop()``` method is the removed item.
  
- Example: Remove the last item by using the ```pop()``` method:  
  
```Python
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) # apple

print(thisset) #   {'banana', 'cherry'} 
```  

*Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed*.
  
- Example: The ```clear()``` method empties the set:  
  
```Python
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)  # set()
```  

- Example: The del keyword will delete the set completely:  
  
```Python
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)  
"""
Traceback (most recent call last):
  File "demo_set_del.py", line 5, in <module>
    print(thisset) #this will raise an error because the set no longer exists
NameError: name 'thisset' is not defined  
"""  
```     
  
---
  
## :basecamp: Loop Set Items

- You can loop through the set items by using a for loop:

- Example: Loop through the set, and print the values:  
```Python
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# banana
# cherry
# apple  
```
    
---
  
## :basecamp: Join Set Items  

### Join Two Sets
  
- There are several ways to join two or more sets in Python.

- You can use the ```union()``` method that returns a new set containing all items from both sets, or the ```update()``` method that inserts all the items from one set into another:  
  
- Example: The ```union()``` method returns a new set with all items from both sets:  
  
```Python
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)  # {2, 'b', 'c', 3, 'a', 1}
```

- Example: The ```update()``` method inserts the items in set2 into set1:  

```Python
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)   # {3, 'b', 2, 'a', 1, 'c'}
```
 
*Note: Both union() and update() will exclude any duplicate items*.  

### Keep ONLY the Duplicates

- The ```intersection_update()``` method will keep only the items that are present in both sets.

- Example: Keep the items that exist in both set x, and set y:

```Python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x) # {'apple'}
```

- The intersection() method will return a new set, that only contains the items that are present in both sets.

- Example: Return a set that contains the items that exist in both set x, and set y:

```Python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z) # {'apple'}
```

## Keep All, But NOT the Duplicates

- The ```symmetric_difference_update()``` method will keep only the elements that are NOT present in both sets.

- Example: Keep the items that are not present in both sets:

```Python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x) # {'google', 'banana', 'microsoft', 'cherry'}
```
- The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

- Example: Return a set that contains all items from both sets, except items that are present in both:

```Python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z) # {'google', 'banana', 'microsoft', 'cherry'}
```

---
  
## :basecamp: Set Methods

Python has a set of built-in methods that you can use on sets.

| Method | Description |
| ------ | ----------- |
| add() | Adds an element to the set |
| clear() | Removes all the elements from the set |
| copy() | Returns a copy of the set|
| difference() | Returns a set containing the difference between two or more sets |
| difference_update() | Removes the items in this set that are also included in another, specified set |
| discard() | Remove the specified item |
| intersection() | Returns a set, that is the intersection of two other sets |
| intersection_update() | Removes the items in this set that are not present in other, specified set(s) |
| isdisjoint() | Returns whether two sets have a intersection or not |
| issuperset() | Returns whether another set contains this set or not |
| pop() | Removes an element from the set |
| remove() | Removes the specified element |
| symmetric_difference() | Returns a set with the symmetric differences of two sets |
| symmetric_difference_update()	 | inserts the symmetric differences from this set and another |
| union() | Return a set containing the union of sets |
| update() | Update the set with the union of this set and others |
                         
---
---

# :star2: Dictionaries  :star2:

---

## :star: Definition

- Dictionaries are used to store data values in key:value pairs.

- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

- As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

- Dictionaries are written with curly brackets, and have keys and values:

- Example: Create and print a dictionary:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

### Dictionary Items

- Dictionary items are ordered, changeable, and does not allow duplicates.

- Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

- Example: Print the "brand" value of the dictionary:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"]) # Ford
```

### Ordered or Unordered?

- As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

- When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

- Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

### Changeable

- Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

### Duplicates Not Allowed

- Dictionaries cannot have two items with the same key:

Example: Duplicate values will overwrite existing values:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

### Dictionary Length

- To determine how many items a dictionary has, use the len() function:

- Example: Print the number of items in the dictionary:

```Python
print(len(thisdict)) # 3
```

### Dictionary Items - Data Types

- The values in dictionary items can be of any data type:

- Example: String, int, boolean, and list data types:

```Python
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
```

### type()

- From Python's perspective, dictionaries are defined as objects with the data type 'dict': ```<class 'dict'>```

Example: Print the data type of a dictionary:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
```


---

## :star: Access Items

### Accessing Items

- You can access the items of a dictionary by referring to its key name, inside square brackets:

- Example: Get the value of the "model" key:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] # Mustang
```

- There is also a method called ```get()``` that will give you the same result:

Example: Get the value of the "model" key:

```Python
x = thisdict.get("model") # Mustang
```

### Get Keys

- The ```keys()``` method will return a list of all the keys in the dictionary.

Example: Get a list of the keys:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x) # dict_keys(['brand', 'model', 'year'])
```

- The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

Example: Add a new item to the original dictionary, and see that the keys list gets updated as well:

```Python
ar = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change dict_keys(['brand', 'model', 'year', 'color'])
```

### Get Values

- The ```values()``` method will return a list of all the values in the dictionary.

Example: Get a list of the values:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x) # dict_values(['Ford', 'Mustang', 1964])
```

- The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

- Example: Make a change in the original dictionary, and see that the values list gets updated as well:

```Python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x) #after the change dict_values(['Ford', 'Mustang', 2020])
```

- Example: Add a new item to the original dictionary, and see that the values list gets updated as well:

```Python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change dict_values(['Ford', 'Mustang', 1964])

car["color"] = "red"
 
print(x) #after the change dict_values(['Ford', 'Mustang', 1964, 'red'])
```

### Get Items

- The ```items()``` method will return each item in a dictionary, as tuples in a list.

Example: Get a list of the key:value pairs

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
```

- The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

Example: Make a change in the original dictionary, and see that the items list gets updated as well:

```Python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["year"] = 2020

print(x) #after the change dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])
```


- Example: Add a new item to the original dictionary, and see that the items list gets updated as well:

```Python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["color"] = "red"

print(x) #after the change dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])
```

### Check if Key Exists

- To determine if a specified key is present in a dictionary use the in keyword:

- Example: Check if "model" is present in the dictionary:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Yes, 'model' is one of the keys in the thisdict dictionary  
```


---

## :star: Change Items

### Change Values

- You can change the value of a specific item by referring to its key name:

- Example: Change the "year" to 2018:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
```

### Update Dictionary

- The ```update()``` method will update the dictionary with the items from the given argument.

-The argument must be a dictionary, or an iterable object with key:value pairs.

- Example: Update the "year" of the car by using the ```update()``` method:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
```

---

## :star: Add Items

### Adding Items

- Adding an item to the dictionary is done by using a new index key and assigning a value to it:

- Example:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
```

### Update Dictionary

- The ```update()``` method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

- The argument must be a dictionary, or an iterable object with ```key:value pairs```.

- Example : Add a color item to the dictionary by using the ```update()``` method:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
```

---

## :star: Remove Items


### Removing Items

- There are several methods to remove items from a dictionary:

- Example: The ```pop()``` method removes the item with the specified key name:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
```

### Example

- The ```popitem()``` method removes the last inserted item (in versions before 3.7, a random item is removed instead):

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang'}
```

### Example

The ```del``` keyword removes the item with the specified key name:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) # {'brand': 'Ford', 'year': 1964}
```

- Example: The del keyword can also delete the dictionary completely:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
```

- Example: The ```clear()``` method empties the dictionary:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) # {}
```

---

## :star: Loop Dictionaries

### Loop Through a Dictionary

- You can loop through a dictionary by using a for loop.

- When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

- Example: Print all key names in the dictionary, one by one:
```Python
for x in thisdict:
  print(x)
# brand
# model
# year
```

- Example: Print all values in the dictionary, one by one:

```Python
for x in thisdict:
  print(thisdict[x])
"""
Ford
Mustang
1964
"""
```

- Example: You can also use the ```values()``` method to return values of a dictionary:

```Python
for x in thisdict.values():
  print(x)
```

- Example :You can use the ```keys()``` method to return the keys of a dictionary:

```Python
for x in thisdict.keys():
  print(x)
```

- Example: Loop through both keys and values, by using the ```items()``` method:

```Python
for x, y in thisdict.items():
  print(x, y)
```


---

## :star: Copy Dictionaries

- You cannot copy a dictionary simply by typing ``` dict2 = dict1```, because: ```dict2``` will only be a reference to ```dict1```, and changes made in ```dict```1 will automatically also be made in ```dict2```.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

- Example: Make a copy of a dictionary with the ```copy()``` method:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

- Another way to make a copy is to use the built-in function ```dict()```.

Example: Make a copy of a dictionary with the ```dict()``` function:

```Python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

---

## :star: Nested Dictionaries

- A dictionary can contain dictionaries, this is called nested dictionaries.

Example: Create a dictionary that contain three dictionaries:

```Python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
```

- Or, if you want to add three dictionaries into a new dictionary:

Example: Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

```Python
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
```



---

## :star: Disctionary Methods

| Method | Description |
| ------ | ----------- |
| clear() | Removes all the elements from the dictionary |
| copy() | Returns a copy of the dictionary |
| fromkeys() | Returns a dictionary with the specified keys and value |
| get() | Returns the value of the specified key |
| items() | Returns a list containing a tuple for each key value pair |
| keys() | Returns a list containing the dictionary's keys |
| pop() | Removes the element with the specified key |
| popitem() | Removes the last inserted key-value pair |
| setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| update() | Updates the dictionary with the specified key-value pairs |
| values() | Returns a list of all the values in the dictionary |


---
---
