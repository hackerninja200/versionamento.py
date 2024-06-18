idades = []
alturas = []

# Pedindo as informações para 5 pessoas
for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    
    # Adicionando idade e altura às listas usando o método .append()
    idades.append(idade)
    alturas.append(altura)

# Imprimindo as idades na ordem inversa
print("\nIdades na ordem inversa:")
for idade in reversed(idades):
    print(idade)

# Imprimindo as alturas na ordem inversa
print("\nAlturas na ordem inversa:")
for altura in reversed(alturas):
    print(altura)
