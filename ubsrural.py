# Classe e listas de filas (Deyvison e Henrique)
## classe com variáveis 'nome', 'idade', e 'condicao'
class Paciente:
    def __init__(self, nome, idade, condicao):
        self.nome = nome
        self.idade = idade
        self.condicao = condicao

    def apresentar(self):
        return f"{self.nome} - {self.idade} anos"

## duas listas vazias, uma da fila prioritária e a outra fila comum
fila_prioritaria = []
fila_comum = []

# Lógica das funcionalidades (Felipe e Wesllen):
## Função mandar paciente para a lista de espera com verificação se idade >= 60 ou condicao for gestante -> fila prioritária; senão -> fila comum.
## Função chamar pacientes na lista de prioridade primeiro, senão, chama fila comum. Se não tiver ninguém nas listas, não chama ninguém.
def cadastrarPacientes():
    print("Cadastro de pacientes:")
    nome = str(input("digite o nome: "))
    idade = int(input("digite a idade: "))
    condicao = str(input("digite a condição: "))

    return [nome, idade, condicao]

def adicionarPacienteNasListas():
    paciente = cadastrarPacientes()

    if paciente[1] >= 60 or paciente[2] == "gestante":
        fila_prioritaria.append(paciente)
    else:
        fila_comum.append(paciente)
        

def chamarProximoPaciente(fila_prioritaria, fila_comum):
    if fila_prioritaria:
        print("Próximo(a) paciente é: {}".format(fila_prioritaria[0].apresentar()))
        fila_prioritaria.pop(0)
    elif fila_comum:
        print("Próximo(a) paciente é: {}".format(fila_comum[0].apresentar()))
        fila_comum.pop(0)
    else:
        print("Não há mais pacientes!")
#chamarProximoPaciente(fila_prioritaria, fila_comum)


# Testes / simulação (Iago e Eduardo)
## testar possiblidades de erro para soluções

while True:
    print("\nmenu de funcionalidades: ")
    print("1: cadastrar")
    print("2: mostrar fila")
    print("3: proximo paciente da fila")
    print("0: sair\n")
    comando = input("digite o que deseja fazer: ")
    print("\n")

    if comando == "0":
        break
    elif comando == "1":
        adicionarPacienteNasListas()
    elif comando == "2":
        print("Fila de pacientes:")

        print("Prioritarios:")
        for i, pessoa in enumerate(fila_prioritaria, start=1):
            print(f"{i} - nome: {pessoa[0]}, idade: {pessoa[1]}, condição: {pessoa[2]}")

        print("\nNão Prioritarios:")
        for i, pessoa in enumerate(fila_comum, start=len(fila_prioritaria)+1):
            print(f"{i} - nome: {pessoa[0]}, idade: {pessoa[1]}, condição: {pessoa[2]}")

    elif comando == "3":
        print("funcionalidade em construção.")
    else:
        print("opção invalida. tente novamente.")
