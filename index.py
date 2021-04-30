# EXEMPLO 1:
def standardize_names(character_name):
    character_name = character_name.strip()
    if ' ' in character_name.strip():
        character_name = character_name.replace(' ', '-')
    return character_name

hero_standardized = standardize_names(" Batman     ")
print(hero_standardized)
# esperado Batman
hero_standardized = standardize_names("      Super Man")
print(hero_standardized)
# esperado Super-Man


def standardize_title(title):
    return title.title()

title = standardize_title("cinco quartos de laranja")
print(title)
# esperado Cinco Quartos De Laranja



def standardize_text(text):
    return ". ".join(i.capitalize() for i in text.split(". "))

text = """a famosa atriz Constance Rattigan recebe uma encomenda desagradável: uma lista com números de
telefone de pessoas que morreram recentemente. é uma coisa assustadora, considerando que os nomes das
poucas pessoas vivas presentes na lista estão assinalados em vermelho com
uma cruz. O da própria Constance é um deles."""

normalized_text = standardize_text(text)
print(normalized_text)

# > A famosa atriz Constance Rattigan recebe uma encomenda desagradável: uma 
# lista com números de telefone de pessoas que morreram recentemente. É uma 
# coisa assustadora, considerando que os nomes das poucas pessoas vivas presentes
# na lista estão assinalados em vermelho com uma cruz. O da própria Constance é um deles.


def title_creator(text):
    i = 1
    # coloque quantos tracos quiser hahahaha
    while i < 20: 
        text = '-'+ text + '-'
        i += 1
    return text.title()

text = "pense num deserto"
title = title_creator(text)

print(title)
# 20 - direita  e 20 - a esquerda
# --------------------Pense Num Deserto--------------------



def text_merge(text_of_blog_a, text_of_blog_b):
    texto = text_of_blog_a + text_of_blog_b
    texto = texto.strip()
    texto = " ".join(texto.split())
    return ". ".join(i.capitalize() for i in texto.split(". "))

        # return ". ".join(i.capitalize() for i in text.split(". "))


text_of_blog_a = """
na Londres do pós-guerra, a escritora     Juliet tenta encontrar uma   trama para seu novo livro. ela 
recebe ajuda por meio de uma     carta de um      desconhecido, um nativo da ilha de Guernsey, 
em cujas mãos havia chegado um livro    que há tempos tinha pertencido    a Juliet.
"""
text_of_blog_b = """
O romance "Cinco Quartos de Laranja" é como   um vinho intenso e delicado.    usando metáforas
culinárias, personagens peculiares   e acontecimentos sobrenaturais,      Harris cria uma história
complexa e      bela ao mesmo tempo.
"""

merged_text = text_merge(text_of_blog_a, text_of_blog_b)

print(merged_text)

# > Na Londres do pós-guerra, a escritora Juliet tenta encontrar uma trama para seu novo livro. Ela 
# recebe ajuda por meio de uma carta de um desconhecido, um nativo da ilha de Guernsey, em cujas
# mãos havia chegado um livro que há tempos tinha pertencido a Juliet o romance 
# "Cinco Quartos de Laranja" é como um vinho intenso e delicado. Usando metáforas culinárias, 
# personagens peculiares e acontecimentos sobrenaturais, Harris cria uma história complexa e bela
# ao mesmo tempo.

