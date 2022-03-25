from sys import stdin, stdout
import time

class Node:
    def __init__(self, nft):
        self.category = nft[0]
        self.value = int(nft[1])
        self.number_nodes = int(nft[2])
        self.children = []
    
    def __repr__(self):
        return f"{self.category}({self.value})"



# ----------------------------- Program ----------------------------



def readln(test_file):
    return test_file.readline().rstrip().split(" ")

def outln(nft):
    stdout.write(str(nft))
    stdout.write("\n")


def populate_tree(root, node, test_file):
    for i in range(int(node[2])):
        nft = readln(test_file)
        root.children.append(Node(nft))
        if int(nft[2]) != 0:
            populate_tree(root.children[i], nft, test_file)



def print_tree(root):
    if root == None:
        return
    
    nfts = []
    nfts.append(root);
    while (len(nfts) != 0):
        level = ""
        root_length = len(nfts)
        while (root_length > 0):
            nft = nfts[0]
            nfts.pop(0);
            level += f"{nft.category}({nft.value}) "
   
            # Enqueue all children of the dequeued item
            for i in range(len(nft.children)):
             
                nfts.append(nft.children[i]);
            root_length -= 1
        level = level.rstrip()
        outln(level)


def calculate_level(root):
    value_sum = 0
    nfts = root.children
    for node in nfts:
        value_sum += calculate_level(node)
    value_sum += root.value
    root.value = value_sum
    return value_sum






def main():

    times = [0, 0, 0, 0, 0]
    test_number = [5000, 10000, 25000, 50000, 75000]
    test_files = ["Test_5000.txt", "Test_10000.txt", "Test_25000.txt", "Test_50000.txt", "Test_75000.txt"]

    for i in range(len(test_number)):
        with open(test_files[i], "r") as test_file:
            temp = readln(test_file)
            root = Node(temp)
            populate_tree(root, temp, test_file)
            
            start_time = time.time()
            calculate_level(root)
            print_tree(root)

            end_time = time.time() - start_time

            times[i] = end_time

    for i in range(len(times)):
        print(f"Tempo para {test_number[i]} linhas: {times[i]}\n")








if __name__ == "__main__":
    main()