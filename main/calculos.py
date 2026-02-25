def renda_total(tempo_de_trabalho, salario_mensal_medio):
    return tempo_de_trabalho * 12 * salario_mensal_medio


def percentual_gasto(gasto_total_cartao, renda_total_valor):
    return (gasto_total_cartao / renda_total_valor) * 100 if renda_total_valor > 0 else 0


def meses_salario_equivalente(gasto_total_cartao, salario_mensal_medio):
    return (gasto_total_cartao / salario_mensal_medio) if salario_mensal_medio > 0 else 0


def calcula_score(percentual):
    if percentual < 15:
        return "Baixo"
    elif 15 <= percentual < 25:
        return "Controlado"
    elif 25 <= percentual < 30:
        return "Atenção"
    elif 30 <= percentual < 40:
        return "Alto"
    elif 40 <= percentual < 50:
        return "Crítico"
    else:
        return "Ultra Crítico"