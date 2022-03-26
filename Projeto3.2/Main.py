from sys import stdin, stdout

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





def readln():
    return stdin.readline().rstrip().split(" ")


def outln(string):
    stdout.write(string.rstrip() + "\n")




def main():
    splay_tree = SplayTree()
    try:
        while True:
            user_in = readln()
            #start_time = time.time()
            if user_in[0] == "ARTIGO":
                if not splay_tree.find(user_in[1]):
                    splay_tree.insert(user_in[1], user_in[2], user_in[3])
                    outln("NOVO ARTIGO INSERIDO")
                else:
                    outln("ARTIGO JA EXISTENTE")

            elif user_in[0] == "OFERTA":
                if not splay_tree.find(user_in[1]):
                    outln("ARTIGO NAO REGISTADO")
                else:
                    splay_tree.insert_info(user_in[2])
                    outln("OFERTA ATUALIZADA")



            elif user_in[0] == "CONSULTA":
                if not splay_tree.find(user_in[1]):
                    outln("ARTIGO NAO REGISTADO")
                else:
                    node = splay_tree.find(user_in[1])
                    outln(node.nft.name + " " + node.nft.hash_nft + " " + str(node.nft.value))
                    outln("FIM")
                

            elif user_in[0] == "LISTAGEM":
                splay_tree.list_tree(splay_tree.root)

            elif user_in[0] == "APAGA":
                splay_tree.delete_tree()
                outln("CATALOGO APAGADO")
            
            elif user_in[0] == "FIM":
                break
            
            else:
                break
            #run_time += (time.time() - start_time)
    except EOFError:
        pass




if __name__=="__main__":
    main()