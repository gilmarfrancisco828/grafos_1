#coding utf-8
from structs.controller import Controller
import os
#help(Controller)
def main():

    ctrl = Controller()
    ctrl.show_folders()
    #help(Controller)
    while True:
        os.system('clear')
        op = ctrl.show_menu()
        if op.lower() == 's':
            exit()
        if op.isdigit == False:
            print('Opção inválida!')
        elif int(op) not in list(range(1,10)):
            print('Opção inválida!')
        else:
            if op == '1':
                ds = ctrl.select_data_structure()
                ctrl.create_graph(ctrl.get_contents(), ds,ctrl.is_graph())
                #TODO adicionar verificacao valorado ou nao
            elif op == '2':
                s = ctrl.select_vertex()
                ctrl.DFS(s)
            elif op == '3':
                s = ctrl.select_vertex()
                ctrl.BFS(s)
            elif op == '4':
                s = ctrl.select_vertex()
                t = ctrl.select_vertex()
                ctrl.caminho_entre_vertex(s, t)
            elif op == '5':
                ctrl.is_conected()
            elif op == '6':
                s = ctrl.select_vertex()
                ctrl.prim(s)
            elif op == '7':
                ctrl.kruskal()
            elif op == '8':
                ctrl.dijkstra(s)
            elif op == '9':
                s = ctrl.select_vertex()
                ctrl.bellman_ford(s)
            
            
                
    
    
    

if __name__ == '__main__':
    main()