#coding utf-8
from structs.controller import Controller
import os
#help(Controller)
def main():

    ctrl = Controller()
    ctrl.build_graph()
    
    while True:
        os.system('clear')
        op = ctrl.show_menu()
        if op.lower() == 's':
            exit()
        if op.isdigit == False:
            print('Opção inválida!')
        elif int(op) not in list(range(1,11)):
            print('Opção inválida!')
        else:
            if op == '1':
                ctrl.ctrl_connected_components()   
            elif op == '2':
                ctrl.ctrl_coloring()
            elif op == '3':
                ctrl.ctrl_mst()
            elif op == '4':
                print(ctrl.get_vertexes())
                s = input('Insira o vértice inicial: ')
                ctrl.ctrl_shortest_path(s)

            elif op == '5':
                ctrl.ctrl_connectivity()
            elif op == '6':
                ctrl.ctrl_transpose()
            elif op == '7':
                ctrl.ctrl_topological_sort()
            elif op == '8':
                print(ctrl.get_vertexes())
                s = input('Insira o vértice inicial: ')
                ctrl.ctrl_BFS(s)
            elif op == '9':
                ctrl.build_graph()
            elif op == '10':
                ctrl.sudoku()
                
            
            
                
    
    
    

if __name__ == '__main__':
    main()