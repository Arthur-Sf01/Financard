def questionario():

    while True:
        try:
            idade = int(input("Qual a sua idade? "))
            if idade < 16:
                print("No Brasil, a idade mínima para trabalhar é 16 anos.")
                continue
            break
        except ValueError:
            print("Digite um número inteiro válido para a idade.")

    while True:
        try:
            tempo_de_trabalho = int(input("Há quantos anos você trabalha? "))
            if tempo_de_trabalho <= 0:
                print("Informe um valor positivo.")
                continue
            break
        except ValueError:
            print("Digite um número inteiro válido para o tempo de trabalho.")

    while True:
        try:
            salario_mensal_medio = float(input("Qual a sua média salarial mensal nesses anos? "))
            if salario_mensal_medio <= 0:
                print("Informe um valor positivo de salário.")
                continue
            break
        except ValueError:
            print("Digite um número válido para o salário (ex: 2500.50).")

    while True:
        try:
            gasto_total_cartao = float(input("Qual o valor total gasto em todos os seus cartões? "))
            if gasto_total_cartao < 0:
                print("Gasto não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Digite um número válido para o gasto (ex: 1000.00).")

    return idade, tempo_de_trabalho, salario_mensal_medio, gasto_total_cartao
