import networkx as nx

data = open('./input/day_11.txt').read().splitlines()
G = nx.DiGraph()

for d in data:
    a, *b = d.split()
    for node in b:
        G.add_edge(a[:-1],node)

print(len(list( nx.shortest_simple_paths(G, source='you', target='out'))))

suspects = nx.descendants(G,'svr') & nx.ancestors(G, 'fft') | nx.descendants(G,'fft') & nx.ancestors(G,'dac') | nx.descendants(G,'dac') & nx.ancestors(G,'out')

for node in list(G.nodes):
    if node not in suspects | {'svr','fft','dac','out'}:
        G.remove_node(node)

svr_to_fft = nx.all_simple_paths(G, source='svr',target='fft')
fft_to_dac = nx.all_simple_paths(G, source='fft',target='dac')
dac_to_out = nx.all_simple_paths(G, source='dac',target='out')
print(len(list(svr_to_fft)) * len(list(fft_to_dac)) * len(list(dac_to_out)))