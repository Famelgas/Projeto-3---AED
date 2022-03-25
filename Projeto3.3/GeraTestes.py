from os import access
import random
import string


def gera_testes_acesso(test_file, num_cases):
    ninssercoes = int(0.1 * num_cases)
    nacessos = int(0.9 * num_cases)
    f = open(test_file, "w")
    numcccharacters = string.ascii_lowercase + string.digits
    listanomes = []
    for h in range(ninssercoes):
        linha = 'ACRESCENTA '
        nome = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        listanomes.append(nome)
        nome += ' '
        numcc = ''.join(random.choice(numcccharacters) for _ in range(16))
        numcc += ' '
        validade = ''.join(random.choice(string.digits) for _ in range(4))
        linha += nome
        linha += numcc
        linha += validade
        linha += '\n'
        f.write(linha)
    for h in range(nacessos):
        nome = random.choice(listanomes)
        linha = 'CONSULTA '
        linha += nome
        linha += '\n'
        f.write(linha)
    f.write('FIM')
    f.close()

def gera_testes_insercao(test_file, num_cases):
    ninssercoes = int(0.1 * num_cases)
    nacessos = int(0.9 * num_cases)
    f = open(test_file, "w")
    numcccharacters = string.ascii_lowercase + string.digits
    listanomes = []
    for h in range(ninssercoes):
        linha = 'ACRESCENTA '
        nome = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        listanomes.append(nome)
        nome += ' '
        numcc = ''.join(random.choice(numcccharacters) for _ in range(16))
        numcc += ' '
        validade = ''.join(random.choice(string.digits) for _ in range(4))
        linha += nome
        linha += numcc
        linha += validade
        linha += '\n'
        f.write(linha)
    for h in range(nacessos):
        nome = random.choice(listanomes)
        linha = 'CONSULTA '
        linha += nome
        linha += '\n'
        f.write(linha)
    f.write('FIM')
    f.close()



if __name__=="__main__":
    num_cases = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    access_files = ["test_100000_access", "test_200000_access", "test_300000_access", "test_400000_access", "test_500000_access", "test_600000_access", "test_700000_access", "test_800000_access", "test_900000_access", "test_1000000_access"]
    insertion_files = ["test_100000_insertion", "test_200000_insertion", "test_300000_insertion", "test_400000_insertion", "test_500000_insertion", "test_600000_insertion", "test_700000_insertion", "test_800000_insertion", "test_900000_insertion", "test_1000000_insertion"]
    
    for i in range(len(num_cases)):
        gera_testes_acesso(access_files[i], num_cases[i])
        gera_testes_insercao(insertion_files[i], num_cases[i])
