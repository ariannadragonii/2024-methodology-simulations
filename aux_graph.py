# returns producers of a graph
def find_producers(graph):
    producers = [node for node in graph.nodes if not list(graph.predecessors(node))]
    return producers

# returns consumers of a graph
def find_consumers(graph):
    consumers = [node for node in graph.nodes if not list(graph.successors(node))]
    return consumers

# returns internal nodes of a graph
def find_action_nodes(graph):
    return [node for node in graph.nodes if node not in find_consumers(graph) + find_producers(graph)]

# returns input frequency of a node in a graph
def find_f_in(graph, node_id): 
    preds = list(graph.predecessors(node_id))
    f_ins = []
    for pred in preds:
        f_ins.append(graph[pred][node_id]['f'])
        f_in = max(f_ins)
    return f_in

# returns input frequency of a node in a graph
def find_f_out(graph, node_id):
    succs = list(graph.successors(node_id))
    f_outs = []
    for succ in succs:
        f_outs.append(graph[node_id][succ]['f'])
        f_out = max(f_outs)
    return f_out