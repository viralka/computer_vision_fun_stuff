'''
Implementation of the standard datastructure 
'''
import collections

#* list 

list_ = ['element', 'element', 'element', 'element'] # muutable, costely to inserting & deleting elements and to add elements if memory is full
ex_list = list('standard')

#* Dictionary
#key value pairs, keys are hashable 

a = {"key1": "value1", "key2": "value2"}


#* Tuple
#immutable, heterogenious, 

tuple_ = (1, 2, 3, 4, 5, 6)


#* Set
# set itself is mutable but the element in set are immutable, heterogenious, no duplicates

same_set_ = set([1, 2, 3, 4, 5])
same_set_ = {1, 2, 3, 4, 5}

#* frozen set 
# it is immutable, no function no nothing can change it 

froz_set = frozenset([1, 2, 3, 4, 5])

#* string 
# array of bytes representing Unicode , it is immutable

string1  =  'hi'

#* counter 
# it is subclass of dictionary.

#  With sequence of items 
example1 = collections.Counter(['B','B','A','B','C','A','B','B','A','C'])
#! Counter({'B': 5, 'A': 3, 'C': 2})   

# with dictionary
count = collections.Counter({'A':3, 'B':5, 'C':2})
#! Counter({'B': 5, 'A': 3, 'C': 2})

count.update(['A', 1])
#! Counter({'B': 5, 'A': 4, 'C': 2, 1: 1})


#* OrderedDict
# it is just ordered dictionary (remenber the order it in which keys are intered)

#! Run and see the output
print('--------------------------------')
#? print('ordered dictionary')

#? print('Initialized')
od = collections.OrderedDict()
od["a"]= 1
od["b"]= 2
od["c"]= 3
od["d"]= 4

for keys, values in od.items():
    #? print(keys, values)
    pass
#? print('see it remenber its order') 

od["a"]= 1
#? print('\n\n')
for keys, values in od.items():
    pass
    #? print(keys, values)
#? print('it do not changes its order by just iterating')

#* Default dictionary

# Defining the dict
d = collections.defaultdict(int)
      
L = [1, 2, 3, 4, 2, 4, 1, 2]
      
# Iterate through the list
# for keeping the count
for i in L:
          
    # The default value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1
          
#? print(d)

#* Chain Map
# it encapsulates many dict and return a single list of dictionary
# and keys are searched in one by one until end 
	
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
	
# Defining the chainmap
c = collections.ChainMap(d1, d2, d3)
#? print(c)

#? print(c['a'])
#? print()
#? print()

#* Named Tuple
# it gives name to the position in the tupele like now L[1] can be said as l.name 

S = collections.namedtuple('S', ["name", "age", "gender"])

test = S("hen", 23, "F")

#? print(test.name)

#* Deque
#double ended Queue , O(n) for pop , o(1) for appendeing , made used double linked list 

de = collections.deque([1,2,3,4,5,6,7,8,9,10,11])

# append() add element at right end of the deque
de.append(12)

# appendleft() add element at left end of the deque
de.appendleft(13)

# appendright() add element at right end of the deque
de.pop()

# popleft() pop element at left end of the deque
de.popleft()


#* Linked List
# first elememt is head and other are node 
# Each node have data and link 

class Node: 

    def __init__(self, data): 
        self.data = data  # Assign data to the node
        self.next = None
    
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    # Insert new node at the beginning of the linked list 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Insert new node after the given prev_node 
    def insertAfter(self, prev_node, new_data): 
        if prev_node is None: 
            print("the given previous node must be in linked list")
            return
        new_node = Node(new_node) 
        new_node.next = prev_node.next
        prev_node.next = new_node 
  
    # Append new node at the end of the linked list 
    def append(self, new_data): 
        new_node = Node(new_node) 
        new_node.next = None
        if self.head is None: 
            self.head = new_node 
            return
        last = self.head 
        while(last.next): 
            last = last.next
        last.next = new_node 
  
    # Delete node with given key 
    def deleteNode(self, key): 
        temp = self.head 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
        while(temp is not None): 
            if temp.data == key: 
                break
            prev = temp 
            temp = temp.next
        if(temp == None): 
            return
        prev.next = temp.next
        temp = None
  
    # Prints the linked list 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, end=" ") 
            temp = temp.next


#* stack 
# first in  last out // last in first out all funcion size, top, push, pop are -> O(1)
# can be implemented by list, deque, queue.LifoQueue

stack = []

# adding elements
stack.append("1")
stack.append("2")
stack.append("3")

# taking elements out
stack.pop()
stack.pop()

# doing by Queue

from queue import LifoQueue

# Initializing a stack
stack = LifoQueue(maxsize= 6)

# for knowing size of queue
stack.qsize()

# adding elements
stack.put("g")
stack.put("f")

# get function to pop the element
stack.get()

#* Queue
# First in and last out it is like a pipeline
# enqueues (adding in overflow condition), Dequeue , front(gitting first element) , rear(gitting last element) and all these funtion are O(1) 

# Initializing a queue
queue = []
  
# Adding elements to the queue
queue.append('g')
queue.append('f')
queue.append('g')
  
print("Initial queue")
print(queue)
  
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0)) # <--------------- this where there is difference in the implementation 
print(queue.pop(0))
  
print("\nQueue after removing elements")
print(queue)
  
# will raise and IndexError
# as the queue is now empty
from queue import Queue

# Initialized a queue
q = Queue(maxsize = 4)

# gives the size
q.qsize()





