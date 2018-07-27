==============================================
===////////////////Graph//////////////////====
==============================================

============Depth first search (Graph)=========
created array for visited

mark current node(starter) and print it
look at all adjacent verticies 
if not visited call node recursivly


===========Breadth first search (Graph)========
create array for visited
create a queue[]

add current node to queue and mark as visited

while queue exists 
pop queue
print popped element
go thru adjacent to popped
if not visited add to que and mark as visited


===========================================
===///////////////Sorting///////////////===
===========================================

=================Bubble Sort================
go thru and compare each element and if i > i + 1 swap elements
check if there are no swaps as you go along, if no swaps, youre done

=================Insertion Sort=============
iterate for how many elemnts there are in array
create key with current element of array
start with first to left of key, then iterate down to zero
check if key is < current iteration move current iteration one to the right
then once we hit a key > current iteration we set that iter + 1 = key

[1, 12, 14, 2, 9, 11] 	origional

[1, 12, 14, 2, 9, 11] 	key = 12 follow = 1, array[follow+1] = key 

[1, 12, 14, 2, 9, 11] 	key = 14 follow = 12 #next key array[follow+1] = key 

[1, 12, 14, 14, 9, 11] 	key = 2 follow = 14, follow[i+1] = follow[]

[1, 12, 12, 14, 9, 11]	key = 2 follow = 12, follow[i+1] = follow[] 	

[1, 2, 12, 14, 9, 11]	key = 2 follow = 1, array[follow+1] = key

[1, 2, 12, 14, 14, 11] 

[1, 2, 12, 12, 14, 11]

[1, 2, 9, 12, 14, 11]

[1, 2, 9, 12, 14, 14]

[1, 2, 9, 12, 12, 14]

[1, 2, 9, 11, 12, 14]