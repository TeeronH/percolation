
import random
import heapq

class PercolationPlayer:
		
	
	def IncidentEdges(graph, vertex):
		return [e for e in graph.E if (e.a == vertex or e.b == vertex)]


	def FindNeighbors(graph, player, vertex):
		count = 0
		for e in PercolationPlayer.IncidentEdges(graph, vertex):
			if e.a.color == player and e.b.color == player:
				count = count + 2
			if e.a.color == player or e.b.color == player:
				count = count + 1
		return count
		

	

	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == -1
	def ChooseVertexToColor(graph, player):
		
		'''
		max_count = 0
		max_vertex = next(iter(graph.V))

		for v in [v for v in graph.V if v.color == -1]:
			if PercolationPlayer.FindNeighbors(graph, player, v) > max_count:
				max_count = PercolationPlayer.FindNeighbors(graph, player, v)
				max_vertex = v

		
		return max_vertex
		
		'''

		for v in graph.V:
			if v == -1:
				count = PercolationPlayer.FindNeighbors(graph, player, v)
				if count < 3:
					return v

		
	
		
		
		
		degrees={vertex: 0 for vertex in graph.V}
		for edge in graph.E:
			degrees[edge.a] +=1
			degrees[edge.b] += 1
		max_key = max(degrees, key=degrees.get)
		while max_key.color != -1:
			degrees.pop(max_key)
			max_key = max(degrees, key=degrees.get)

		
		return max_key
		
		
		


		
		
		

	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == player
	def ChooseVertexToRemove(graph, player):
		
		

		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color != player or e.b.color !=player:
						count = count + 1
				if count > 7:
					return v
		

		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color != player or e.b.color !=player:
						count = count + 1
				if count > 6:
					return v
		
		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color != player or e.b.color !=player:
						count = count + 1
				if count > 5:
					return v

		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color != player or e.b.color !=player:
						count = count + 1
				if count > 4:
					return v

		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color != player or e.b.color !=player:
						count = count + 1
				if count > 3:
					return v

		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color != player or e.b.color !=player:
						count = count + 1
				if count > 2:
					return v

		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color != player or e.b.color !=player:
						count = count + 1
				if count > 1:
					return v
		
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color != player or e.b.color !=player:
						return v
	

		
		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color == player or e.b.color ==player:
						count = count + 1
				if count < 2:
					return v
		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color == player or e.b.color ==player:
						count = count + 1
				if count < 3:
					return v

		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color == player or e.b.color ==player:
						count = count + 1
				if count < 4:
					return v
		
		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color == player or e.b.color ==player:
						count = count + 1
				if count < 5:
					return v

		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color == player or e.b.color ==player:
						count = count + 1
				if count < 6:
					return v
		
		
		count = 0
		for v in graph.V:
			if v.color == player:
				for e in PercolationPlayer.IncidentEdges(graph, v):
					if e.a.color == player or e.b.color ==player:
						count = count + 1
				if count < 7:
					return v
		
		
		
	
		
		
		return random.choice([v for v in graph.V if v.color == player])
		
		
		
		




# Feel free to put any personal driver code here.
def main():
	pass

if __name__ == "__main__":
	main()
