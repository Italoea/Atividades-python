import random
import string

def gerar_senha(nivel):
    if nivel == "fraca":
        # Apenas letras minúsculas 6 á 8 caracteres
        caracteres = string.ascii_lowercase
        tamanho = random.randint(6, 8)
    elif nivel == "media":
        # Letras maiúsculas minúsculas e números, 8 á 12 caracteres
        caracteres = string.ascii_letters + string.digits
        tamanho = random.randint(8, 12)
    elif nivel == "forte":
        # Letras maiúsculas, minúsculas, números e símbolos, 12-16 caracteres
        caracteres = string.ascii_letters + string.digits + string.punctuation
        tamanho = random.randint(12, 16)
    else:
        raise ValueError("Nível inválido! Escolha entre 'fraca', 'media' ou 'forte'.")

    # Gerar a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
if __name__ == "__main__":
    print("Escolha o nível de segurança para sua senha:")
    print("1. Fraca")
    print("2. Média")
    print("3. Forte")
    escolha = input("Digite 1, 2 ou 3: ").strip()
    niveis = {"1": "fraca", "2": "media", "3": "forte"}
    nivel_selecionado = niveis.get(escolha)

    if nivel_selecionado:
        senha = gerar_senha(nivel_selecionado)
        print(f"Sua senha {nivel_selecionado} é: {senha}")
    else:
        print("Opção inválida! Tente novamente.")

