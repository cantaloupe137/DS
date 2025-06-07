class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def dfs(node, x, y):
    if not node:
        return None
    if node.val == x or node.val == y:
        return node
    found = []
    for child in node.children:
        res = dfs(child, x, y)
        if res:
            found.append(res)
    if len(found) >= 2:
        return node
    return found[0] if found else None

while True:
    try:
        line = input()
        if not line.strip():
            continue
        n, x, y = map(int, line.split())
        nodes = dict()
        parent_of = dict()
        all_nodes = set()
        for _ in range(n):
            parts = list(map(int, input().split()))
            v0 = parts[0]
            if v0 not in nodes:
                nodes[v0] = Node(v0)
            for v in parts[1:]:
                if v not in nodes:
                    nodes[v] = Node(v)
                nodes[v0].children.append(nodes[v])
                parent_of[v] = v0
            all_nodes.add(v0)
            all_nodes.update(parts[1:])
        root = None
        for v in all_nodes:
            if v not in parent_of:
                root = nodes[v]
                break
        lca = dfs(root, x, y)
        print(lca.val if lca else None)
    except EOFError:
        break