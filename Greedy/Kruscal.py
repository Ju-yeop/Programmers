parent = []
set_size = 0

def init(setN):
    global parent, set_size
    set_size = setN
    for _ in range(setN):
        parent.append(-1)

def find(id):
    global parent
    while parent[id] >= 0:
        id = parent[id]
    return id

def union(p1, p2):
    global parent, set_size
    parent[p1] = p2
    set_size -= 1

def kruscal(vertex, adj):
    v_size = len(vertex)
    ls = []
    init(v_size)
    for i in range(v_size - 1):
        for j in range(i+1, v_size):
            if adj[i][j] is not None:
                ls.append([i, j, adj[i][j]])
    ls.sort(key=lambda n: n[2], reverse=True)

    current_link = 0
    while current_link < v_size - 1:
        item = ls.pop(-1)
        x_p = find(item[0])
        y_p = find(item[1])
        if x_p != y_p:
            print("간선 추가: (%s, %s, %d)" % (vertex[item[0]], vertex[item[1]], item[2]))
            union(x_p, y_p)
            current_link += 1


vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[None, 29, None, None, None, 10, None],
          [29, None, 16, None, None, None, 15],
          [None, 16, None, 12, None, None, None],
          [None, None, 12, None, 22, None, 18],
          [None, None, None, 22, None, 27, 25],
          [10, None, None, None, 27, None, None],
          [None, 15, None, 18, 25, None, None]]

kruscal(vertex, weight)



