import os
from model.vingadores import vingadores

class layout:
 
    @staticmethod
    def titulo():
        print('''
             
░█──░█ ▀█▀ ░█▄─░█ ░█▀▀█ ─█▀▀█ ░█▀▀▄ ░█▀▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
─░█░█─ ░█─ ░█░█░█ ░█─▄▄ ░█▄▄█ ░█─░█ ░█──░█ ░█▄▄▀ ░█▀▀▀ ─▀▀▀▄▄ 
──▀▄▀─ ▄█▄ ░█──▀█ ░█▄▄█ ░█─░█ ░█▄▄▀ ░█▄▄▄█ ░█─░█ ░█▄▄▄ ░█▄▄▄█
              
              ''')
 
    @staticmethod    
    def menu():
        os.system('cls')
        layout.titulo()
        print()
        print('Menu principal')
        print('1. Cadastrar novo VINGADOR')
        print('2. Listar todos os VINGADORES')
        print('3. Sair')
        print()
        layout.opcao()

    @staticmethod
    def titulocad(tit):
        os.system('cls')
        layout.titulo
        print(f'{str(tit).upper()}')
        print('*' * 20)
        print()

    @staticmethod
    def cadastro():
        layout.titulocad('cadastro novo VINGADOR')
        nomeheroi = input('Nome do Heroí: ')
        nomereal = input('Nome real: ')
        categoria = input('Categoria: ')
        poderes = input('Poderes: ')
        poderpri = input('Poderes principal: ')
        fraq = input('Fraqueza: ')
        lvlforca = input('Nivel de força: ')

        ving = vingadores(nomeheroi, nomereal, categoria, poderes, poderpri, fraq, lvlforca)
 
        print(f'O carro foi cadastrado: \n{ving}')

    @staticmethod
    def opcao():
        opcao = int(input('Digite sua opção: '))
 
        try:
            if opcao == 1:
                layout.cadastro()
            elif opcao == 2:
                layout.titulocad('listando carros')
                vingadores.vinglist()
            elif opcao == 3:
                print('Encerrando o programa')
                exit()
            else:
                print('Digite uma opção válida!')
        except ValueError:
                print('Você deve digitar um número inteiro')
       
        layout.voltarmenu()
 
    @staticmethod
    def voltarmenu():
        print()
        input('Digite qualquer tecla para voltar ao menu')
        os.system('cls')
        layout.menu()