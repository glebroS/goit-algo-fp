import uuid
import networkx as nx
import matplotlib.pyplot as plt
import collections


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def generate_color(step, total_steps):
    start_r, start_g, start_b = 0, 0, 50 
    end_r, end_g, end_b = 100, 200, 255 

    r = int(start_r + (end_r - start_r) * (step / total_steps))
    g = int(start_g + (end_g - start_g) * (step / total_steps))
    b = int(start_b + (end_b - start_b) * (step / total_steps))

    return f'#{r:02x}{g:02x}{b:02x}'


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def dfs_visualize(root):
    if root is None:
        return

    total_steps = count_nodes(root)
    
    stack = [root]
    visited = set()
    
    traversal_order = []
    
    while stack:
        node = stack.pop()
        
        if node.id not in visited:
            visited.add(node.id)
            traversal_order.append(node)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    for i, node in enumerate(traversal_order):
        node.color = generate_color(i, total_steps)
    
    draw_tree(root, "DFS Visualization (Depth First Search)")


def bfs_visualize(root):
    if root is None:
        return
        
    total_steps = count_nodes(root)
    queue = collections.deque([root])
    visited = set()
    traversal_order = []
    
    while queue:
        node = queue.popleft()
        
        if node.id not in visited:
            visited.add(node.id)
            traversal_order.append(node)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    for i, node in enumerate(traversal_order):
        node.color = generate_color(i, total_steps)
        
    draw_tree(root, "BFS Visualization (Breadth First Search)")


if __name__ == "__main__":
    # Створення дерева для тестів
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    
    # DFS
    print("Візуалізація DFS...")
    dfs_visualize(root)
    
    # Створимо дерево заново для чистоти експерименту
    root2 = Node(0)
    root2.left = Node(4)
    root2.left.left = Node(5)
    root2.left.right = Node(10)
    root2.right = Node(1)
    root2.right.left = Node(3)
    
    # BFS
    print("Візуалізація BFS...")
    bfs_visualize(root2)
