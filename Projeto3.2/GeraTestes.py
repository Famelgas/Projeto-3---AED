from os import access
import random
import string


def gera_testes_cenario_1(test_file, num_cases):
    ninssercoes = int(0.4 * num_cases)
    nconsultas = int(0.3 * num_cases)
    nofertas = int(0.3 * num_cases)
    f = open(test_file, "w")
    numcccharacters = string.ascii_lowercase + string.digits
    listanomes = []
    listanomesmais = []
    listanomesmenos = []

    for h in range(ninssercoes):
        linha = 'ARTIGO '
        nome = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        listanomes.append(nome)
        nome += ' '
        hash_nft = ''.join(random.choice(numcccharacters) for _ in range(6))
        hash_nft += ' '
        value = str(random.randint(0, 1000000))
        linha += nome
        linha += hash_nft
        linha += value
        linha += '\n'
        f.write(linha)

    percent = 0
    for i in range(len(listanomes)):
        if percent < int(0.05 * len(listanomes)):
            listanomesmais.append(listanomes[i])
        else:
            listanomesmenos.append(listanomes[i])
        percent += 1


    for h in range(int(0.9 * nconsultas)):
        nome = random.choice(listanomesmais)
        linha = 'CONSULTA '
        linha += nome
        linha += '\n'
        f.write(linha)

    for h in range(int(0.1 * nconsultas)):
        nome = random.choice(listanomesmenos)
        linha = 'CONSULTA '
        linha += nome
        linha += '\n'
        f.write(linha)
    
    for h in range(int(0.9 * nofertas)):
        nome = random.choice(listanomesmais)
        linha = 'OFERTA '
        linha += nome
        value = str(random.randint(0, 1000000))
        linha += value
        linha += '\n'
        f.write(linha)

    for h in range(int(0.1 * nofertas)):
        nome = random.choice(listanomesmenos)
        linha = 'OFERTA '
        linha += nome
        value = str(random.randint(0, 1000000))
        linha += value
        linha += '\n'
        f.write(linha)
    
    f.write('FIM')
    f.close()




def gera_testes_cenario_2(test_file, num_cases):
    ninssercoes = int(0.4 * num_cases)
    nconsultas = int(0.3 * num_cases)
    nofertas = int(0.3 * num_cases)
    f = open(test_file, "w")
    numcccharacters = string.ascii_lowercase + string.digits
    listanomes = []

    for h in range(ninssercoes):
        linha = 'ARTIGO '
        nome = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        listanomes.append(nome)
        nome += ' '
        hash_nft = ''.join(random.choice(numcccharacters) for _ in range(6))
        hash_nft += ' '
        value = str(random.randint(0, 1000000))
        linha += nome
        linha += hash_nft
        linha += value
        linha += '\n'
        f.write(linha)




    for h in range(nconsultas):
        nome = random.choice(listanomes)
        linha = 'CONSULTA '
        linha += nome
        linha += '\n'
        f.write(linha)

    for h in range(nofertas):
        nome = random.choice(listanomes)
        linha = 'OFERTA '
        linha += nome
        value = str(random.randint(0, 1000000))
        linha += value
        linha += '\n'
        f.write(linha)


    
    f.write('FIM')
    f.close()




if __name__=="__main__":
    num_cases = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    cenario_1_files = ["test_100000_cenario_1", "test_200000_cenario_1", "test_300000_cenario_1", "test_400000_cenario_1", "test_500000_cenario_1", "test_600000_cenario_1", "test_700000_cenario_1", "test_800000_cenario_1", "test_900000_cenario_1", "test_1000000_cenario_1"]
    cenario_2_files = ["test_100000_cenario_2", "test_200000_cenario_2", "test_300000_cenario_2", "test_400000_cenario_2", "test_500000_cenario_2", "test_600000_cenario_2", "test_700000_cenario_2", "test_800000_cenario_2", "test_900000_cenario_2", "test_1000000_cenario_2"]
    
    for i in range(len(num_cases)):
        gera_testes_cenario_1(cenario_1_files[i], num_cases[i])
        gera_testes_cenario_2(cenario_2_files[i], num_cases[i])