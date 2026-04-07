import random

# ---- Questao 1 ---- Calculadora de Operacoes Simples ----
def questao1():
    print("\n=== Calculadora de Operações Simples ===")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                print("Erro: não é possível dividir por zero.")
                return
            resultado = num1 / num2
        else:
            print("Operação inválida. Use +, -, * ou /.")
            return

        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
    except ValueError:
        print("Entrada inválida. Digite números válidos.")


# ---- Questao 2 ---- Jogo de Adivinhacao ----
def questao2():
    print("\n=== Jogo de Adivinhação ===")
    numero_secreto = random.randint(1, 50)
    print("Tentei um número entre 1 e 50. Você tem 5 tentativas!")

    for tentativa in range(1, 6):
        try:
            palpite = int(input(f"Tentativa {tentativa}/5 - Digite seu palpite: "))
        except ValueError:
            print("Entrada inválida. Você perdeu esta tentativa.")
            continue

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto}!")
            return
        elif palpite < numero_secreto:
            print("Seu palpite está abaixo do número sorteado.")
        else:
            print("Seu palpite está acima do número sorteado.")

    print(f"Suas tentativas acabaram! O número era {numero_secreto}.")


# ---- Questao 3 ---- Contador de Numeros Pares e Impares ----
def questao3():
    print("\n=== Contador de Números Pares e Ímpares ===")
    pares = 0
    impares = 0

    for i in range(1, 11):
        try:
            numero = int(input(f"Digite o {i}º número: "))
        except ValueError:
            print("Entrada inválida. Considerando como zero.")
            numero = 0

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"\nQuantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")


# ---- Questao 4 ---- Calculo de Media de Notas com Aprovacao ----
def questao4():
    print("\n=== Cálculo de Média de Notas com Aprovação ===")
    try:
        quantidade = int(input("Digite a quantidade de notas: "))
    except ValueError:
        print("Entrada inválida para a quantidade. Encerrando.")
        return

    soma = 0
    for i in range(1, quantidade + 1):
        try:
            nota = float(input(f"Digite a nota {i}: "))
        except ValueError:
            print("Entrada inválida. Considerando nota como zero.")
            nota = 0
        soma += nota

    media = soma / quantidade if quantidade > 0 else 0
    print(f"\nMédia: {media:.2f}")
    if media >= 7:
        print("Situação: Aprovado!")
    else:
        print("Situação: Reprovado.")


# ---- Questao 5 ---- Calculadora de Desconto ----
def questao5():
    print("\n=== Calculadora de Desconto ===")
    try:
        preco = float(input("Digite o preço do produto: "))
        percentual = float(input("Digite o percentual de desconto: "))
        desconto = preco * (percentual / 100)
        preco_final = preco - desconto
        print(f"Valor do desconto: R${desconto:.2f}")
        print(f"Preço final: R${preco_final:.2f}")
    except ValueError:
        print("Entrada inválida. Digite valores numéricos.")


# ---- Questao 6 ---- Conversor de Unidades Simples ----
def questao6():
    print("\n=== Conversor de Unidades Simples ===")
    print("1 - Converter metros para centímetros")
    print("2 - Converter quilômetros para metros")
    opcao = input("Escolha uma opção (1 ou 2): ")

    if opcao == "1":
        try:
            valor = float(input("Digite o valor em metros: "))
            resultado = valor * 100
            print(f"{valor} metros = {resultado} centímetros")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico.")
    elif opcao == "2":
        try:
            valor = float(input("Digite o valor em quilômetros: "))
            resultado = valor * 1000
            print(f"{valor} quilômetros = {resultado} metros")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico.")
    else:
        print("Opção inválida. Escolha 1 ou 2.")


# ---- Questao 7 ---- Verificador de Sinal com Contador ----
def questao7():
    print("\n=== Verificador de Sinal com Contador ===")
    print('Digite números continuamente. Digite "sair" para encerrar.')
    positivos = 0
    negativos = 0
    zeros = 0

    while True:
        entrada = input("Digite um número (ou 'sair'): ")
        if entrada.lower() == "sair":
            break
        try:
            numero = float(entrada)
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            zeros += 1

    print(f"\nPositivos: {positivos}")
    print(f"Negativos: {negativos}")
    print(f"Zeros: {zeros}")


# ---- Questao 8 ---- Calculo de Area e Perimetro de um Retangulo ----
def questao8():
    print("\n=== Cálculo de Área e Perímetro de um Retângulo ===")
    try:
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = largura * altura
        perimetro = 2 * (largura + altura)
        print(f"Área: {area:.2f}")
        print(f"Perímetro: {perimetro:.2f}")
    except ValueError:
        print("Entrada inválida. Digite valores numéricos.")


# ---- Questao 9 ---- Conversao de Idade para Dias, Semanas e Meses ----
def questao9():
    print("\n=== Conversão de Idade para Dias, Semanas e Meses ===")
    try:
        idade = int(input("Digite sua idade em anos: "))
        dias = idade * 365
        semanas = idade * 52
        meses = idade * 12
        print(f"Você já viveu aproximadamente:")
        print(f"  {dias} dias")
        print(f"  {semanas} semanas")
        print(f"  {meses} meses")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


# ---- Questao 10 ---- Simulador de Conta Bancaria Simples ----
def questao10():
    print("\n=== Simulador de Conta Bancária Simples ===")
    try:
        saldo = float(input("Digite o saldo inicial: "))
        deposito = float(input("Digite o valor do depósito: "))
        saque = float(input("Digite o valor do saque: "))

        saldo += deposito

        if saque > saldo:
            print("Erro: saldo insuficiente para realizar o saque.")
            print(f"Saldo atual (após depósito): R${saldo:.2f}")
        else:
            saldo -= saque
            print(f"Saldo final: R${saldo:.2f}")
    except ValueError:
        print("Entrada inválida. Digite valores numéricos.")


# ---- Menu Principal ----
def menu():
    while True:
        print("\n" + "=" * 50)
        print("  TRABALHO 02 - Álgebra e Algoritmos")
        print("=" * 50)
        print("1  - Calculadora de Operações Simples")
        print("2  - Jogo de Adivinhação")
        print("3  - Contador de Números Pares e Ímpares")
        print("4  - Cálculo de Média de Notas com Aprovação")
        print("5  - Calculadora de Desconto")
        print("6  - Conversor de Unidades Simples")
        print("7  - Verificador de Sinal com Contador")
        print("8  - Cálculo de Área e Perímetro de um Retângulo")
        print("9  - Conversão de Idade para Dias, Semanas e Meses")
        print("10 - Simulador de Conta Bancária Simples")
        print("0  - Sair")
        print("=" * 50)

        opcao = input("Escolha um exercício (0-10): ")

        if opcao == "1":
            questao1()
        elif opcao == "2":
            questao2()
        elif opcao == "3":
            questao3()
        elif opcao == "4":
            questao4()
        elif opcao == "5":
            questao5()
        elif opcao == "6":
            questao6()
        elif opcao == "7":
            questao7()
        elif opcao == "8":
            questao8()
        elif opcao == "9":
            questao9()
        elif opcao == "10":
            questao10()
        elif opcao == "0":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Escolha entre 0 e 10.")


if __name__ == "__main__":
    menu()
