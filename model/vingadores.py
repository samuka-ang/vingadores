import os
import time
import enum
 
class Vingador:
    lista_vingadores = []
    lista_poderes = [
        ""
    ]
   
    class categoria_vingadores:
        HUMANO = "Humano"
        META_HUMANO = "Meta-humano"
        ALIENIGENA = "Alienígena"
        DEUS = "Deus"
        ANDROIDE = "Androide"
   
    def __init__(self, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_de_forca):
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_de_forca = nivel_de_forca
        self.convocado = False
        self.tornozeleira = False
        self.chip_gps = False
       
        # Adicionar automaticamente à lista de Vingadores
        Vingador.lista_vingadores.append(self)
 
    def __str__(self):
        return f'{self.nome_heroi.ljust(20)} | {self.nome_real.ljust(20)} | {self.categoria.ljust(20)} | ' \
               f'{"Convocado" if self.convocado else "Não Convocado".ljust(20)} | ' \
               f'{"Tornozeleira Aplicada" if self.tornozeleira else "Sem Tornozeleira".ljust(20)} | ' \
               f'{"Chip GPS Aplicado" if self.chip_gps else "Sem Chip GPS".ljust(20)}'
 
 
class Interface():
    animacao = True
 
    @staticmethod
    def animacaoLinhas(testiculo, duracao):
        for ch in testiculo:
            time.sleep(duracao)
            print(ch, end="", flush=True)
 
    @staticmethod
    def menu():
        if Interface.animacao == True:
            Interface.animacaoLinhas('''
 
 
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──██████─██████████████─████████████████───██████████████─██████████████───██████████████─██████████████─██████████████─
─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██──██░░██─██░░██████████─██░░████████░░██───██░░██████░░██─██░░██████░░██───██░░██████░░██─██░░██████████─██░░██████████─
─██░░██──██░░██─██░░██─────────██░░██────██░░██───██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─██░░██─────────██░░██─────────
─██░░██████░░██─██░░██████████─██░░████████░░██───██░░██──██░░██─██░░██████░░████─██░░██████░░██─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████░░██─██░░██████████─██░░██████░░████───██░░██──██░░██─██░░████████░░██─██░░██████░░██─██████████░░██─██░░██████████─
─██░░██──██░░██─██░░██─────────██░░██──██░░██─────██░░██──██░░██─██░░██────██░░██─██░░██──██░░██─────────██░░██─██░░██─────────
─██░░██──██░░██─██░░██████████─██░░██──██░░██████─██░░██████░░██─██░░████████░░██─██░░██──██░░██─██████████░░██─██░░██████████─
─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████──██████─██████████████─██████──██████████─██████████████─████████████████─██████──██████─██████████████─██████████████─
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
''', 0.01)
 
        Interface.animacao = False
        print('\n')
        print('Seja bem-viado! Escolha uma das opções abaixo\n')
        print('1. Cadastrar vingador')
        print('2. Ver lista de vingadores ')
        print('3. Convocar vingador')
        print('4. Aplicar tornozeleira')
        print('5. Aplicar chip GPS')
        print('6. Emitir mandado de prisão')
        print('7. Sair')
        Interface.ler_opcao_usuario(Interface.Cadastro, Interface.listar_vingadores, Interface.convocar_vingador,
                                     Interface.aplicar_tornozeleira, Interface.aplicar_chip_gps, Interface.emitir_mandado, Interface.sair)
 
    @staticmethod
    def VoltarMenu():
        input("\nPressione Enter para voltar ao menu...")
        os.system("cls")
        Interface.menu()
 
    @staticmethod
    def Cadastro():
        nome_heroi = input('Nome do herói: ')
        nome_real = input('Nome real: ')
        categoria = input('Categoria (Humano, Meta-humano, Androide, Deidade, Alienígena): ')
 
        if categoria not in [Vingador.categoria_vingadores.HUMANO, Vingador.categoria_vingadores.META_HUMANO,
                             Vingador.categoria_vingadores.ANDROIDE, Vingador.categoria_vingadores.DEUS,
                             Vingador.categoria_vingadores.ALIENIGENA]:
            print("Categoria inválida! Tente novamente.")
            Interface.Cadastro()
            return
 
        poderes = input('Poderes (separados por vírgula): ').split(",")
        poder_principal = input('Poder principal: ')
        fraquezas = input('Fraquezas (separadas por vírgula): ').split(",")
        nivel_forca = int(input('Nível de força (0 a 10000): '))
 
        if nivel_forca < 0 or nivel_forca > 10000:
            print("Nível de força inválido!")
            Interface.Cadastro()
            return
       
        vingador = Vingador(nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca)
        Vingador.lista_vingadores.append(vingador)
        print(f'Vingador {nome_heroi} cadastrado com sucesso!')
        Interface.VoltarMenu()
 
    @staticmethod
    def listar_vingadores():
        if not Vingador.lista_vingadores:
            print("Nenhum vingador cadastrado.")
        else:
            print(f'{"Nome do Herói".ljust(20)} | {"Nome Real".ljust(20)} | {"Categoria".ljust(20)} | '
                  f'{"Convocado".ljust(20)} | {"Tornozeleira".ljust(20)} | {"Chip GPS".ljust(20)}')
            for vingador in Vingador.lista_vingadores:
                print(vingador)
            Interface.VoltarMenu()
 
    @staticmethod
    def convocar_vingador():
        nome = input("Digite o nome do herói ou nome real do vingador para convocar: ")
        vingador_encontrado = None
        for vingador in Vingador.lista_vingadores:
            if vingador.nome_heroi.lower() == nome.lower() or vingador.nome_real.lower() == nome.lower():
                vingador_encontrado = vingador
                break
        if vingador_encontrado:
            vingador_encontrado.convocado = True
            print(f'{vingador_encontrado.nome_heroi} foi convocado com sucesso!')
        else:
            print("Vingador não encontrado.")
        Interface.VoltarMenu()
 
    @staticmethod
    def aplicar_tornozeleira():
        nome = input("Digite o nome do herói ou nome real do vingador para aplicar a tornozeleira: ")
        vingador_encontrado = None
        for vingador in Vingador.lista_vingadores:
            if vingador.nome_heroi.lower() == nome.lower() or vingador.nome_real.lower() == nome.lower():
                vingador_encontrado = vingador
                break
        if vingador_encontrado:
            if not vingador_encontrado.convocado:
                print(f"{vingador_encontrado.nome_heroi} precisa ser convocado antes de aplicar a tornozeleira!")
            else:
                vingador_encontrado.tornozeleira = True
                if vingador_encontrado.nome_heroi.lower() == "thor" or vingador_encontrado.nome_heroi.lower() == "hulk":
                    print(f"{vingador_encontrado.nome_heroi} resiste à tornozeleira!")
                else:
                    print(f"Tornozeleira aplicada em {vingador_encontrado.nome_heroi}.")
        else:
            print("Vingador não encontrado.")
        Interface.VoltarMenu()
 
    @staticmethod
    def aplicar_chip_gps():
        nome = input("Digite o nome do herói ou nome real do vingador para aplicar o chip GPS: ")
        vingador_encontrado = None
        for vingador in Vingador.lista_vingadores:
            if vingador.nome_heroi.lower() == nome.lower() or vingador.nome_real.lower() == nome.lower():
                vingador_encontrado = vingador
                break
        if vingador_encontrado:
            if not vingador_encontrado.tornozeleira:
                print(f"A tornozeleira precisa ser aplicada em {vingador_encontrado.nome_heroi} antes do chip GPS!")
            else:
                vingador_encontrado.chip_gps = True
                print(f"Chip GPS aplicado em {vingador_encontrado.nome_heroi}.")
        else:
            print("Vingador não encontrado.")
        Interface.VoltarMenu()
 
    @staticmethod
    def emitir_mandado():
        nome = input("Digite o nome do herói ou nome real do vingador para emitir mandado: ")
        vingador_encontrado = None
        for vingador in Vingador.lista_vingadores:
            if vingador.nome_heroi.lower() == nome.lower() or vingador.nome_real.lower() == nome.lower():
                vingador_encontrado = vingador
                break
        if vingador_encontrado:
            print(f"Mandado de prisão emitido para {vingador_encontrado.nome_heroi}.")
        else:
            print("Vingador não encontrado.")
        Interface.VoltarMenu()
 
    @staticmethod
    def sair():
        print("Encerrando o programa...")
        time.sleep(1)
        exit()
 
    @staticmethod
    def ler_opcao_usuario(*metodos):
        opcao = input("\nDigite aqui: ")
        os.system('cls')
        try:
            if opcao.isdigit() and 1 <= int(opcao) <= len(metodos):
                metodos[int(opcao) - 1]()
            else:
                print("Opção inválida. Tente novamente.")
                Interface.VoltarMenu()
        except:
            print("Opção inválida. Tente novamente.")
            Interface.VoltarMenu()
           
 
