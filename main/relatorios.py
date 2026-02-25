def gerar_relatorio(idade, anos, salario, gasto_total_cartao, renda, pct, meses_eq, score):
    # Mensagem por score
    if score == "Baixo":
        mensagem = "Seu nível de comprometimento está bem abaixo da média nacional."
    elif score == "Controlado":
        mensagem = "Seu comprometimento está dentro da média observada no Brasil."
    elif score == "Atenção":
        mensagem = "Seu comprometimento está próximo do limite superior da média nacional."
    elif score == "Alto":
        mensagem = "Seu comprometimento está acima da média nacional. Atenção ao planejamento."
    elif score == "Crítico":
        mensagem = "Seu nível de comprometimento é elevado. Recomenda-se revisão financeira."
    else:  # Ultra Crítico
        mensagem = "Seu comprometimento está muito acima do padrão nacional. Risco elevado."

    # Comparação com média nacional (referência Bacen)
    media_nacional = 29.0
    diff_pp = pct - media_nacional

    if diff_pp > 0:
        situacao_media = f"{diff_pp:.2f} p.p. acima"
    elif diff_pp < 0:
        situacao_media = f"{abs(diff_pp):.2f} p.p. abaixo"
    else:
        situacao_media = "igual à média"

    relatorio = f"""===== FINANCARD – RESULTADO =====

Idade: {idade} anos
Renda total acumulada: R$ {renda:,.2f}
Gasto total no cartão: R$ {gasto_total_cartao:,.2f}
Comprometimento equivalente: {pct:.2f}%
Equivalente a: {meses_eq:.1f} meses de salário
Classificação: {score}

--- COMPARAÇÃO BRASIL ---
Referência nacional estimada: ~{media_nacional:.1f}%
Diferença: {situacao_media}

--- ANÁLISE ---
{mensagem}

Referência: comprometimento de renda com dívidas (BCB/SGS 29034)
================================
"""
    return relatorio