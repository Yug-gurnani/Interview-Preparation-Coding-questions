"""
it is only applicable in directed acyclic graphs
"""
def dfs(graph,node,vis,st):
    vis[node] = 1
    for i in graph[node]:
        if i not in vis:
            dfs(graph,i,vis,st)
    st.append(node)
def topological_sort(graph):
    st = []
    vis = {}
    for node in graph:
        if node not in vis:
            dfs(graph,node,vis,st)
        
    print(*st[::-1])
graph = {5:[2,0],1:[],0:[],3:[1],2:[3],4:[0,1]}
topological_sort(graph)