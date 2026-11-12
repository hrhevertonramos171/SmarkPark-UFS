from config import TARIFA_POR_HORA, PERMANENCIA_MINIMA

def calcular_cobranca(horas):
    if horas < PERMANENCIA_MINIMA:
        horas = PERMANENCIA_MINIMA
    valor = float(horas) * TARIFA_POR_HORA
    return valor

def somar_faturamento(faturamento, valor):
    return faturamento + valor

def calcular_media(faturamento, saidas):
    if saidas == 0:
        return 0.00
    return faturamento / saidas

def ajustar_dinheiro(valor):
    texto= f"{valor:.2f}"
    texto = texto.replace(",", ".")
    return "R$" + texto