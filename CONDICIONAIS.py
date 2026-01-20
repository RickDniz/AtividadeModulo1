#1. Peça um número e diga se ele é positivo.
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
else:
    print("O número não é positivo.")


#2. Peça a idade e informe se é maior de idade ou menor de idade.
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


#3. Peça uma nota (0 a 10) e informe: Aprovado (>= 7), Recuperação (5 a 6.9) ou Reprovado (< 5).
nota = float(input("Digite a nota (0 a 10): "))

if nota < 0 or nota > 10:
    print("Nota inválida.")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")


#4. Peça um número e verifique: se é positivo, se é par e se é múltiplo de 5.

numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
else:
    print("O número não é positivo.")

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

if numero % 5 == 0:
    print("O número é múltiplo de 5.")
else:
    print("O número não é múltiplo de 5.")


#5. Peça a cor do semáforo (verde, amarelo, vermelho) e exiba a ação correspondente.
cor = input("Digite a cor do semáforo (verde, amarelo, vermelho): ").lower()

if cor == "verde":
    print("Siga")
elif cor == "amarelo":
    print("Atenção")
elif cor == "vermelho":
    print("Pare")
else:
    print("Cor inválida")


#6. Peça a idade e, se for maior de idade, pergunte se tem habilitação (sim/não) e diga se pode dirigir.

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você não pode dirigir.")
else:
    habilitacao = input("Você tem habilitação? (sim/não): ").strip().lower()

    if habilitacao == "sim":
        print("Você pode dirigir.")
    elif habilitacao == "não" or habilitacao == "nao":
        print("Você não pode dirigir.")
    else:
        print("Resposta inválida.")


#7. Peça um número e mostre 'Par' ou 'Ímpar' usando apenas uma linha de código.

print("Par" if int(input("Digite um número: ")) % 2 == 0 else "Ímpar")


#8.Peça um número e diga se ele está entre 10 e 20 (inclusive).
numero = int(input("Digite um número: "))

if 10 <= numero <= 20:
    print("O número está entre 10 e 20.")
else:
    print("O número não está entre 10 e 20.")


#9.Peça três números e diga qual é o maior.
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a >= b and a >= c:
    print(f"O maior número é {a}")
elif b >= a and b >= c:
    print(f"O maior número é {b}")
else:
    print(f"O maior número é {c}")


#10.Peça usuário e senha. Se forem 'admin' e '1234', exiba 'Acesso permitido', caso contrário 'Acesso
negado'
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")
