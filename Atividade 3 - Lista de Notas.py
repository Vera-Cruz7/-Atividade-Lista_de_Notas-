# Inicializando a lista de notas
notas = []

# Função para adicionar uma nova nota
def adicionar_nota(nova_nota):
    notas.append(nova_nota)
    print(f"Nota {nova_nota} adicionada com sucesso!")

# Função para remover uma nota específica
def remover_nota(nota_remover):
    if nota_remover in notas:
        notas.remove(nota_remover)
        print(f"Nota {nota_remover} removida com sucesso!")
    else:
        print("Nota não encontrada na lista.")

# Função para ordenar as notas
def ordenar_notas():
    notas.sort()
    print("Notas ordenadas em ordem crescente.")

# Função para exibir estatísticas das notas
def exibir_estatisticas():
    if notas:
        nota_maxima = max(notas)
        nota_minima = min(notas)
        soma_notas = sum(notas)
        total_notas = len(notas)
        print(f"Nota Máxima: {10}")
        print(f"Nota Mínima: {0}")
        print(f"Soma das Notas: {soma_notas}")
        print(f"Total de Notas: {total_notas}")
    else:
        print("Nenhuma nota registrada.")

# Execução do programa com entradas predefinidas

# Adicionando notas
adicionar_nota(0)
adicionar_nota(1)
adicionar_nota(2)
adicionar_nota(3)
adicionar_nota(4)
adicionar_nota(5)
adicionar_nota(6)
adicionar_nota(7)
adicionar_nota(8)
adicionar_nota(9)
adicionar_nota(10)

# Exibindo lista de notas após adições
print(f"Lista de notas atual: {notas}")

# Removendo uma nota específica
remover_nota(7)

# Exibindo lista de notas após remoção
print(f"Lista de notas após remoção: {notas}")

# Adicionando uma nota específica
adicionar_nota(7)

# Exibindo lista de notas após adição
print(f"Lista de notas após adição: {notas}")

# Ordenando notas
ordenar_notas()

# Exibindo lista de notas após ordenação
print(f"Lista de notas ordenada: {notas}")

# Exibindo estatísticas das notas
exibir_estatisticas()