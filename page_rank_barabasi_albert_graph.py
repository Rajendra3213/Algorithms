import networkx as nx
import matplotlib.pyplot as plt

# Generate Barabasi-Albert graph
G = nx.barabasi_albert_graph(60, 41)

# Calculate PageRank with damping factor 0.4
pr = nx.pagerank(G, 0.4)

# Draw the graph
pos = nx.spring_layout(G)  # Positions for all nodes

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=200, cmap=plt.cm.plasma)

# Draw edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Draw node labels
nx.draw_networkx_labels(G, pos, labels={node: f'{node}\nPR: {pr[node]:.3f}' for node in G.nodes()}, font_size=8)

# Show the plot
plt.title("Barabasi-Albert Graph with PageRank")
plt.axis('off')
plt.show()
