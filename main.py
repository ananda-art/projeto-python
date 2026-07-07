print("Sistema de verificação de idade")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Mensagens personalizadas baseadas na idade
if idade < 0:
    print("Idade inválida.")
elif idade >= 18:
    print(f"Olá, {nome}! Você é maior de idade. Seja bem-vindo ao sistema!")
else:
    print(f"Olá, {nome}! Você é menor de idade. Seu acesso foi restrito.")

