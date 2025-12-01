from calculos.impostos import calcular_irpf

salario = 3000
irpf = calcular_irpf(salario)

print(f"O IRPF para um salário de R$ {salario:.2f} é: R$ {irpf:.2f}")

