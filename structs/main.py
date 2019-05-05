#coding utf-8

from controller import Controller

def main():

    ctrl = Controller()
    ctrl.show_folders()
    #help(Controller)
    while True:
        op = ctrl.show_menu()
        if op.lower() == 's':
            exit()
        elif int(op) not in list(range(1,10)):
            print('Opção inválida!')
        else:
            if op == '1':
                ctrl.select_data_structure()
            elif op == '2':
                ctrl.DFS()
            elif op == '3':
                ctrl.BFS()
            elif op == '4':
                ctrl.caminho_entre_vertex()
            elif op == '5':
                ctrl.is_conected()
            elif op == '6':
                ctrl.prim()
            elif op == '7':
                ctrl.kruskal()
            elif op == '8':
                ctrl.dijkstra()
            elif op == '9':
                ctrl.bellman_ford()
            
                
    
    
    

if __name__ == '__main__':
    main()