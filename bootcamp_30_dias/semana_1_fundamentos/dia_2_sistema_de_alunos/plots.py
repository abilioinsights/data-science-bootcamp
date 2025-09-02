import matplotlib.pyplot as plt

def grafico_histograma(matriz):
    """
    Plota um histograma das notas de todos os alunos.
    """
    plt.hist(matriz.flatten(), bins=10, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title("Distribuição das Notas")
    plt.xlabel("Nota")
    plt.ylabel("Quantidade")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def grafico_barras(media):
    """
    Plota um gráfico de barras da média por disciplina.
    """
    disciplinas = ["Matemática", "Física", "Programação"]
    plt.bar(disciplinas, media, color='orange', edgecolor='black', alpha=0.8)
    plt.title("Média por Disciplina")
    plt.ylabel("Média")
    plt.ylim(0, 10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
