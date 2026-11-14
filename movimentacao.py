
import config

def ocupacao_positiva(ocupadas):
    if ocupadas < 0 or ocupadas > config.CAPACIDADE_MAXIMA:
        return False
    return True

def tem_vaga(ocupadas):
    return ocupacao_positiva(ocupadas) and ocupadas < config.CAPACIDADE_MAXIMA

def tem_veiculo(ocupadas):
    return ocupacao_positiva(ocupadas) and ocupadas > 0


def registrar_entrada(ocupadas):
    ocupadas = ocupadas + 1
    vagas_livres = config.CAPACIDADE_MAXIMA - ocupadas
    print("Entrada registrada com sucesso!")
    print("Vagas livres: ", vagas_livres)
    return ocupadas


def registrar_saida(ocupadas):
    return ocupadas - 1


def pedir_horas():
    horas = 0
    valido = False
    while not valido:
        try:
            horas = int(input("Quantas horas o veículo ficou: "))
        except ValueError:
            print("Informe só números inteiros")
        else:
            if horas <= 0:
                print("O valor informado precisa ser maior que 0")
            else:
                valido = True
        finally:
            print("---------------------------------")
        return horas