from random import randint, choice


def generate_tests(num, show=False, lvl=0):
    with open("words", "r") as file:
        palavras = file.readlines()

    def generate_tests_util(num, show=False, lvl=0):
        temp = []
        while num != 1:
            a = randint(1, num-1)
            num -= a
            temp.append(a)
        # print(p1, sum(p1))
        texto= open("C:/Users\WRT511\PycharmProjects\pythonProject2\exemplo.txt","a")
        if lvl == 0:
            texto.write(f"Todos {randint(0, 1000)} {len(temp)}\n")
        else:
            texto.write(" "*(lvl*show) + f"{choice(palavras)[:-1]} {randint(0, 1000)} {len(temp)}\n")
        texto.close()
        for i in temp:
            generate_tests_util(i, show, lvl+1)

    generate_tests_util(num, show, lvl)




generate_tests(10000)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
Todos 0 3
Arte 5 2
Classica 1000 0
Fotografia 50 0
Livros 100 0
Musica 0 3
Rock 20 1
SoftRock 5 0
Pop 20 0
Country 20 0
Todos(1220)
Arte(1055) Livros(100) Musica(65)
Classica(1000) Fotografia(50) Rock(25) Pop(20) Country(20)
SoftRock(5)
"""