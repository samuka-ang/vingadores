class vingadores:

    lista_ving = []

    def __init__(self, nomeheroi, nomereal, categoria, poderes, poderpri, fraq, lvlforca):
        self.nomeheroi = nomeheroi
        self.nomereal = nomereal
        self.categoria = categoria
        self.poderes = poderes
        self.poderpri = poderpri
        self.fraq = fraq
        self.lvlforca = lvlforca
        vingadores.lista_ving.append(self)

    @classmethod
    def vinglist(cls):
        print(f'{'Nome do heroí'.ljust(15)} | {'Nome real'.ljust(15)} | {'Categoria'.ljust(10)} | {'Poderes'.ljust(45)} | {'Poder principal'.ljust(18)} | {'Fraqueza'.ljust(25)} | {'Nivel de força'.ljust(10)}')
        for ving in vingadores.lista_ving:
            print(f'{str(ving.nomeheroi).ljust(15)} | {str (ving.nomereal).ljust(15)} | {str (ving.categoria).ljust(10)} | {str (ving.poderes).ljust(45)} | {str (ving.poderpri).ljust(18)} | {str (ving.fraq).ljust(25)} | {str (ving.lvlforca).ljust(10)}')
   
    def __str__(self):
        return f'{'Nome do heroí'.ljust(15)} | {'Nome real'.ljust(15)} | {'Categoria'.ljust(10)} | {'Poderes'.ljust(45)} | {'Poder principal'.ljust(18)} | {'Fraqueza'.ljust(25)} | {'Nivel força'.ljust(10)} \n{str(self.nomeheroi).ljust(15)} | {str (self.nomereal).ljust(15)} | {str (self.categoria).ljust(10)} | {str (self.poderes).ljust(45)} | {str (self.poderpri).ljust(18)} | {str (self.fraq).ljust(25)} | {str (self.lvlforca).ljust(10)}'

homem_aranha = vingadores('Homem-Aranha', 'Peter Parker', 'Humano', 'Força e agilidade sobre-humanas', 'Tecnologia', 'Perder seus entes queridos', 'Moderado')
capitao_america = vingadores('Capitão América', 'Steve Rogers', 'Humano', 'Força e resistência aprimoradas', 'Escudo vibranium', 'Perder sua moral', 'Alto')
thor = vingadores('Thor', 'Thor Odinson', 'Deus', 'Controle sobre o trovão e força sobre-humana', 'Mjolnir', 'Perder seu poder divino', 'Extremo')

vingadores.vinglist()
print()
print(thor)