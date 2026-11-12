from xml.dom.pulldom import PROCESSING_INSTRUCTION

import financeiro as fin
import config

def mostrar_vagas(ocupadas):
    vagas_livres = config.CAPACIDADE_MAXIMA - ocupadas
    taxa = ocupadas * 100 / config.CAPACIDADE_MAXIMA
    print("-------- CONTROLE DE VAGAS --------")
    print()
    print("Capacidade de Vagas: ", config.CAPACIDADE_MAXIMA)
    print("Vagas ocupadas: ", ocupadas)
    print("Vagas disponíveis: ", vagas_livres)
    print("Taxa de ocupação: ",str(int(taxa)) + "%")
    print()
    print("------------------------------------")


def mostrar_faturamento(faturamento, saidas):
    media = fin.calcular_media(faturamento, saidas)
    print("-------- CONTROLE DE FATURAMENTO --------")
    print()
    print ("Total de faturamento: ", fin.ajustar_dinheiro(faturamento))
    print("Saídas registradas: ", saidas)
    print("Média por saída: ", fin.ajustar_dinheiro(media))
    print()
    print("-----------------------------------------")


def mostrar_relatorios(entradas, saidas, ocupadas, faturamento):
    vagas_livres = config.CAPACIDADE_MAXIMA - ocupadas
    print("-------- CONTROLE DE RELATORIOS --------")
    print()
    print("Total de entradas: ", entradas)
    print("Total de saidas: ", saidas)
    print("Veículos estacionados: ", ocupadas)
    print("Vagas livres: ", vagas_livres)
    print("Faturamento: ", fin.ajustar_dinheiro(faturamento))
    print()
    print("------------------------------------------")


def mostrar_precos():
    print("-------- TABELA DE PREÇOS --------")
    print()
    print("Tarifa por hora: ", fin.ajustar_dinheiro(config.TARIFA_POR_HORA))
    print("Funciomento: ", config.HORARIO_FUINCIONAMENTO)
    print()
    print("Simulação de valores: ")
    for horas in range(1, 6):
        valor = fin.calcular_cobranca(horas)
        print(str(horas) + " hora(s) ->", fin.ajustar_dinheiro(valor))
    print()
    print("----------------------------------")


def mostrar_comprovante(horas, valor, ocupadas):
    vagas_livres = config.CAPACIDADE_MAXIMA - ocupadas
    print("-------- CONTROLE DE COMPROVANTE --------")
    print()
    print("Tempo de permanência: ", horas, "hora(s)")
    print("Tarifa por hora: ", fin.ajustar_dinheiro(config.TARIFA_POR_HORA))
    print("Valor a pagar: ", fin.ajustar_dinheiro(valor))
    print("Vagas livres: ", vagas_livres)
    print("-----------------------------------------")


def mostrar_resumo_final(entradas, saidas, faturamento):
    print("-------- CONTROLE DE RESUMO FINAL --------")
    print("Total de entradas: ", entradas)
    print("Total de saidas: ", saidas)
    print("Faturamento: ", fin.ajustar_dinheiro(faturamento))
    print("------------------------------------------")
    print("Obrigado por usar o SmartPark! Até a próxima!")


















