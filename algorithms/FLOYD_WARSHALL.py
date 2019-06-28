from collections import defaultdict


def FLOYD_WARSHALL(G):
    d = defaultdict(dict)
    p = defaultdict(dict)

    for i in G.vertexes:
        for j in G.vertexes[i]:
            d[i][j] = G.get_value(i, j)
            p[i][j] = None

    for k in range(1, G.get_len()):
        for i in G.vertexes:
            for j in G.vertexes[i]:
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = k