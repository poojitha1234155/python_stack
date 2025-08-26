# Accessing string elements- strings are indexed,starting from 0 for the first character.negative indices start from -1 for the last character

s="python"
print(s[0])   #  output : p
print(s[-1])  #  output : n

#slicing strings

s="python"
print(s[0:3])    #output :pyt (0 to 2)
print(s[:3])     #output :pyt (start o is default)
print(s[3:])     #output :hon (end is the length by default)
print(s[-3:])    #output :hon (last 3 characters)

#concantenation:Adding 2 strings

str1="hello"
str2="world"
result=str1+" "+str2
print(result)  #output : hello world

#Repetition : can multiply with an integer

str="Hi!"
print(str*3)    #output : Hi! Hi! Hi!

#strip()-Removes whitespace (or specified characters)from both ends of a string

text="Hello,world"
print(text.strip())    #output : "Hello,world"

#lower()-converts all characters in a string to lowercase()

text="Hello"
print(text.lower())    #output : "hello"

#upper()-converts all characters in a string to uppercase

text="Hello"
print(text.upper())     #output : "HELLO"

#find(substring)-Returns the index of the first occurrence of a substring:returns-1 if not found.

text="Hello,world"
print(text.find("world"))   #output : 7

#replace(old,new)-Replaces all occurences of a substring with another substring

text="i love india"
print(text.replace("india","food"))   #output : "i love food"

#slit(delimiter)-Splits a string into a list based on a delimiter

text="pooja,aishu,lalitha"
print(text.split(","))       #output : ['pooja','aishu','lalitha']

#",".join(iterable)-joins elements of an iterable (e.g.,list)into a single string, separated by the specified delimiter

items=["a","b","c","d"]
print(",".join(items))     #output : "a,b,c,d"

#startswith(prefix)-Return True if the string starts with the specified prefix;otherwise,false.

text="pooja"
print(text.startswith("po"))    #output : "True"

#endswith(suffex)-Returns True if the string ends with the specified suufix;otherwise,False

text="pooja"
print(text.endswith("ja"))      #output : "True"

#count(substring)-Counts occurrences of a substring in a string

text="Apple"
print(text.count("l"))   #output : 1

#List Methods :

#Accessing and slicing

numbers=[1,2,3,4,5]
print(numbers[1])    #output : 2
print(numbers[1:4])   #output : 2,3,4

#len()-returns the numbers of elements in a list

numbers=[1,2,3]
print(len(numbers))    #output : 3

#in-Checks if an element exists in the list

numbers=[1,2,3,4]
print(2 in numbers)  #output : true

#concantenation-combines two lists

list1=[1,2]
list2=[3,4]
print(list1+list2)    #output : [1,2,3,4]

#append(item)-Adds an item to the end of the list

fruits=[1,2]
fruits.append(3)
print(numbers)   #output : [1,2,3]

#extend(iterable)-Extends the list by appendings elements from another iterable

numbers=[1,2]
numbers.extend([3,4])
print(numbers)            #output : [1,2,3,4]


#insert(index,item)-inserts an item at a specified position

number=[1,3]
number.insert(1,2)
print(number)          #out put : [1,2,3]

#remove(element)-Removes the first occurrence of an element.

numbers=[1,2,3,4]
numbers.remove(2)  
print(numbers)        #output : [1,3,4]


#pop(index)-Removes and returns the element at the specified index.Default:last item

number=[1,2,3]
print(number.pop(1))   #output : 2
print(number)           #output: 2,3

#index(element)-Returns the index of the first occurrence of an element

number=[1,2,3]
print(number.index(2))    #output : 1

#reverse()-Reverses the list in place

numbers=[1,2,3]
numbers.reverse()
print(number)            #output : [3,2,1]

#sort(reverse=False)-sorts the list in ascending order(default) or descending order (if reverse=True)

numbers=[3,1,2]
numbers.sort()
print(number)           #output : [1,2,3]

#clear()-Removes all elements from the list

numbers=[1,2,3]
numbers.clear()
print(numbers)         #output : []


#SET methods:

#add(element)-Adds an element to the set
s={1,2}
s.add(3)
print(s)       #output : {1,2,3}

#remove(element)-removes the specified element. raises keyerror if not found

s={1,2,3}
s,remove(2)
print(s)       #output : {1,3}

#discard(element)_Removes the spaecified element but does not raise an error if not found

s={"apple","banana","kiwi"}
s.discard("orange")
print(s)         #output : {'apple','banana','kiwi}

#pop()_Removes an returns an arbitrary element

s={1,2,3,4}
print(s.pop())    #output : 1
print(s)         #output : {2,3,4}

#clear()-Removes all elements from the set
s={1,2,3}
s,clear()
print(s)          # output: set()

#union(other_set)-Return a set containsing all elements from both sets

s={1,2}
s2={3,2}
print(s.union(s2))     #output :{1,2,3}

#intersection(other_set)-returns element common to both sets

s1={1,2}
s2={2,4}
print(s1.intersection(s2))        #output : {2}


#difference(other_set)-returns elements in the first set but not in the second

s1={1,2}
s2={2,3}
print(s1.symmetric_difference(s1))      #output : {1,3}


#issubset(other_set)-check if all elements of the set sre in another set

s1={2,3}
s2={2,3,4}
print(s1.issubset(s2))            #output : True

#issuperset(other_set)-check if the set contains all elements of another set

s1={1,2,3}
s2={3,4}
print(s.issuperset(s2))              #output : True


#isdisjoint(other-set)-returns true if the sets have no elements in common 

s1={1,2,}
s2={3,4}
print(s.isdisjoint(s2))     #output : true