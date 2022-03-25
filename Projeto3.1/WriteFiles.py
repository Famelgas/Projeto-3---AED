from random import randint, choice

def generate_tests(test_file, num, show=False, lvl=0):
    with open("Words.txt", "r") as file:
        palavras = file.readlines()

    def generate_tests_util(num, show=False, lvl=0):
        temp = []
        while num != 1:
            a = randint(1, num-1)
            num -= a
            temp.append(a)
        # print(p1, sum(p1))
        texto= open(test_file,"a")
        if lvl == 0:
            texto.write(f"Todos {randint(0, 1000)} {len(temp)}\n")
        else:
            texto.write(" "*(lvl*show) + f"{choice(palavras)[:-1]} {randint(0, 1000)} {len(temp)}\n")
        texto.close()
        for i in temp:
            generate_tests_util(i, show, lvl+1)

    generate_tests_util(num, show, lvl)







if __name__=="__main__":
    test_files = ["Test_5000.txt", "Test_10000.txt", "Test_25000.txt", "Test_50000.txt", "Test_75000.txt"]
    test_number = [5000, 10000, 25000, 50000, 75000]
    for f in range(5):
        generate_tests(test_files[f], test_number[f])


