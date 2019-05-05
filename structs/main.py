#coding utf-8

from controller import Controller



def main():

    ctrl = Controller()
    ctrl.show_folders()
    # while True:
    #     op = ctrl.show_menu()
    #     if op.lower() == 's':
    #         exit()
    
    ctrl.get_vertexes()
    ctrl.get_edges()


if __name__ == '__main__':
    main()