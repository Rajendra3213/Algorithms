import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes for the web pages
G.add_nodes_from(['A', 'B', 'C', 'D'])

# Add edges representing the links between pages
edges = [('D', 'B'),('D', 'A'),('D', 'C'), ('B', 'C'), ('B', 'A'), ('C', 'A')]
G.add_edges_from(edges)

# Set initial PageRank value of 0.25 for each page
initial_pagerank = {node: 0.25 for node in G.nodes()}

# Draw the initial graph
plt.figure(figsize=(15, 4))
pos = {'A': (-1, 0), 'B': (-1, -1), 'C': (1, -1), 'D': (1, 0)}
plt.subplot(1, 5, 1)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', edge_color='gray', arrowsize=20)
plt.title("Iteration 0")
plt.axis('off')

# Annotate nodes with their initial PageRank values
for node, (x, y) in pos.items():
    plt.text(x, y + 0.1, "{:.2f}".format(initial_pagerank[node]), fontsize=10, ha='center', va='center')

# Calculate PageRank iteratively for 4 iterations
pagerank_values = initial_pagerank.copy()
for i in range(4):
    new_pagerank = {}
    for node in G.nodes():
        new_pagerank[node] = 0.0
        for neighbor in G.predecessors(node):
            new_pagerank[node] += pagerank_values[neighbor] / len(list(G.successors(neighbor)))
    pagerank_values = new_pagerank
    
    # Draw the graph for each iteration
    plt.subplot(1, 5, i + 2)
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', edge_color='gray', arrowsize=20)
    plt.title("Iteration {}".format(i + 1))
    plt.axis('off')
    
    # Annotate nodes with their PageRank values
    for node, (x, y) in pos.items():
        plt.text(x, y + 0.1, "{:.3f}".format(pagerank_values[node]), fontsize=10, ha='center', va='center')

# Show the plot
plt.tight_layout()
plt.show()
