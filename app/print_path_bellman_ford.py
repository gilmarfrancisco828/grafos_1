from algorithms.BELLMAN_FORD import *
from structs.graph import Type


def print_path(result, s):
    for u in result.d:
        print("Vértice:", u)

        if result.pi[u] is None and u == s:
            print("Caminho: Raiz", end='')
        else:
            # if result.pi[u] is None:
            #     print("Não são conectados", end='')
            # else:
                print("Caminho:", u, end='')
                inc = u
                len = result.d[inc]
                # print(result.d[inc])
                # input()
                while result.pi[inc] is not None:
                    print(" <-- " + str(result.pi[inc]), end='')
                    inc = result.pi[inc]
                    # len += result.d[inc]
                print("\n\tDistância:", len, end='')
        print("\n")

