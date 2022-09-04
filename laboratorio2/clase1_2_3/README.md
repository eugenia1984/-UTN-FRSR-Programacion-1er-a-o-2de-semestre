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

```Python
```

```Python
```

```Python
```

```Python
```

```Python
```

```Python
```
---
---

# :star: Sets

---
---

# :star: Dictionaries

---
---
