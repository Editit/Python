# Defining the locations of the police and the drug traces 
police = [2, 4, 5] 
drug_traces = [3, 8, 9] 

G = nx.Graph() 
G.add_edges_from(edges) 
mapping = {0:'0 - Detective', 1:'1', 2:'2 - Police', 3:'3 - Drug traces', 
		4:'4 - Police', 5:'5 - Police', 6:'6', 7:'7', 8:'Drug traces', 
		9:'9 - Drug traces', 10:'10 - Drug racket location'} 

H = nx.relabel_nodes(G, mapping) 
pos = nx.spring_layout(H) 
nx.draw_networkx_nodes(H, pos, node_size =[200, 200, 200, 200, 200, 200, 200, 200]) 
nx.draw_networkx_edges(H, pos) 
nx.draw_networkx_labels(H, pos) 
pl.show() 