from vingadores import Interface from vinga... por JOÃO PEDRO MINUCCI REGUEIRA
JOÃO PEDRO MINUCCI REGUEIRA
10:50
from vingadores import Interface
from vingadores import Vingador
 
def main():
    Vingador('Homem de Ferro', 'Tony Stark', 'Humano', ['Inteligência', 'Engenharia', 'Rico'], 'Armadura', ['Arrogância', 'Orgulho'], 2000)
    Vingador('Capitão América', 'Steve Rogers', 'Humano', ['Força', 'Habilidade em Combate', 'Liderança'], 'Escudo', ['Inexperiência no mundo moderno'], 8000)
    Vingador('Thor', 'Thor Odinson', 'Deus', ['Força sobre-humana', 'Controle sobre raios', 'Imortalidade'], 'Mjolnir', ['Desatenção', 'Impulsividade'], 10000)
    Vingador('Hulk', 'Bruce Banner', 'Humano', ['Força sobre-humana', 'Regeneração', 'Durabilidade'], 'Força', ['Raiva', 'Controle mental'], 10000)
    Vingador('Viúva Negra', 'Natasha Romanoff', 'Humano', ['Habilidade em combate', 'Espionagem', 'Agilidade'], 'Combate corpo a corpo', ['Sem poderes sobre-humanos'], 7000)
    Vingador('Gavião Arqueiro', 'Clint Barton', 'Humano', ['Habilidade com arcos e flechas', 'Acuidade visual', 'Combate'], 'Arcos e flechas', ['Sem poderes sobre-humanos'], 6500)
    Vingador('Pantera Negra', 'T\'Challa', 'Humano', ['Força', 'Velocidade', 'Tecnologia avançada', 'Habilidades de combate'], 'Agilidade e reflexos', ['Dúvidas morais'], 9000)
    Vingador('Feiticeira Escarlate', 'Wanda Maximoff', 'Meta-humana', ['Magia', 'Manipulação de realidade', 'Telecinese'], 'Manipulação de realidade', ['Falta de controle emocional'], 10000)
    Vingador('Wolverine', 'Logan', 'Mutante', ['Regeneração', 'Força sobre-humana', 'Feras'], 'Garras de adamantium', ['Perda de controle', 'Vingança'], 9000)
    Vingador('Ciclope', 'Scott Summers', 'Mutante', ['Visão de feixe de energia', 'Habilidade estratégica'], 'Visão de feixe', ['Cegueira'], 8000)
    Vingador('Tempestade', 'Ororo Munroe', 'Mutante', ['Controle sobre o clima', 'Voo'], 'Manipulação de clima', ['Descontrole emocional'], 8000)
    Vingador('Jean Grey', 'Jean Grey', 'Mutante', ['Telepatia', 'Telecinese', 'Manipulação de energia'], 'Telecinese', ['Falta de controle sobre Phoenix'], 9500)
    Vingador('Professor X', 'Charles Xavier', 'Mutante', ['Telepatia', 'Habilidade de manipulação mental', 'Liderança'], 'Telepatia', ['Vulnerabilidade física'], 7500)
    Vingador('Fera', 'Henry McCoy', 'Mutante', ['Força sobre-humana', 'Agilidade', 'Intelecto'], 'Força física', ['Insegurança devido à aparência'], 8500)
    Vingador('Gambit', 'Remy LeBeau', 'Mutante', ['Manipulação de energia', 'Acuidade física'], 'Cartas carregadas', ['Impulsividade'], 7500)
    Vingador('Míssil', 'Rogue', 'Mutante', ['Absorção de habilidades', 'Super força', 'Invulnerabilidade'], 'Absorção de poderes', ['Perda de controle sobre os poderes'], 9000)
 
    Interface().menu()
 
if __name__ == "__main__":
    main()
 
tem menu de contexto