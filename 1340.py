# @author Matheus Alves dos Santos
# TITLE: Eu Posso Adivinhar a Estrutura de Dados!
# ID: 1340

from collections import deque

while (True):
	try:
		queue = deque()
		stack = []
		priority_queue = []
		data_structures = [True, True, True]
		  
		n_lines = int(raw_input())

		for i in range(n_lines):
			query = map(int, raw_input().split())

			if (query[0] == 1):
				queue.appendleft(query[1])
				stack.append(query[1])
				priority_queue.append(query[1])

			else:
				priority_queue.sort()
				
				if (queue.pop() != query[1]):
					data_structures[0] = False
				if (stack.pop() != query[1]):
					data_structures[1] = False
				if (priority_queue.pop() != query[1]):
					data_structures[2] = False

		if (data_structures == [False, False, False]):
			print "impossible"
		elif (data_structures == [True, False, False]):
			print "queue"
		elif (data_structures == [False, True, False]):
			print "stack"
		elif (data_structures == [False, False, True]):
			print "priority queue"
		else:
			print "not sure"
	
	except:
		break    
