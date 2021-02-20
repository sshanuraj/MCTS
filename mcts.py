import numpy as np 
import random as rd 

INF = 10000000

class Node:
	def __init__(self, total_score, ni, par):
		self.t = total_score
		self.n = ni
		self.n_actions = rd.randrange(2, 5)
		self.children = []
		self.parent = par
		self.isTerminal = False

	def goUp(self):
		return self.parent

	def populate(self, curr_depth, max_depth):
		if self.isTerminal:
			return None
		for i in range(self.n_actions):
			node = Node(0, 0, self)
			if depth == max_depth:
				node.isTerminal = True
			self.children.append(node)

	def getMaxUcbNode(self, N):
		ucbs = []
		if self.isTerminal:
			return None
		for node in self.children:
			ucbs.append(node.calculateUCB(N))
		ucbs = np.array(ucbs)
		return self.children(np.argmax(ucbs))

	def calculateUCB(self, N):
		if self.n == 0:
			return INF
		ucb = (self.t/self.n) + (np.log(N)/self.n)**0.5
		return ucb

	def checkLeaf(self):
		if len(self.children) == 0:
			return True
		return False

	def getRandomizedValue(self):
		return rd.randrange(-10, 11)

	def backpropagate(self, reward):
		return None

	def rollout(self):
		return self.getRandomizedValue()


class Tree:
	def __init__(self, root, max_depth):
		self.root = root
		self.N = 0 #total iterations
		self.max_depth = max_depth
		self.root.populate(0, self.max_depth)

	def startPlay(self, depth, n_iterations):
		curr_depth = 0
		curr = self.root
		count = 0
		N = self.N

		while n_iterations > count:
			curr = self.root

			if curr.checkLeaf():
				if curr.n == 0:
					if curr.isTerminal:
						reward = curr.getRandomizedValue()
						curr.backpropagate(reward)
						count += 1
						continue
					curr.rollout(curr_depth)
				else:
					curr.populate() #expansion
					curr = curr.getMaxUcbNode(N)
					if curr == None:
						reward = curr.getRandomizedValue()
						curr.backpropagate(reward)
						count += 1
						continue
					curr_depth += 1
					reward = curr.rollout(curr_depth) #rollout and backpropagete
					curr.backpropagate(reward)
					count += 1
			else:
				curr = curr.getMaxUcbNode(N) #selection
				curr_depth += 1



