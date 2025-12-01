# 3) Crie uma estrutura de pacote chamada 'calculos' contendo um módulo 'impostos.py'. Dentro de 'impostos.py', 
# defina uma função 'calcular_irpf(salario)' que retorna 15% do salário (apenas um exemplo simples). 
# Certifique-se de que o diretório 'calculos' contenha o arquivo '__init__.py'. Em um arquivo fora do pacote (no mesmo nível), 
# chamado 'folha_pagamento.py', importe a função 'calcular_irpf' de 'calculos.impostos' e use-a para calcular e imprimir o IRPF para um salário de 3000.

def calcular_irpf(salario):
    return salario * 0.15
