def verificar_numero(numero):
    if numero > 0:
        return "Número positivo"
    elif numero < 0:
        return "Número negativo"
    else:
        return "Número zero"

def eh_par(numero):
    if numero % 2 == 0:
        return True
    return False