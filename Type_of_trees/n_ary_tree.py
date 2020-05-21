# Python3 program to count number of nodes 
# which has more children than its parent 
from collections import deque 

adj = [[] for i in range(100)] 

# function to count number of nodes 
# which has more children than its parent 
def countNodes(root): 

	count = 0

	# queue for applying BFS 
	q = deque() 

	# BFS algorithm 
	q.append(root) 

	while len(q) > 0: 

		node = q.popleft() 

		# traverse children of node 
		for i in adj[node]: 
			# children of node 
			children = i 

			# if number of childs of children 
			# is greater than number of childs 
			# of node, then increment count 
			if (len(adj[children]) > len(adj[node])): 
				count += 1
			q.append(children) 

	return count 


# Driver program to test above functions 

# construct n ary tree as shown 
# in above diagram 
adj[1].append(2) 
adj[1].append(3) 
adj[2].append(4) 
adj[2].append(5) 
adj[2].append(6) 
adj[3].append(9) 
adj[5].append(7) 
adj[5].append(8) 

root = 1

print(countNodes(root)) 

