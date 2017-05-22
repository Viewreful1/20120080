def dfs(a, check, now):
    if check[now]:
        return
    check[now] = True
    print(now, end=' ')
    for nxt in a[now]:
        dfs(a, check, nxt)
        
def bfs(a, start):
    check = [False] * (n+1)
    queue = []
    queue.append(start)
    check[start] = True
    while queue:
        now = queue[0]
        print(queue.pop(0), end=' ')
        for nxt in a[now]:
            if check[nxt]:
                continue
            queue.append(nxt)
            check[nxt] = True
            
n, m , start  = map(int, input().split())
a = []
for i in range(0, n+1):
    a.append([])
for i in range(0, m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(n):
    a[i].sort()
check = [False] * (n+1)

dfs(a, check, start)
print()
bfs(a, start)
print()