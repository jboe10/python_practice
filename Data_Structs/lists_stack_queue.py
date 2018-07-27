##############     tricks ##########
sqaures = [x**2 for x in range(10)]
#sqaures = [0 ,1 ,4 ,9 ,16 ...... 81]




#####################################################################

fruits  = ['orange', 'apple','pear','banana','kiwi','apple','banana']

fruits.count('apple')
fruits.count('tangerine')

fruits.index('banana')
fruits.index('banana',4) #find next banana starting at pos 4

fruits.reverse()
print(fruits)

fruits.append('grape') #add onto end
fruits

fruits.pop() #pop of last item
fruits

fruits.sort()
fruits

############################# list as a stack ############################

stack = [1,2,3,4]
stack.append(5)
stack.append(6)

stack.pop()
stack.pop


######################### list as Queue

from collections import deque

queue = deque([1,2,3])
deque.popleft()


