from random import randint

print("__________ JOGO DA FORCA __________")

words = ["livro","caneta","garfo","panela","mesa","cama","microfone","celular","martelo","bolsa","criança","menina",
         "garoto","pai","mãe","homem","mulher","professor","médica","estudante","ator","empresário","cachorro","gato",
         "cavalo","tigre","papagaio","mico","capivara","palmeira","roseira","samambaia","capim","coqueiro","girassol",
        ]

random = randint(0,len(words)-1) # escolhe uma palavra
word = list(words[random])
c_letter = []
w_letter = []
s_word=list('-' * len(word))
vida = 10
fim = False

while not fim:
    print("\n\n----- ----- -----")

    print(f"Letras restantes: {len(word)}\nTentativas restantes: {life}")
    print(f"Acertos: {c_letter}\nErros:   {w_letter}")

    print(f"\nPalavra sercreta: ", end="")
    for n in s_word:print(f"{n}",end="")

    letter = str(input("\nDigite uma letra: "))

    if letter in word: # Verifica se a letra digitada tem na palavra
        if not letter in c_letter:
            c_letter.append(letter)
        for i in range(0, len(word)):
            if letter == word[i]:
                s_word[i] = word[i]
    else:
        if not letter in w_letter:
            w_letter.append(letter)
            life = life - 1


    if word == s_word: # Se apalavra for a certa
        print("---------- Parabéns, você ganhou. ----------")
        print("A palavra é: ", end="")
        for n in word: print(f"{n}", end="")
        end = True
    elif life == 0: # se as vidas acabarem
        print("---------- Que pena, você perdeu. ----------")
        print("A palavra era: ", end="")
        for n in word: print(f"{n}", end="")
        end = True