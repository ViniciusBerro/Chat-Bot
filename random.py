import random


def random_string():
    random_list = [
        "Desculpa mas não entendi",
        "Desculpa, mas so respondo sobre o pila verde",
        "Desculpe, acabei nao entendendo.",
        "Perdao, nao consigo lhe dar uma resposta no momento.",
        "Uma resposta sobre sua pergunta e foge do meu banco de dados, tente usar termos como Pila Verde ou Pila Azul."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]