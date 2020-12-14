
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
		
	def getEdges(graph):
		eList = {vertex : set() for vertex in graph.V}
		for edge in graph.E:
			eList[edge.a].add(edge)
			eList[edge.b].add(edge)
		return eList

	def getNeighbors(graph):
		nList = {vertex : set() for vertex in graph.V}
		for edge in graph.E:
			nList[edge.a].add(edge.b)
			nList[edge.b].add(edge.a)
		return nList
	

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
		
		
		for v in graph.V:
			if v == -1:
				count = FindNeighbors(graph, player, v)
				if count < 4:
					return v
				if count < 3:
					return v
		'''
		

		vertexHeap = []
		nList = PercolationPlayer.getNeighbors(graph)
		count = 0
		vertexList = graph.V
		for vertex in vertexList:
			if vertex.color == -1:
				heur = 0
				for neighbor in nList[vertex]:
					heur -= 30
					if neighbor.color == player: heur += 5
					if len(nList[neighbor]) == 1: heur -= 1
					if neighbor.color == 1 - player: heur += len(nList[neighbor])
				heapq.heappush(vertexHeap, (heur, count, vertex))
				count += 1
		if vertexHeap: return heapq.heappop(vertexHeap)[2]

		
		'''
		
		degrees={vertex: 0 for vertex in graph.V}
		for edge in graph.E:
			degrees[edge.a] +=1
			degrees[edge.b] += 1
		max_key = max(degrees, key=degrees.get)
		while max_key.color != -1:
			degrees.pop(max_key)
			max_key = max(degrees, key=degrees.get)


		
		return max_key
		
		
		'''

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
