from math import prod
import networkx as nx

G = nx.DiGraph()
for a, *b in map(str.split, open('./input/day_11.txt')):
    G.add_edges_from([(a[:-1],c) for c in b])

print(len(list( nx.shortest_simple_paths(G, source='you', target='out'))))

r = ['svr','fft','dac','out']
r_order = [[r[i],r[i+1]] for i in range(len(r)-1)]
suspects = set().union(*[nx.descendants(G, a) & nx.ancestors(G,b) for a, b in r_order])
G.remove_nodes_from(G.nodes - (suspects | set(r)))

print(prod(len(list(nx.all_simple_paths(G, source=a,target=b))) for a, b in r_order))