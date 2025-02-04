import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def dividir_valor(valor, percentual):
    if percentual < 0 or percentual > 100:
        raise ValueError("O percentual deve estar entre 0 e 100.")
    
    parte1 = (percentual / 100) * valor
    parte2 = valor - parte1
    
    return parte1, parte2

# Exemplo de uso
valor = float(input("Digite o valor total (R$): ").replace(',', '.'))
percentual = float(input("Digite o percentual para a primeira parte: ").replace(',', '.'))

parte1, parte2 = dividir_valor(valor, percentual)

print(f"Valor total: {locale.currency(valor, grouping=True)}")
print(f"{percentual}% do valor: {locale.currency(parte1, grouping=True)}")
print(f"{100 - percentual}% do valor: {locale.currency(parte2, grouping=True)}")