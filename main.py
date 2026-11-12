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