import random
import benchmark.py

class PercolationPlayer:

	degrees = {vertex: 0 for vertex in graph.V}
	for edge in edges.V:
		degrees[edge.a] +=1
		degrees[edge.b] += 1

	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == -1
	def ChooseVertexToColor(graph, player):
		degrees1 = {vertex: 0 for vertex in graph.V}
		for edge in edges.V:
			degrees1[edge.a] +=1
			degrees1[edge.b] += 1
		max_key = max(degrees1, key=degrees1.get)
		while max_key.color != -1:
			degrees1.pop(max_key)
			max_key = max(degrees1, key=degrees1.get)
		return max_key

			


	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == player
	def ChooseVertexToRemove(graph, player):
		for v in graph.V:
			if v.color == player:
				for e in graph.IncidentEdges(v):
					if e.a.color != player or e.b.color !=player:
						return v
		return random.choice([v for v in graph.V if v.color == player])




# Feel free to put any personal driver code here.
def main():
	pass

if __name__ == "__main__":
	main()
