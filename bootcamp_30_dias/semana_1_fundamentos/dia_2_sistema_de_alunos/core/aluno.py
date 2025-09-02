class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas  # [matemática, física, programação]

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def aprovado(self):
        return self.calcular_media() >= 7

    def __str__(self):
        return f"{self.nome} | Notas: {self.notas} | Média: {self.calcular_media():.2f}"
