from sys import stdin, stdout
import time

class NFT:
    def __init__(self, name, hash_nft, value):
        self.name = name
        self.hash_nft = hash_nft
        self.value = value

class Node:
    def __init__(self, name, hash_nft, value):
        self.nft = NFT(name, hash_nft, value)
        self.left = self.right = None


class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None, None, None) #For splay()

    def insert(self, name, hash_nft, value):
        if (self.root == None):
            self.root = Node(name, hash_nft, value)
            return

        self.splay(name)
        if self.root.nft.name == name:
            # If the name is already there in the tree, don't do anything.
            return

        n = Node(name, hash_nft, value)
        if name < self.root.nft.name:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def insert_info(self, value):
        self.root.nft.value = value

  
    def find(self, name):
        if self.root == None:
            return None
        self.splay(name)
        if self.root.nft.name != name:
            return None
        return self.root


    def list_tree(self, node):
        if node != None:
            self.list_tree(node.left)
            outln(node.nft.name + " " + node.nft.hash_nft + " " + str(node.nft.value))
            self.list_tree(node.right)
    

    def delete_tree(self):
        self.root = None

    
    def splay(self, name):
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if name < t.nft.name:
                if t.left == None:
                    break
                if name < t.left.nft.name:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif name > t.nft.name:
                if t.right == None:
                    break
                if name > t.right.nft.name:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t






# --------- funtions ---------





def readln(file):
    return file.readline().rstrip().split(" ")


def outln(string):
    stdout.write(string.rstrip() + "\n")




def main(test_file):
    splay_tree = SplayTree()
    user_in = [""]
    run_time = 0

    with open(test_file, "r") as file:
        try:
            while True:
                user_in = readln(file)
                start_time = time.time()
                if user_in[0] == "ARTIGO":
                    if not splay_tree.find(user_in[1]):
                        splay_tree.insert(user_in[1], user_in[2], user_in[3])
                        #outln("NOVO ARTIGO INSERIDO")
                    else:
                        pass
                        #outln("ARTIGO JA EXISTENTE")

                elif user_in[0] == "OFERTA":
                    if not splay_tree.find(user_in[1]):
                        pass
                        #outln("ARTIGO NAO REGISTADO")
                    else:
                        splay_tree.insert_info(user_in[2])
                        #outln("OFERTA ATUALIZADA")



                elif user_in[0] == "CONSULTA":
                    if not splay_tree.find(user_in[1]):
                        pass
                        #outln("ARTIGO NAO REGISTADO")
                    else:
                        node = splay_tree.find(user_in[1])
                        #outln(node.nft.name + " " + node.nft.hash_nft + " " + str(node.nft.value))
                        #outln("FIM")
                    

                elif user_in[0] == "LISTAGEM":
                    splay_tree.list_tree(splay_tree.root)
                    #outln("FIM")

                elif user_in[0] == "APAGA":
                    splay_tree.delete_tree()
                    #outln("CATALOGO APAGADO")
                
                elif user_in[0] == "FIM":
                    break
                
                else:
                    break
                run_time += (time.time() - start_time)
        except EOFError:
            pass
    return run_time



if __name__=="__main__":
    num_cases = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    cenario_1_files = ["test_100000_cenario_1", "test_200000_cenario_1", "test_300000_cenario_1", "test_400000_cenario_1", "test_500000_cenario_1", "test_600000_cenario_1", "test_700000_cenario_1", "test_800000_cenario_1", "test_900000_cenario_1", "test_1000000_cenario_1"]
    cenario_2_files = ["test_100000_cenario_2", "test_200000_cenario_2", "test_300000_cenario_2", "test_400000_cenario_2", "test_500000_cenario_2", "test_600000_cenario_2", "test_700000_cenario_2", "test_800000_cenario_2", "test_900000_cenario_2", "test_1000000_cenario_2"]


    cenario_1_times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cenario_2_times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(cenario_1_files)):
        run_time = main(cenario_1_files[i])
        cenario_1_times[i] = run_time 
         
    for i in range(len(cenario_2_files)):
        run_time = main(cenario_2_files[i])
        cenario_2_times[i] = run_time


    print("------------ Tempos Cenário 1 ------------")
    for i in range(len(cenario_1_times)):
        print("Tempo " + str(num_cases[i]) + " casos: ", end=" ")
        print(cenario_1_times[i])

    print("\n")

    print("----------- Tempos Cenário 2 ------------")
    for i in range(len(cenario_2_times)):
        print("Tempo " + str(num_cases[i]) + " casos: ", end=" ")
        print(cenario_2_times[i])


