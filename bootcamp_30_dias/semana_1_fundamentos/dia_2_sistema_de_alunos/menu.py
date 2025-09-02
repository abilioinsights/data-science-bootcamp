from core.aluno import Aluno
from core.turma import Turma
import numpy as np
from plots import grafico_histograma, grafico_barras

class Menu:
    def __init__(self, turma):
        self.turma = turma
        self.opcoes = [
            (self.submenu_alunos, "Gerenciar alunos"),
            (self.submenu_turma, "Gerenciar Turmas"),
            (self.sair, "Encerrar programa")
        ]

    def exibir(self):
        while True:
            print("\n--- MENU ---")
            for i, (_, descricao) in enumerate(self.opcoes, start=1):
                print(f"{i}. {descricao}")
            opcao = input("\nEscolha uma opção: ")

            if opcao.isdigit():
                idx = int(opcao) - 1
                if 0 <= idx < len(self.opcoes):
                    funcao, _ = self.opcoes[idx]
                    funcao()
                    continue
            print("Opção inválida. Tente novamente.")

    def submenu_alunos(self):
        while True:
            print("\n--- SUBMENU: GERENCIAR ALUNOS ---")
            opcoes = [
                (self.adicionar_aluno, "Adicionar aluno"),
                (self.listar_alunos, "Listar alunos"),
                (self.atualizar_aluno, "Atualizar aluno"),
                (self.remover_aluno, "Remover aluno"),
                (self.mostrar_aprovados, "Listar alunos aprovados"),
                (self.mostrar_reprovados, "Listar alunos reprovados"),
                (None, "Voltar ao menu principal")
            ]
            for i, (_, descricao) in enumerate(opcoes, start=1):
                print(f"{i}. {descricao}")
            escolha = input("\nEscolha uma opção: ")
            try:
                escolha = int(escolha)
                if escolha == len(opcoes):  # Voltar
                    break
                funcao, _ = opcoes[escolha-1]
                funcao()
            except (ValueError, IndexError):
                print("Opção inválida.")

    def submenu_turma(self):
        while True:
            print("\n--- SUBMENU: GERENCIAR TURMA ---")
            opcoes = [
                (self.mostrar_estatisticas, "Mostrar estatísticas da turma"),
                (self.mostrar_melhor_aluno, "Exibir melhor aluno"),
                (self.mostrar_aprovados, "Listar alunos aprovados"),
                (self.mostrar_reprovados, "Listar alunos reprovados"),
                (self.mostrar_notas_normalizadas, "Notas normalizadas (0 a 1)"),
                (self.mostrar_notas_ponderadas, "Notas ponderadas por disciplina"),
                (self.mostrar_estatisticas_avancadas, "Estatísticas avançadas"),
                (self.gerar_graficos, "Gerar gráficos de desempenho"),
                (None, "Voltar ao menu principal")
            ]
            for i, (_, descricao) in enumerate(opcoes, start=1):
                print(f"{i}. {descricao}")
            escolha = input("\nEscolha uma opção: ")
            try:
                escolha = int(escolha)
                if escolha == len(opcoes):
                    break
                funcao, _ = opcoes[escolha-1]
                funcao()
            except (ValueError, IndexError):
                print("Opção inválida.")

    def adicionar_aluno(self):
        nome = input("Nome do aluno: ")
        while True:
            try:
                notas = list(map(float, input("Digite as 3 notas separadas por espaço: ").split()))
                if len(notas) != 3:
                    raise ValueError
                break
            except ValueError:
                print("Erro: digite exatamente 3 números válidos.")
        aluno = Aluno(nome, notas)
        self.turma.adicionar_aluno(aluno)

    def listar_alunos(self):
        self.turma.listar_alunos()

    def atualizar_aluno(self):
        nome = input("Nome do aluno a atualizar: ")
        while True:
            try:
                notas = list(map(float, input("Digite as 3 novas notas separadas por espaço: ").split()))
                if len(notas) != 3:
                    raise ValueError
                break
            except ValueError:
                print("Erro: digite exatamente 3 números válidos.")
        self.turma.atualizar_aluno(nome, notas)

    def remover_aluno(self):
        nome = input("Nome do aluno a remover: ")
        self.turma.remover_aluno(nome)

    def mostrar_estatisticas(self):
        media = self.turma.media_da_turma()
        if media is None:
            print("Não há alunos cadastrados.")
        else:
            print(f"Média da turma: {media:.2f}")
            print("Média por disciplina:", np.round(self.turma.media_por_disciplina(), 2))

    def mostrar_melhor_aluno(self):
        melhor = self.turma.melhor_aluno()
        if melhor:
            print("Melhor aluno:", melhor)
        else:
            print("Nenhum aluno cadastrado.")

    def mostrar_aprovados(self):
        aprovados = self.turma.listar_aprovados()
        if aprovados:
            print("Lista de Aprovados:")
            for aluno in aprovados:
                print(aluno)
        else:
            print("Nenhum aluno cadastrado.")

    def mostrar_reprovados(self):
        reprovados = self.turma.listar_reprovados()
        if reprovados:
            print("Lista de Reprovados:")
            for aluno in reprovados:
                print(aluno)
        else:
            print("Nenhum aluno cadastrado.")

    def mostrar_notas_normalizadas(self):
        normalizadas = self.turma.notas_normalizadas()
        if normalizadas is None:
            print("Nenhum aluno cadastrado.")
        else:
            print("Notas normalizadas (0 a 1):")
            for i, aluno in enumerate(self.turma.alunos):
                print(f"{aluno.nome}: {np.round(normalizadas[i], 2)}")

    def mostrar_notas_ponderadas(self):
        pesos = np.array([0.5, 0.3, 0.2])
        ponderadas = self.turma.nota_ponderada(pesos)
        if ponderadas is None:
            print("Nenhum aluno cadastrado.")
        else:
            print("Notas ponderadas:")
            for i, aluno in enumerate(self.turma.alunos):
                print(f"{aluno.nome}: {ponderadas[i]:.2f}")

    def mostrar_estatisticas_avancadas(self):
        pesos = np.array([0.5, 0.3, 0.2])
        ponderadas = self.turma.nota_ponderada(pesos)
        if ponderadas is None:
            print("Nenhum aluno cadastrado.")
            return
        print(f"Média: {np.mean(ponderadas):.2f}")
        print(f"Mediana: {np.median(ponderadas):.2f}")
        print(f"Desvio padrão: {np.std(ponderadas):.2f}")
        print("Correlação entre disciplinas:")
        print(np.round(np.corrcoef(self.turma.matriz_notas().T), 2))

    def gerar_graficos(self):
        matriz = self.turma.matriz_notas()
        if matriz is None:
            print("Nenhum aluno cadastrado.")
            return
        grafico_histograma(matriz)
        grafico_barras(np.mean(matriz, axis=0))

    def sair(self):
        print("Encerrando...")
        self.turma.salvar()
        exit()