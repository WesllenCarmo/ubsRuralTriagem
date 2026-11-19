# criação da estrutura de dados (POO) e listas de filas
# Deyvison e Henrique
# classe com variáveis nome, idade, e condicao
# duas listas vazias, uma da fila prioritária e a outra fila comum
class Paciente:
    def __init__(self, nome, idade, gestante):
        self.nome = nome
        self.idade = idade
        self.gestante = gestante

    def eh_prioritario(self):
        return self.idade >= 60 or self.gestante

    def apresentar(self):
        return f"{self.nome} - {self.idade} anos"

fila_prioritaria = []
fila_comum = []
# Lógica das funcionalidades mandar pacientte para a list da de espera específica e chamar pacientes
# Felipe e Wesllen
# função mandar paciente para a lista de espera com verificação se idade >= 60 ou condicao for gestante -> fila prioritária, se não, fila comum

# função chamar paciente: se houver pacientes na lista de prioridade, chama eles primeiro, se não, chama fila comum. Se não tiver ninguém nas listas, não chama ninguém
def chamarProximoPaciente(fila_prioritaria, fila_comum):
    if fila_prioritaria:
        print("Próximo(a) paciente é: {}".format(fila_prioritaria[0].apresentar()))
        fila_prioritaria.pop(0)
    elif fila_comum:
        print("Próximo(a) paciente é: {}".format(fila_comum[0].apresentar()))
        fila_comum.pop(0)
    else:
        print("Não há mais pacientes!")
chamarProximoPaciente(fila_prioritaria, fila_comum)
# Testes / simulação 
# Iago e Eduardo
# testar possiblidades de erro para soluções
