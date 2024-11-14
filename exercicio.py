def mensagem (texto):
    print ("_" *30)
    print (texto)
    print ("_" * 30)
    print ("DIGITE UMA TECLA")
    print ("_"*30, )
    teclas =  ("S D E")
    print (teclas)
    digitar = str (input("Digite uma tecla:"))
    if digitar == "S":
        print ("Você escolheu o método sacar")
    elif digitar == "D":
        print ("Você escolheu o método Depositar")
    elif digitar == "E":
        print ("Você escolheu o método de ver o extrato")
mensagem ("SEJA BEM VINDO AO BANCO!!")
