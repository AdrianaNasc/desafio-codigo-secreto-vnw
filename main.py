#Restaurando as Regras Escolares (Missão 1)

nota = float(input("Digite a nota do aluno: "))
if nota >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
#--------------------------------

#O Sistema Eleitoral Secreto (Missão 2)

idade = 16
if idade >= 16:
    print("Você pode votar!")
else:
    print("Você ainda não pode votar!")
#--------------------------------

#Recuperando o Sistema de Notas (Missão 3)

nota = float(input("Digite a nota do aluno: "))
if 90 <= nota <= 100:
    print("Parabéns, você tirou nota A!")
elif 80 <= nota < 90:
    print("Muito bem, você tirou nota B.")
elif 70 <= nota < 80:
    print("Bom trabalho, você tirou nota C.")
elif 60 <= nota < 70:
    print("Fique atento, você tirou nota D.")
else:
    print("Estude um pouco mais, você tirou nota F!")
#---------------------------------

#Restaurando a Identificação de Números (Missão 4)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é {soma}.")
#---------------------------------

#Recuperando o Cofre de Segurança (Missão 5)

senha_acesso = "Python123"
senha_usuario = input("Digite a senha: ")
if senha_usuario == senha_acesso:
    print("Acesso concedido!")
else:
    print("Senha incorreta! Acesso negado.")
#---------------------------------

#Reforçando a Segurança e a Contagem do Sistema (Missão 6)

contador = 1
while contador <= 10:
    print(contador)
    contador += 1
#---------------------------------

#Organizando a Lista (Missão 7)

numeros = [8, 3, 10, 1, 5]
numeros_ordenados = sorted(numeros)
print("Os números em ordem crescente são:", numeros_ordenados)
#---------------------------------

#Acessando os Registros de Alunos (Missão 8)

nomes = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
primeiro_nome = nomes[0]
print("O primeiro nome é:", primeiro_nome)
ultimo_nome = nomes[-1]
print("O último nome é:", ultimo_nome)
#---------------------------------

#Calculando Dobro de um Número (Missão 9)

def dobro(numero):
    return numero * 2
numero = 5
resultado = dobro(numero)
print(f"O dobro de {numero} é {resultado}.")
#---------------------------------

#Contando Letras (Missão 10)

def contar_letras(nome):
    return len(nome)
nome = "Ana"
quantidade_letras = contar_letras(nome)
print(f"O nome {nome} tem {quantidade_letras} letras.")