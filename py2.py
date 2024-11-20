def invertir_cadena(cadena):
    # Divideix la cadena en paraules
    paraules = cadena.split()
    # Inverteix les paraules
    paraules_invertides = paraules[::-1]
    # Uneix les paraules invertides en una nova cadena
    cadena_invertida = ' '.join(paraules_invertides)
    return cadena_invertida
