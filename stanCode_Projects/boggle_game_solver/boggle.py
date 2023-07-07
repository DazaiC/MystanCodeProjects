"""
File: boggle.py
Name: Dazai
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

class Node:
	def __init__(self, alpha, visited=False):
		self.alpha = alpha # store alphabet
		self.visited = visited # store if the node has visited

def main():
	"""
	First, use a 2D graph to store input datas which is consisted of custom node class
	Second,
	"""
	rows, cols = (4, 4)
	alpha_graph = [[],[],[],[]] # 2D graph to store node

	for row in range(rows):
		datas = input(f'{row+1} row of letters: ').split()
		if len(datas) != cols: # Return if the input datas are not 4 items
			print('Illegal input')
			return

		for col in range(cols): # Loop over the input datas
			if len(datas[col]) > 1: # Return if the input data is longer than 1
				print('Illegal input')
				return
			if not datas[col].isalpha(): # Return if the input data is not alpha
				print('Illegal input')
				return
			alpha_graph[row].append(Node(datas[col].lower(), False)) # Construct a node and append to graph


	start = time.time()
	d = read_dictionary() # Initiate dictionary
	found_list = set() # Initiate a set to store the valid word
	# Chose the first alphabet
	for row in range(rows):
		for col in range(cols):
			s = alpha_graph[row][col].alpha # s: string to store the letter
			alpha_graph[row][col].visited = True # Update bool value
			permutation(row, col, alpha_graph, s, found_list, d)
			alpha_graph[row][col].visited = False # Restore bool value
	print(f'There are {len(found_list)} words in total.')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')



def permutation(row, col, alpha_graph, s, found_list, d):
	if len(s) > 16:
		pass
	else:
		# Find neighboring letter
		for i in [-1, 0, 1]:
			for j in [-1, 0, 1]:
				neighbor_row = row + i # neighboring letter row index
				neighbor_col = col + j # neighboring letter col index
				if 0 <= neighbor_row <= 3 and 0 <= neighbor_col <= 3: # Check if neighboring index are in the valid range
					if alpha_graph[neighbor_row][neighbor_col].visited is False: # Check if the neighboring letter has visited
						# Choose
						s += alpha_graph[neighbor_row][neighbor_col].alpha

						# Explore
						if has_prefix(s, d): # Check prefix to optimize
							if len(s) >= 4: # the length of string >= 4, then to search dictionary
								if s in d and s not in found_list:
									print(f'Found "{s}"')
									found_list.add(s)
							alpha_graph[neighbor_row][neighbor_col].visited = True # Update bool value
							permutation(neighbor_row, neighbor_col, alpha_graph, s, found_list, d) # Explore


						# Un-choose
						s = s[:-1] # Restore string
						alpha_graph[neighbor_row][neighbor_col].visited = False # Restore bool value



def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""

	d = set() # Set to store word
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			if 4 <= len(line) <= 16: # Only store the word which length is between 4~16
				d.add(line)
	return d


def has_prefix(sub_s, d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in d:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
