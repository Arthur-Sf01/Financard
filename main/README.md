# FinanCard – Analisador de Gastos no Cartão (CLI)

FinanCard é uma ferramenta em Python (terminal) que estima o **comprometimento de renda** a partir do gasto no cartão de crédito e entrega um relatório com classificação de risco e comparação com um indicador brasileiro de referência.

## O que o FinanCard calcula
Com base nas informações inseridas pelo usuário, o sistema calcula:

- **Renda total acumulada**: anos_trabalhados × 12 × salário_mensal_médio
- **Comprometimento equivalente (%)**: (gasto_total_cartão ÷ renda_total_acumulada) × 100
- **Meses de salário equivalentes**: gasto_total_cartão ÷ salário_mensal_médio
- **Score (string)**: Baixo / Controlado / Atenção / Alto / Crítico / Ultra Crítico

> Observação: esta versão (v1) trabalha com um modelo simples e serve como estimativa inicial.

## Referência socioeconômica (Brasil)
As faixas e o texto de análise usam como base o conceito de **comprometimento de renda com dívidas**, tomando como referência o indicador do Banco Central do Brasil:

- **BCB/SGS 29034 – Comprometimento de renda das famílias com o serviço da dívida**

O relatório também mostra a diferença (em pontos percentuais) em relação a um patamar nacional de referência.

## Faixas de classificação (v1)
- < 15% → **Baixo**
- 15% a < 25% → **Controlado**
- 25% a < 30% → **Atenção**
- 30% a < 40% → **Alto**
- 40% a < 50% → **Crítico**
- ≥ 50% → **Ultra Crítico**

## Exemplo de saída


===== FINANCARD – RESULTADO =====
...
Comprometimento equivalente: 50.00%
Classificação: Ultra Crítico
...
--- COMPARAÇÃO BRASIL ---
Referência nacional estimada: ~29.0%
Diferença: 21.00 p.p. acima
...

## ▶️ Como executar
No terminal, dentro da pasta do projeto:

```bash
python main.py

