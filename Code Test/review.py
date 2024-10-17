#!/usr/bin/env python
# coding: utf-8

# In[6]:


### 3 Code Review


# Review 1

def add_to_list(value, my_list=[]):

    my_list.append(value)

    return my_list

 #ANS: By using the argument my_list=[], each call of add_to_list will modify the same list and thus created unwanted result. 
 #A modified code is shown below
def add_to_list_revised(value, my_list = None):
     if my_list is None:
         my_list =[]
     my_list.append(value)
     return my_list()


# In[7]:


# Review 2

def format_greeting(name, age):

    return "Hello, my name is {name} and I am {age} years old."

#AMS: There is an format error in the 2nd line of code, and we should use f_strings in order to return the desire name and age. 
#The modified code is shown below
def format_greeting_revised(name, age):
    return f"Hello, my name is {name} and I am {age} years old."


# In[11]:


# Review 3

class Counter:

    count = 0

 

    def __init__(self):

        self.count += 1

 

    def get_count(self):

        return self.count

#ANS: count should be an instance variable instead of a class variable. Otherwise, all counter instances will sahre the same count.
#The modified code is shown below

class Counter:
    def __init__(self):
        self.count = 1  # Initialize count per instance

    def get_count(self):
        return self.count


# In[ ]:


# Review 4

import threading

 

class SafeCounter:

    def __init__(self):

        self.count = 0

 

    def increment(self):

        self.count += 1

 

def worker(counter):

    for _ in range(1000):

        counter.increment()

 

counter = SafeCounter()

threads = []

for _ in range(10):

    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)

 

for t in threads:

    t.join()

#ANS: The increment method is not thread safe. A race condition may occure in the part of coding in this case. 
#Thus, we need to modify the initialization as well as the increment method as shown below

class SafeCounter:

    def __init__(self):

        self.count = 0
        self.lock() = thread.lock()

 

    def increment(self):
        with self.lock():
            self.count += 1


# In[ ]:


# Review 5

def count_occurrences(lst):

    counts = {}

    for item in lst:

        if item in counts:

            counts[item] =+ 1

        else:

            counts[item] = 1

    return counts

#ANS: There is an operator error in this code. count[item] =+ 1 should be count[item] += 1
# The modified code is shown below
def count_occurrences(lst):

    counts = {}

    for item in lst:

        if item in counts:

            count[item] += 1

        else:

            counts[item] = 1

    return counts

