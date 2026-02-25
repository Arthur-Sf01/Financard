from questionario import questionario
from calculos import renda_total, percentual_gasto, meses_salario_equivalente, calcula_score
from relatorios import gerar_relatorio

def main():
    
    idade, tempo_de_trabalho, salario_mensal_medio, gasto_total_cartao = questionario()
    
    renda = renda_total(tempo_de_trabalho, salario_mensal_medio)
    pct = percentual_gasto(gasto_total_cartao, renda)
    meses_eq = meses_salario_equivalente(gasto_total_cartao, salario_mensal_medio)
    score = calcula_score(pct)

    print(gerar_relatorio(idade, tempo_de_trabalho, salario_mensal_medio, gasto_total_cartao, renda, pct, meses_eq, score))
    
if __name__ == "__main__":
    main()