import random # importei a bibioteca random

palavra = random.choice([ "casa", "carro", "floresta", "rio", "montanha", "cidade", "livro", "escola", "computador", "janela",
    "porta", "mesa", "cadeira", "amigo", "sol", "lua", "estrela", "vento", "chuva", "tempo",
    "relógio", "chave", "telefone", "papel", "caneta", "viagem", "praia", "mundo", "água", "fogo",
    "terra", "ar", "animais", "fruta", "planta", "flor", "árvore", "pessoa", "família", "amor",
    "amizade", "história", "poema", "musica", "filme", "arte", "foto", "natureza", "mar", "lago",
    "passado", "presente", "futuro", "memória", "vida", "saúde", "doença", "dor", "remédio", "sorriso",
    "lágrima", "alegria", "tristeza", "medo", "sonho", "pesadelo", "esperança", "fé", "paz", "guerra",
    "luta", "vitória", "derrota", "corrida", "jogo", "esporte", "trabalho", "dinheiro", "férias", "tempo",
    "energia", "força", "luz", "sombra", "mistério", "segredo", "verdade", "mentira", "sabedoria", "inteligência",
    "conhecimento", "ciência", "tecnologia", "futebol", "basquete", "volei", "comida", "bebida", "doce", "sal",
    "pimenta", "arroz", "feijão", "pizza", "chocolate", "bolo"
]) # inseri palavras em uma lista
letras_usuario = [ ] # criei uma cariavel para as letras que o usuario digitar ser inseridas.
chances = 10 # limitei as chances 
ganhou_jogo = False # coloquei uma variavel para mostrar se a pessoa ganhou ou perdeu

while True:
    for letra in palavra: # percorre cada letra da palavra
        if letra.lower() in letras_usuario:
            print (letra, end=" ")
        else:
            print ("_", end= " ")

    print ( f"Você tem {chances} chances")

    tentativa = input ("Escolha uma letra:")

    letras_usuario.append(tentativa.lower())

    if tentativa.lower () not in palavra.lower(): # se a letra inserida não tiver na palavra, o jogador irá perder uma chance.
        chances -=1

    ganhou = True
    for letra in palavra:
        if letra.lower()not in letras_usuario:
            ganhou = False

    if chances ==0 or ganhou: # se as chances se esgotarem o jogo para e se o jogador ganhar irá parar também.

        break

if ganhou: # Condição para mostrar se o jogador ganhou ou não
   print (f" ========== Parabens você ganhou!!!A palavra era: {palavra} ========== ")
else:
   print (f" ---------- você perdeu :( A palavra era: {palavra} ---------- ")
