import numpy as np
import json
from core.aluno import Aluno

class Turma:
    def __init__(self):
        self.alunos = []

    # Adiciona aluno a lista
    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
            print(f"Aluno {aluno.nome} adicionado com notas {aluno.notas}.")
        else:
            print("Erro: deve passar uma instância da classe Aluno.")

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return
        print("\n--- Lista de Alunos ---")
        for aluno in self.alunos:
            print(aluno)

    def atualizar_aluno(self, nome, novas_notas):
        aluno = self.buscar_por_nome(nome)
        if aluno:
            if len(novas_notas) != len(aluno.notas):
                print("Quantidade de notas não confere.")
                return
            aluno.notas = novas_notas
            print(f"Notas de {nome} atualizadas para {novas_notas}.")
        else:
            print("Aluno não encontrado.")

    def remover_aluno(self, nome):
        antes = len(self.alunos)
        self.alunos = [a for a in self.alunos if a.nome.lower() != nome.lower()]
        if len(self.alunos) < antes:
            print(f"Aluno {nome} removido.")
        else:
            print("Aluno não encontrado.")

    def buscar_por_nome(self, nome):
        for aluno in self.alunos:
            if aluno.nome.lower() == nome.lower():
                return aluno
        return None

    def melhor_aluno(self):
        if not self.alunos:
            return None
        return max(self.alunos, key=lambda a: a.calcular_media())

    def media_da_turma(self):
        if not self.alunos:
            return None
        medias = [aluno.calcular_media() for aluno in self.alunos]
        return sum(medias) / len(medias)

    def matriz_notas(self):
        if not self.alunos:
            return None
        return np.array([aluno.notas for aluno in self.alunos])

    def media_por_disciplina(self):
        matriz = self.matriz_notas()
        if matriz is None:
            return None
        return np.mean(matriz, axis=0)

    def notas_normalizadas(self):
        matriz = self.matriz_notas()
        if matriz is None:
            return None
        minimos = matriz.min(axis=0)
        maximos = matriz.max(axis=0)
        denominador = np.where((maximos - minimos) == 0, 1, maximos - minimos)
        return (matriz - minimos) / denominador

    def nota_ponderada(self, pesos):
        matriz = self.matriz_notas()
        if matriz is None:
            return None
        return np.dot(matriz, pesos)

    def listar_aprovados(self):
        return [a for a in self.alunos if a.aprovado()]

    def listar_reprovados(self):
        return [a for a in self.alunos if not a.aprovado()]

    def salvar(self, arquivo="dados.json"):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([a.__dict__ for a in self.alunos], f, ensure_ascii=False, indent=4)

    def carregar(self, arquivo="dados.json"):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.alunos = [Aluno(**d) for d in dados]
        except FileNotFoundError:
            self.alunos = []
