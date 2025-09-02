from core.turma import Turma
from menu import Menu

def main():
    turma = Turma()
    turma.carregar()  # Carrega dados do arquivo JSON, se existir
    menu = Menu(turma)
    menu.exibir()     # Inicia o menu principal

if __name__ == "__main__":
    main()
