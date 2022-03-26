from sys import stdin, stdout
from tokenize import String
import time

class User(object):
    def __init__(self, username: String, cc_number: String, date: String):
        self.username = username
        self.cards = []
        self.new_card(cc_number, date)

    def new_card(self, cc_number, date):
        self.cards.append([cc_number, date])
        self.cards = sorted(self.cards, key=lambda card: card[0])


class Node:
    def __init__(self, username: String, cc_number: String, date: String):
        self.user = User(username, cc_number, date)
        self.parent = None
        self.height = 0
        self.left_child = None
        self.right_child = None
    
    def print_node(self):
        self.user.print_user_info(True)

    


# ----------- AVL TREE -----------


class AVLTree(object):

    def __init__(self):
        self.root = None

    # adiciona um novo no a arvore
    def add_node(self, username, cc_number, date):
        if not self.root:
            self.root = Node(username, cc_number, date)
        else:
            new_node = self.insert_node(self.root, username, cc_number, date)
            self.walk_up(new_node)

    # insere o novo no na arvore
    def insert_node(self, node: Node, username, cc_number, date):
        if node.user.username > username:
            if not node.left_child:
                node.left_child = Node(username, cc_number, date)
                node.left_child.parent = node
                return node.left_child

            return self.insert_node(node.left_child, username, cc_number, date)
        
        else:
            if not node.right_child:
                node.right_child = Node(username, cc_number, date)
                node.right_child.parent = node
                return node.right_child

            return self.insert_node(node.right_child, username, cc_number, date)

    # adiciona mais um cartao a um user
    def add_node_info(self, node: Node, cc_number, date):
        for i in range(len(node.user.cards)):
            if node.user.cards[i][0] == cc_number:
                node.user.cards[i][1] = date
                #outln("CARTAO ATUALIZADO")
                return
        node.user.new_card(cc_number, date)
        #outln("NOVO CARTAO INSERIDO")
        return

        

    # encontra um no especifico
    def find_node(self, username, node: Node):
        if node is None:
            return False
        if node.user.username > username:
            return self.find_node(username, node.left_child)
        elif node.user.username < username:
            return self.find_node(username, node.right_child)
        return node

    # apaga a arvore toda
    def delete_tree(self):
        self.root = None
        #outln("LISTAGEM APAGADA")
        
        
            

    # passa pela arvore    
    def traverse_tree(self):
        if not self.root:
            return iter(())
        return self.traverse_inorder(self.root)




    # da yield a todos os nos da esquera para a direita
    def traverse_inorder(self, node):
        if node.left_child:
            yield from self.traverse_inorder(node.left_child)
        yield node
        if node.right_child:
            yield from self.traverse_inorder(node.right_child)
    

    def walk_up(self, node):
        if not node:
            return
        else:
            self.check_node(node)
            return self.walk_up(node.parent)

    def check_node(self, node: Node):
        left_height = -1
        right_height = -1
        if node.left_child:
            left_height = node.left_child.height
        if node.right_child:
            right_height = node.right_child.height
        if abs(left_height - right_height) > 1:
            if left_height < right_height:
                if node.right_child:
                    self.left_rotate(node, node.right_child)
                else:
                    self.right_rotate(node, node.left_child)
            else:
                if node.left_child:
                    self.right_rotate(node, node.left_child)
                else:
                    self.left_rotate(node, node.right_child)
        else:
            node.height = max(left_height, right_height) + 1

    


   
    def left_rotate(self, node, child_node):
        if child_node.left_child:
            node.right_child = child_node.left_child
            node.right_child.parent = node
        else:
            node.right_child = None

        if node != self.root:
            child_node.parent = node.parent
            if node.parent.right_child == node:
                node.parent.right_child = child_node
            else:
                node.parent.left_child = child_node
        else:
            child_node.parent = None
            self.root = child_node

        child_node.left_child = node
        node.parent = child_node

        node.height -= 1

    

    def right_rotate(self, node, child_node):
        if child_node.right_child:
            node.left_child = child_node.right_child
            node.left_child.parent = node
        else:
            node.left_child = None

        if node != self.root:
            child_node.parent = node.parent
            if node.parent.right_child == node:
                node.parent.right_child = child_node
            else:
                node.parent.left_child = child_node
            # node.parent.left_child = child_node
        else:
            child_node.parent = None
            self.root = child_node

        child_node.right_child = node
        node.parent = child_node

        node.height -= 1


# --------- funtions ---------



def readln(file):
    return file.readline().rstrip().split(" ")


def outln(string):
    stdout.write(string.rstrip() + "\n")


def main(test_file):
    avl_tree = AVLTree()
    user_in = [""]
    run_time = 0

    with open(test_file, "r") as file:
        try:
            while True:
                user_in = readln(file)
                start_time = time.time()
                if user_in[0] == "ACRESCENTA":
                    if not avl_tree.find_node(user_in[1], avl_tree.root):
                        avl_tree.add_node(user_in[1], user_in[2], user_in[3])
                        #outln("NOVO UTILIZADOR CRIADO")
                    else:
                        user_node = avl_tree.find_node(user_in[1], avl_tree.root)
                        avl_tree.add_node_info(user_node, user_in[2], user_in[3])


                elif user_in[0] == "CONSULTA":
                    if not avl_tree.find_node(user_in[1], avl_tree.root):
                        pass
                        #outln("NAO ENCONTRADO")
                    else:
                        user_node = avl_tree.find_node(user_in[1], avl_tree.root)
                        for i in range(len(user_node.user.cards)):
                            pass
                            #outln(user_node.user.cards[i][0] + " " + user_node.user.cards[i][1])
                        #outln("FIM")
                    

                #elif user_in[0] == "LISTAGEM":
                    #list_users(avl_tree)

                elif user_in[0] == "APAGA":
                    avl_tree.delete_tree()
                
                elif user_in[0] == "FIM":
                    break
                
                else:
                    break
                run_time += (time.time() - start_time)
        except EOFError:
            pass
    return run_time



#def list_users(avl_tree: AVLTree):
    #tree = avl_tree.traverse_tree()
    #for node in tree:
        #stdout.write(node.user.username)
        #for i in range(len(node.user.cards)):
            #stdout.write(" " + node.user.cards[i][0] + " " + node.user.cards[i][1])
        #outln("")
    #outln("FIM")
    



if __name__ == '__main__':
    access_files = ["test_100000_access", "test_200000_access", "test_300000_access", "test_400000_access", "test_500000_access", "test_600000_access", "test_700000_access", "test_800000_access", "test_900000_access", "test_1000000_access"]
    insertion_files = ["test_100000_insertion", "test_200000_insertion", "test_300000_insertion", "test_400000_insertion", "test_500000_insertion", "test_600000_insertion", "test_700000_insertion", "test_800000_insertion", "test_900000_insertion", "test_1000000_insertion"]
    
    num_cases = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    access_times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    insertion_times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(access_files)):
        run_time = main(access_files[i])
        access_times[i] = run_time 
         
    for i in range(len(insertion_files)):
        run_time = main(insertion_files[i])
        insertion_times[i] = run_time


    print("------------ Tempos de acesso ------------")
    for i in range(len(access_times)):
        print("Tempo " + str(num_cases[i]) + " casos: ", end=" ")
        print(access_times[i])

    print("\n")

    print("----------- Tempos de insercao -----------")
    for i in range(len(insertion_times)):
        print("Tempo " + str(num_cases[i]) + " casos: ", end=" ")
        print(insertion_times[i])

        