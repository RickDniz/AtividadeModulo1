# # ATIVIDADE LOOPS E FUNÇÃO
#1. Faça um programa que peça números ao usuário até que ele digite 0. Ao final, mostre a soma de todos os números digitados.

soma = 0
numero = -1

while numero != 0:
    numero = int(input("Digite um número (0 para sair): "))
    soma += numero

print("A soma dos números digitados é:", soma)

#2. Crie um programa que peça uma senha ao usuário e só termine quando a senha correta "python123" for digitada.

senha = ""
tentativas = 0

while senha != "python123":
    senha = input("Digite a senha: ")
    tentativas += 1

print(f"Acesso liberado após {tentativas} tentativas.")

#3. Escreva um programa que mostre a tabuada de um número escolhido pelo usuário, de 1 até 10, usando while.
numero = int(input("Digite um número: "))
contador = 1

while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1

#4. Faça um programa que mostre todos os números pares de 1 a 20.

for numero in range(2, 21, 2):
    print(numero)

#5. Escreva um programa que leia 5 números e mostre o maior deles.
maior = None

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))

    if maior is None or numero > maior:
        maior = numero

print("O maior número digitado foi:", maior)

#6. Crie um programa que percorra uma string digitada pelo usuário e conte quantas vogais ela possui.
texto = input("Digite um texto: ").lower()
contador = 0

for letra in texto:
    if letra in "aeiou":
        contador += 1

print("Quantidade de vogais:", contador)

#7. Crie uma função que receba dois números e retorne a soma deles.

def soma(a, b):
    return a + b

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print("Soma:", soma(n1, n2))

#8. Crie uma função que receba um número e retorne True se ele for par e False caso contrário.
def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

#9. Crie uma função que receba uma lista de números e retorne a média deles. def media(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma / len(lista)

#10. Crie uma função chamada saudacao que receba o nome de uma pessoa como parâmetro e exiba a
mensagem: 👉 "Olá, [nome]! Seja bem-vindo(a)!"
def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo(a)!"

print(saudacao("Paulo"))
