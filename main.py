import config
import movimentacao
import financeiro as fin
from relatorios import mostrar_vagas, mostrar_relatorios, mostrar_faturamento
from relatorios import mostrar_precos, mostrar_comprovante, mostrar_resumo_final


def mostrar_menu():
    print()
    print("-" * 37)
    print("  SMARTPARK - SISTEMA")
    print("-" * 37)
    print("1 - Registrar entrada de veículo")
    print("2 - Registrar a saída de veículo")
    print("3 - Consultar vagas disponíveis")
    print("4 - Consultar faturamento")
    print("5 - Relatório de movimentações")
    print("6 - Consultar tabela de preços")
    print("0 - Encerrar sistema")
    print("-" * 37)


def ler_opcao():
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        opcao = -1
    return opcao


ocupadas = config.OCUPACAO_INCIAL
faturamento = config.FATURAMENTO_INICIAL
total_entradas = 0
total_saidas = 0

print("Bem vindo ao SMARTPARK")
print("Horário de funcionamento: ", config.HORARIO_FUINCIONAMENTO)

opcao = -1
while opcao != 0:
    mostrar_menu()
    opcao = ler_opcao()
    print()

    match opcao:
        case 1:
            if movimentacao.tem_vaga(ocupadas):
                ocupadas = movimentacao.registrar_entrada(ocupadas)
                total_entradas = total_entradas + 1
            else:
                print("Estacionamento lotado! Impossível registrar entrada agora.")

        case 2:
            if movimentacao.tem_veiculo(ocupadas):
                horas = movimentacao.pedir_horas()
                valor = fin.calcular_cobranca(horas)
                ocupadas = movimentacao.registrar_saida(ocupadas)
                total_saidas = total_saidas + 1
                faturamento = fin.somar_faturamento(faturamento, valor)
                mostrar_comprovante(horas, valor, ocupadas)
            else:
                print("Não tem nenhum veículo estacionado")

        case 3:
            mostrar_vagas(ocupadas)

        case 4:
            mostrar_faturamento(faturamento, total_saidas)

        case 5:
            mostrar_relatorios(total_entradas, total_saidas, ocupadas)

        case 6:
            mostrar_precos()

        case 0:
            print("Sistema encerrado")
            mostrar_resumo_final(total_entradas, total_saidas, faturamento)

        case _:
            print("Opção invalida! Digite um número de 0 à 6")
